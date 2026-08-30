# Contributing

Contributions are welcome while the project is under private development and after publication.

## Before submitting a change

1. Keep examples fictional and generic.
2. Put cross-platform behavior in `kernel/`; put provider-specific instructions in `adapters/`.
3. Update `schema/sheets.json` before changing Sheet columns.
4. Do not add another source of truth.
5. Run:

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

## Design standard

Prefer a small interface with substantial behavior behind it. New modules should reuse the core record types and review loop rather than creating parallel task systems.
