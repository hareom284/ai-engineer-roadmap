# Python idioms for a PHP engineer

**Plan day:** Day 1 (Mon 14 Sep) · **Status:** `not-started`
_Status values: `not-started` → `learning` → `can-explain`. You are done when you can answer every question below out loud, without notes, in under two minutes each._

## In my own words
_One paragraph for a senior engineer who has never used this. No jargon you cannot define._



## Must be able to answer
- [ ] Why do type hints not raise at runtime, and what does that imply for anything crossing an API boundary?
- [ ] When does a mutable default argument bite you, and what is the fix?
- [ ] Rewrite an append loop as a comprehension. When is a comprehension the wrong choice?
- [ ] What does a `with` block guarantee that try/finally does by hand?

## Reference explanations
_Explained with Claude, kept here to look back at. Still write your own answers above and in "In my own words"._

### Type hints do not raise at runtime

**The rule:** a type hint is a **label**, not a guard. Python stores it and moves on. Nothing checks it when the code runs.

**Analogy:** a sticker on a box saying "books". The delivery driver never opens the box. You only find out it holds glass when you try to put it on the shelf and it breaks.

**PHP vs Python:**

```php
function addOne(int $n): int { return $n + 1; }
addOne("abc");   // PHP: TypeError right here, at the call
```

```python
def add_one(n: int) -> int:
    return n + 1

print(add_one.__annotations__)   # {'n': <class 'int'>, 'return': <class 'int'>}  <- just stored
add_one("5")                     # no error at the call...
                                 # TypeError: can only concatenate str (not "int") to str
                                 #   ...it fails later, inside, at the `+`
```

The same with a dataclass — this is `scratch/03_dataclass.py`:

```python
from dataclasses import dataclass

@dataclass
class Order:
    id: str
    total: int

o = Order(id="A1", total="not a number")
print(o)   # Order(id='A1', total='not a number')  <- no error at all
```

**Why this is dangerous at an API boundary:** "API boundary" = anywhere data comes from outside your code: a JSON request body, a form, a database row, a file, an LLM response. Outside data does not care about your hints.

```python
data = json.loads('{"id": "A1", "total": "250"}')   # total is a STRING in the JSON
order = Order(**data)                               # accepted silently
order.total > 100
# TypeError: '>' not supported between instances of 'str' and 'int'
```

The bad value got **in** at the boundary, and the crash happens **later**, somewhere else, which makes it hard to trace.

**The fix:** validate at the boundary. That is exactly what **Pydantic** does (Day 2): it reads your hints and actually enforces them — converting `"250"` to `250`, or raising `ValidationError` for `"not a number"`. FastAPI uses Pydantic for every request body for this reason.

**So what are hints for?** Your editor (autocomplete, red underlines), type checkers like `mypy` / `pyright` that check the code *before* it runs, and libraries like Pydantic that read them on purpose.

**Interview answer (under 30 seconds):** "Python type hints are metadata. The interpreter stores them but does not enforce them, so wrong types pass silently and fail later, far from the cause. They help editors and static checkers, but data crossing a boundary — requests, JSON, LLM output — has to be validated at runtime, which is why FastAPI uses Pydantic models."

### Mutable default argument

**Mutable** = can be changed after it is created. `list`, `dict`, `set` are mutable. `int`, `str`, `None`, `tuple` are not.

**The rule:** a default value is created **once, when Python reads the `def` line** — not each time the function is called. Every call that uses the default gets that same one object.

**Analogy:** the default is a whiteboard fixed to the meeting-room wall, not a fresh sheet of paper per meeting. Whatever the last meeting wrote is still there.

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item.__defaults__)   # ([],)          <- the one shared list, created at def time
print(add_item("a"))           # ['a']
print(add_item("b"))           # ['a', 'b']     <- surprise: "a" is still there
print(add_item.__defaults__)   # (['a', 'b'],)  <- the default itself has changed
print(add_item("c", []))       # ['c']          <- fine: caller passed their own list
print(add_item("d"))           # ['a', 'b', 'd'] <- back to the shared list
```

**When it bites:** only when all three are true —
1. the default is mutable (`[]`, `{}`, `set()`, or an object),
2. the function changes it in place (`append`, `d[key] = ...`, `update`, `add`),
3. the function is called more than once without passing that argument.

In a web server this is nasty: the process lives for a long time, so data from one request can leak into the next user's request.

**Why PHP never had this:** PHP arrays are copied by value and the default is rebuilt on every call. `function f($items = [])` always starts empty.

**The fix — use `None` as the default and create the list inside:**

```python
def add_item(item, items=None):
    if items is None:      # use `is None`, not `if not items` (an empty list passed in would be replaced)
        items = []         # new list on every call
    items.append(item)
    return items
```

For dataclasses and Pydantic, use a factory instead of `= []`:

```python
from dataclasses import dataclass, field

@dataclass
class Cart:
    items: list[str] = field(default_factory=list)   # new list per Cart
```

(A dataclass refuses `items: list = []` with a `ValueError`. Pydantic copies defaults per instance, so `= []` is safe there, but `Field(default_factory=list)` is the clearer habit.)

**Interview answer (under 30 seconds):** "Default values are evaluated once at function definition, so a mutable default like a list is shared across calls. If the function mutates it, state leaks between calls. The fix is to default to `None` and create a new list inside the function, or use `default_factory` in dataclasses."

### Comprehensions

**The rule:** a comprehension builds a new list (or dict, or set) from another collection in one expression. It replaces the "empty list + for loop + append" pattern, and PHP's `array_filter` / `array_map` / `array_column`.

**How to read it:** `[ what_to_keep   for item in collection   if condition ]`
→ "give me *what_to_keep*, for each *item* in *collection*, if *condition*."

**Loop → comprehension:**

```python
orders = [
    {"id": "A1", "customer": "acme",   "total": 250},
    {"id": "A2", "customer": "acme",   "total": 80},
    {"id": "A3", "customer": "globex", "total": 140},
]

# PHP habit: append loop
big = []
for o in orders:
    if o["total"] > 100:
        big.append(o)

# Python: list comprehension (filter)       ~ array_filter
big = [o for o in orders if o["total"] > 100]
# [{'id': 'A1', ...}, {'id': 'A3', ...}]

# filter + transform                        ~ array_map(array_filter(...))
big_ids = [o["id"] for o in orders if o["total"] > 100]
# ['A1', 'A3']

# dict comprehension                        ~ array_column($orders, 'total', 'id')
totals_by_id = {o["id"]: o["total"] for o in orders}
# {'A1': 250, 'A2': 80, 'A3': 140}

# set comprehension (unique values)         ~ array_unique(array_column(...))
customers = {o["customer"] for o in orders}
# {'acme', 'globex'}   (a set has no fixed order)

# no brackets inside a function call = generator: no list is built in memory
grand_total = sum(o["total"] for o in orders)
# 470
```

**When a comprehension is the WRONG choice — use a normal `for` loop when:**

1. **You are doing actions, not building a list.** Printing, saving to a DB, sending an email, calling an API.
   ```python
   [print(o) for o in orders]    # BAD: builds a useless list of None just to loop
   for o in orders:              # GOOD
       print(o)
   ```
2. **The logic needs several steps or `if/elif/else` branches.** If you have to read it twice, it is too clever.
3. **You need `try/except` per item.** You cannot put `try` inside a comprehension.
4. **It is nested more than one level** (`[x for row in grid for x in row if ...]`). One level is fine; beyond that, a loop is clearer.
5. **The line no longer fits comfortably on screen.**

Rule of thumb: comprehension for **"turn this collection into that collection"**; loop for **"do something for each item."**

**Interview answer (under 30 seconds):** "A comprehension builds a new collection from an existing one with an optional filter, in one expression — it replaces the append-loop pattern and is the idiomatic Python for map and filter. I switch back to a plain loop when the body has side effects, needs error handling per item, has multiple branches, or would be nested more than one level, because readability matters more than saving lines."

### `with` blocks (context managers)

**The rule:** `with` guarantees that **cleanup code runs when the block ends — no matter how it ends**: normally, by `return`, or by an exception.

**Analogy:** a hotel door that locks itself behind you. You cannot forget to lock it, even if you leave running because of a fire alarm.

**PHP (by hand):**

```php
$f = fopen("data.txt", "r");
try {
    $content = fread($f, 1024);
} finally {
    fclose($f);   // you must remember to write this every time
}
```

**Python, try/finally by hand (works, but easy to forget):**

```python
f = open("data.txt")
try:
    content = f.read()
finally:
    f.close()
```

**Python with `with` (same guarantee, nothing to forget):**

```python
with open("data.txt") as f:
    content = f.read()
# f is closed here — always
```

**Proof that it closes even when the block crashes:**

```python
try:
    with open(path) as f:
        raise ValueError("boom")
except ValueError as e:
    print("caught", e, "closed?", f.closed)
# caught boom closed? True
```

**Important: `with` does NOT swallow the error.** The cleanup runs, then the exception keeps going up. You still need `try/except` if you want to handle the error.

**How it works:** any object with two methods can be used with `with`:
- `__enter__()` — runs at the start (open the file, start a transaction). Its return value becomes the `as` variable.
- `__exit__()` — runs at the end, **always** (close the file, commit or rollback). It is told whether an exception happened.

```python
class Demo:
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("exit, exc_type =", exc_type)
        return False   # False = do not swallow the exception

with Demo():
    raise RuntimeError("x")
# enter
# exit, exc_type = <class 'RuntimeError'>
# ...then the RuntimeError is still raised
```

**Where you will see it in this roadmap:**

```python
with open("doc.txt") as f: ...                 # files         (Day 1)
with httpx.Client() as client: ...             # HTTP connections closed
async with httpx.AsyncClient() as client: ...  # async version (Day 3)
with Session(engine) as session: ...           # DB session    (Day 6)
```

Closest Laravel idea: `DB::transaction(function () { ... })` — the framework commits or rolls back for you when the closure finishes or throws.

**Interview answer (under 30 seconds):** "A `with` block uses a context manager: `__enter__` runs at the start and `__exit__` is guaranteed to run at the end, even on an exception or early return. It is the same guarantee as try/finally, but the cleanup lives inside the resource instead of being repeated by every caller, so you cannot forget it. It does not swallow the exception unless `__exit__` returns True."

## Gotchas / what bit me
_Anything that cost you more than fifteen minutes. These become interview stories._

-

## Minimal snippet
_The smallest code that demonstrates the idea. Typed by you, not pasted._

```python

```

## Sources I actually used
-
