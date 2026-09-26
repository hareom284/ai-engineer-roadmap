# Pydantic v2

**Plan day:** Day 2 · **Status:** `can-explain`
_Status values: `not-started` → `learning` → `can-explain`. You are done when you can answer every question below out loud, without notes, in under two minutes each._

## In my own words
_One paragraph for a senior engineer who has never used this. No jargon you cannot define._

_(My own answers from the Day 2 session, 2026-09-26.)_

A dataclass accepts a string where we defined `int`; Pydantic enforces what we defined, and it converts when it safely can (`"2"` → `2`, `"2026-01-31"` → a real `date`), raising only when conversion is impossible. `model_validate` takes data **in** (a plain dict from JSON, a request, an LLM reply) and `model_dump` sends data **out** (back to a plain dict). A field validator validates one specific field; a model validator runs after every field is valid, so it is the one for cross-field rules. `model_json_schema()` describes the **shape** of the data — which fields exist, their **types**, and which are **required** — and I will send it to an **LLM** on Day 10 so it replies with exactly that JSON.

## Must be able to answer
- [x] What does Pydantic give you that a @dataclass does not?
- [x] `model_validate` vs the constructor; `model_dump` vs `dict()`. When does each matter?
- [x] Field validator vs model validator: which one for cross-field rules?
- [x] How do you get a JSON Schema out of a model, and where will you need it later?

### Direction cheat-sheet
| Call | Direction | Use for |
|---|---|---|
| `Invoice.model_validate(data)` | dict → model | untrusted data: JSON, request body, LLM output |
| `Invoice(invoice_no=..., ...)` | kwargs → model | data I build myself in code |
| `invoice.model_dump()` | model → dict | API responses, writing to a DB |

## Gotchas / what bit me
_Anything that cost you more than fifteen minutes. These become interview stories._

- **Indentation decides whether a validator exists at all.** I wrote `@field_validator("qty")` at column 0, below the class instead of inside it. No error, no warning — Pydantic simply never saw it, and `qty=0` validated happily. In PHP the `{ }` would have made the mistake obvious. Lesson: after adding a validator, always prove it fires by feeding it bad data.
- Ran `python file.py` instead of `uv run python file.py` and got `ModuleNotFoundError: No module named 'pydantic'`. The system Python is not the project `.venv`. Same thing happens with the editor's ▶ button unless the interpreter is set to `./.venv`.
- Wrote `from tests.test_invoice import Invoice` inside the model file — backwards. The tests import the models, never the reverse.
- Empty tests pass. Five tests with only `# TODO` comments reported "5 passed". A test with no assertion proves nothing; break one on purpose to check it can fail.

## Minimal snippet
_The smallest code that demonstrates the idea. Typed by you, not pasted._

From `docuquery/scratch/07_invoice_validators.py` — one field rule, one cross-field rule:

```python
class LineItem(BaseModel):
    desc: str
    qty: int
    unit_price: Decimal

    @field_validator("qty")          # sees ONE field
    @classmethod
    def qty_must_be_positive(cls, v):
        if v < 1:
            raise ValueError("Quantity must be positive")
        return v                     # a field validator returns the value


class Invoice(BaseModel):
    invoice_no: str
    issued_on: date
    line_items: list[LineItem]
    total: Decimal

    @model_validator(mode="after")   # sees the WHOLE object
    def total_must_match(self):
        calculated_total = sum(item.qty * item.unit_price for item in self.line_items)
        if self.total != calculated_total:
            raise ValueError(f"Total {self.total} does not match calculated total {calculated_total}")
        return self                  # a model validator returns self
```

Proof both rules fire:

```
qty=0        -> Value error, Quantity must be positive
wrong total  -> Value error, Total 999.00 does not match calculated total 1300.00
```

## Sources I actually used
- Pydantic v2 docs: `BaseModel`, `field_validator`, `model_validator`
- `docuquery/scratch/06_invoice_model.py`, `07_invoice_validators.py`, `tests/test_invoice.py`
