# 📘 Assignment: Testing and Debugging in Python

## 🎯 Objective

Practice finding bugs with automated tests and improving Python code with clear error handling. You will use `pytest` to test functions, fix failing behavior, and add tests for edge cases.

## 📝 Tasks

### 🛠️ Run Tests and Find the Bugs

#### Description

Run the provided test suite and read the failure messages. Use the failures to identify problems in `calculator.py` without changing the tests yet.

#### Requirements

Completed program should:

- Install `pytest` and run the tests with `pytest`
- Record which tests pass and which tests fail before making changes
- Explain in a short comment or note what each failing test reveals

Example command:

```text
pytest
```

### 🛠️ Fix Functions and Handle Invalid Input

#### Description

Correct the implementation in `calculator.py` so that it matches the behavior described by the tests. Keep the function names and parameters unchanged.

#### Requirements

Completed program should:

- Return the correct discounted price from `calculate_discount(price, percent)`
- Return the average of a non-empty list from `average(numbers)`
- Raise `ValueError` when `average()` receives an empty list
- Raise `ValueError` when `parse_age()` receives text that is not a whole-number age
- Pass all provided tests without modifying their expected behavior

### 🛠️ Add Edge-Case Tests

#### Description

Extend `test_calculator.py` with tests for inputs that are not covered by the starter tests. Use descriptive test names and make each test check one behavior.

#### Requirements

Completed program should:

- Add at least three new tests
- Cover at least one boundary value, such as a 0% or 100% discount
- Cover at least one invalid or unusual input
- Keep all original and new tests passing
