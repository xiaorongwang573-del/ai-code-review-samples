# Code Review Notes: Moving Average

## Original Issue

The original implementation has an off-by-one bug:

```python
for i in range(len(values) - window):
```

For four values and a window of two, the valid windows are:

- `[10, 20]`
- `[20, 30]`
- `[30, 40]`

That means the loop should run three times. The original code only runs two times.

## Correct Fix

Use:

```python
range(0, len(values) - window + 1)
```

The `+ 1` includes the final valid window.

## Edge Cases Added

- `window <= 0`: raise `ValueError`
- `window > len(values)`: return an empty list
- `window == len(values)`: return one average

## Why This Matters for AI Code Evaluation

AI-generated code often looks plausible but fails boundary cases. A careful reviewer should check:

- loop bounds
- empty inputs
- invalid parameters
- output shape
- whether the behavior is documented and testable
