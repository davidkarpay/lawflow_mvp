# 🧠 Copilot Debugging Guide: Lawflow

This guide helps you debug Lawflow modules using VSCode Copilot and log traces.

## 🔍 How to Debug a Failing Test

1. Open `logs/<module>.log` to inspect runtime output.
2. In Copilot Chat, paste the test case or error message and ask:

   ```
   Why is this test failing?

   Here's the log:
   [Paste log snippet]
   ```

3. To step through logic:
   ```
   Rewrite `run()` from `services/intake/main.py` to process a dictionary input.
   ```

4. Use `print()` for fast feedback, or write to `logs/<module>.log`.

---

## ✅ Debugging Examples

### Example: Test Failure

Test:
```python
def test_run():
    assert run() == "Success"
```

Log Output:
```
2025-06-20 12:30:45 - INFO - Running intake module logic
```

Ask Copilot:
> Why is `run()` returning None? Should I return a status string instead?

---

## 🛠️ Suggest Enhancements

Prompt Copilot:
```
Add a try/except block around the main logic in `run()` and log exceptions to file.
```

