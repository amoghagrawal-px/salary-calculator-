# Employee Salary Calculator

**PS No. 10 – B.Tech CSE** | Python 3 | Console application | Single file, no external libraries

A command-line program that takes an employee's **name, ID and basic salary**, calculates **HRA, DA, gross salary, PF, tax and net salary**, and prints a formatted **salary slip**. After each slip it asks whether to process another employee, so many employees can be handled in one run.

**Concepts used:** Functions, Operators, Conditions (`if / elif / else`), Loops (`while`), Input validation, String methods

---

## Table of Contents
1. [Problem Statement](#1-problem-statement)
2. [Salary Rules](#2-salary-rules)
3. [Project Structure](#3-project-structure)
4. [How to Run](#4-how-to-run)
5. [How the Program Works (Flow)](#5-how-the-program-works-flow)
6. [Code Walkthrough (Function by Function)](#6-code-walkthrough-function-by-function)
7. [Input Validation in Detail](#7-input-validation-in-detail)
8. [Tax Slab Explained](#8-tax-slab-explained)
9. [Salary Slip Format](#9-salary-slip-format)
10. [Test Cases with Step-by-Step Calculations](#10-test-cases-with-step-by-step-calculations)
11. [Edge Cases and Behaviour](#11-edge-cases-and-behaviour)
12. [Requirement Checklist](#12-requirement-checklist)
13. [Limitations and Future Improvements](#13-limitations-and-future-improvements)

---

## 1. Problem Statement

Calculating salaries by hand is repetitive and easy to get wrong. The task is to write a Python 3 program (one `.py` file, run from the console) that:

1. Takes employee **name, ID and basic salary** as input.
2. Calculates **HRA, DA, PF and tax** using operators and conditions.
3. Uses **functions** such as `calculate_gross()` and `print_slip()`.
4. Prints a **neat salary slip** and allows **more employees using a loop**.

The program must also pass the four test cases given in the problem statement (normal, boundary, invalid and a different valid input).

## 2. Salary Rules

| Component | Meaning | Formula |
|-----------|---------|---------|
| **Basic** | Base pay entered by the user | Input |
| **HRA** | House Rent Allowance | 20% of basic |
| **DA** | Dearness Allowance | 10% of basic |
| **Gross Salary** | Total before deductions | Basic + HRA + DA (= 130% of basic) |
| **PF** | Provident Fund (deduction) | 12% of basic |
| **Tax** | Income tax (deduction), based on **gross** | see slab below |
| **Net Salary** | Take-home pay | Gross − PF − Tax |

**Tax slab (applied on gross salary):**

| Gross salary | Tax rate |
|--------------|----------|
| Up to 25,000 | 0% |
| 25,001 to 50,000 | 5% of gross |
| Above 50,000 | 10% of gross |

## 3. Project Structure

```
.
├── salary_calculator.py     # the complete solution (single file)
├── README.md                # this file (detailed documentation)
├── SUMMARY.md               # project summary / report
└── screenshots/
    ├── test_cases_given.png # test cases from the problem statement
    ├── test_case_1.png      # Test Case 1 – Normal input
    ├── test_case_2.png      # Test Case 2 – Boundary / minimum input
    ├── test_case_3.png      # Test Case 3 – Invalid input
    └── test_case_4.png      # Test Case 4 – Different valid scenario
```

## 4. How to Run

**Requirements:** Python 3 (no pip installs needed).

```bash
python salary_calculator.py
# or, on systems where python3 is the command:
python3 salary_calculator.py
```

**What you will see:**

1. A heading: `===== Employee Salary Calculator =====`
2. Prompts for **employee name**, **employee ID** and **basic salary**.
3. The **salary slip**.
4. `Calculate for another employee? (y/n):` – type `y` to continue, anything else to exit.
5. `Thank you!` when you exit.

## 5. How the Program Works (Flow)

```
START
  │
  ▼
Print heading, set choice = "y"
  │
  ▼
┌─────────────────────────────┐
│ while choice == "y":        │◄──────────────────────┐
│   read name                 │                       │
│   read employee ID          │                       │
│   get_basic_salary()        │ (loops until valid)   │
│   hra   = calculate_hra     │                       │
│   da    = calculate_da      │                       │
│   gross = calculate_gross   │                       │
│   pf    = calculate_pf      │                       │
│   tax   = calculate_tax     │                       │
│   net   = calculate_net     │                       │
│   print_slip(...)           │                       │
│   ask "another? (y/n)" ─────┼── "y" ────────────────┘
└─────────────────────────────┘
  │ anything else
  ▼
Print "Thank you!"  →  END
```

The order of calculation matters: **gross** needs HRA and DA, **tax** needs gross, and **net** needs gross, PF and tax. `main()` therefore calculates them in exactly this order.

## 6. Code Walkthrough (Function by Function)

### `get_basic_salary()`
Asks for the basic salary repeatedly until the user enters a valid **positive number**, then returns it as a `float`.

```python
def get_basic_salary():
    while True:
        value = input("Enter basic salary: ")
        if value.replace(".", "", 1).isdigit():
            salary = float(value)
            if salary > 0:
                return salary
            else:
                print("Invalid salary. Enter a positive number.")
        else:
            print("Invalid salary. Enter a positive number.")
```

- `while True` creates an endless loop that only ends when `return` is reached (valid input).
- `value.replace(".", "", 1)` removes **one** decimal point so values like `25000.50` are accepted.
- `.isdigit()` then checks that what remains is only digits. This is what rejects `-5000` (the minus sign is not a digit) and `abc`.
- `float(value)` converts the checked text to a number.
- `salary > 0` rejects zero (e.g. `0` or `0.0`) even though it is made of digits.
- Both failure paths print the same message: `Invalid salary. Enter a positive number.`

### `calculate_hra(basic)`
```python
return basic * 20 / 100
```
Returns 20% of basic salary.

### `calculate_da(basic)`
```python
return basic * 10 / 100
```
Returns 10% of basic salary.

### `calculate_gross(basic, hra, da)`
```python
return basic + hra + da
```
Gross salary is basic plus both allowances.

### `calculate_pf(basic)`
```python
return basic * 12 / 100
```
Provident Fund is 12% of **basic** (not gross).

### `calculate_tax(gross)`
```python
if gross <= 25000:
    tax = 0
elif gross <= 50000:
    tax = gross * 5 / 100
else:
    tax = gross * 10 / 100
return tax
```
Uses `if / elif / else` to pick the slab. Because the conditions are checked top to bottom, the `elif` only runs when gross is already above 25,000, so it does not need a lower bound.

### `calculate_net(gross, pf, tax)`
```python
return gross - pf - tax
```
Take-home salary after both deductions.

### `print_slip(name, emp_id, basic, hra, da, gross, pf, tax, net)`
Prints the formatted slip. Values are converted with `int()` so amounts show as whole numbers (matching the expected outputs). It prints the detailed slip first, then a compact two-line summary:

```
HRA: 6000 | DA: 3000 | Gross: 39000
PF: 3600 | Tax: 1950 | Net Salary: 33450
```
This summary format is exactly the format used in the problem statement's expected outputs.

### `main()`
Controls the whole program: prints the heading, then runs a `while choice == "y"` loop. In each pass it reads the name and ID, gets a validated salary, runs all calculations, prints the slip, and asks whether to continue. The answer is converted with `.lower()` so both `y` and `Y` work.

## 7. Input Validation in Detail

| User types | Result | Why |
|------------|--------|-----|
| `30000` | Accepted | Digits only, greater than 0 |
| `25000.50` | Accepted | One decimal point is allowed |
| `-5000` | Rejected | `-` is not a digit |
| `abc` | Rejected | Letters are not digits |
| `0` or `0.0` | Rejected | Digits, but not greater than 0 |
| *(empty, just Enter)* | Rejected | Empty text is not digits |
| `1.2.3` | Rejected | More than one decimal point |
| `10,000` | Rejected | Comma is not a digit |

When input is rejected the program prints `Invalid salary. Enter a positive number.` and asks again. It never crashes on bad input.

## 8. Tax Slab Explained

Tax is a **flat rate on the whole gross amount** according to the slab the gross falls in; it is **not** progressive (it is not calculated slab-by-slab on portions of income).

| Basic salary | Gross (130% of basic) | Slab | Tax |
|--------------|----------------------|------|-----|
| 10,000 | 13,000 | ≤ 25,000 | 0 |
| 30,000 | 39,000 | 25,001 – 50,000 | 5% = 1,950 |
| 50,000 | 65,000 | > 50,000 | 10% = 6,500 |

Since gross = 1.3 × basic, the slab limits correspond to these basic salaries: no tax up to about **19,230** basic; 5% up to about **38,461** basic; 10% above that.

## 9. Salary Slip Format

```
========================================
            SALARY SLIP
========================================
Employee Name : Amogh Agrawal
Employee ID   : E101
----------------------------------------
Basic Salary  : 30000
HRA (20%)     : 6000
DA (10%)      : 3000
Gross Salary  : 39000
----------------------------------------
PF (12%)      : 3600
Tax           : 1950
----------------------------------------
NET SALARY    : 33450
========================================
HRA: 6000 | DA: 3000 | Gross: 39000
PF: 3600 | Tax: 1950 | Net Salary: 33450
```

The slip is organised into three blocks: employee details, **earnings** (basic, HRA, DA, gross), and **deductions** (PF, tax) leading to the final **net salary**.

## 10. Test Cases with Step-by-Step Calculations

The test cases given in the problem statement:

![Given test cases](screenshots/test_cases_given.png)

All four were executed and the output matches the expected output exactly.

| # | Scenario | Input | Expected | Result |
|---|----------|-------|----------|--------|
| 1 | Normal input | 30000 | HRA 6000, DA 3000, Gross 39000, PF 3600, Tax 1950, Net 33450 | **Pass** |
| 2 | Boundary / minimum (no tax slab) | 10000 | HRA 2000, DA 1000, Gross 13000, PF 1200, Tax 0, Net 11800 | **Pass** |
| 3 | Invalid input | -5000, then abc | `Invalid salary. Enter a positive number.` | **Pass** |
| 4 | Different valid scenario | 50000 | HRA 10000, DA 5000, Gross 65000, PF 6000, Tax 6500, Net 52500 | **Pass** |

### Test Case 1 – Normal Input (basic = 30000)

| Step | Calculation | Result |
|------|-------------|--------|
| HRA | 30000 × 20 / 100 | 6000 |
| DA | 30000 × 10 / 100 | 3000 |
| Gross | 30000 + 6000 + 3000 | 39000 |
| PF | 30000 × 12 / 100 | 3600 |
| Tax | 39000 is above 25000 and not above 50000, so 5%: 39000 × 5 / 100 | 1950 |
| Net | 39000 − 3600 − 1950 | **33450** |

![Test Case 1](screenshots/test_case_1.png)

### Test Case 2 – Boundary / Minimum Input (basic = 10000)

| Step | Calculation | Result |
|------|-------------|--------|
| HRA | 10000 × 20 / 100 | 2000 |
| DA | 10000 × 10 / 100 | 1000 |
| Gross | 10000 + 2000 + 1000 | 13000 |
| PF | 10000 × 12 / 100 | 1200 |
| Tax | 13000 ≤ 25000, so no tax | 0 |
| Net | 13000 − 1200 − 0 | **11800** |

This case checks the lowest slab: the `if gross <= 25000` branch gives zero tax.

![Test Case 2](screenshots/test_case_2.png)

### Test Case 3 – Invalid Input (-5000, then abc)

Trace of `get_basic_salary()`:

| Attempt | Input | Check | Outcome |
|---------|-------|-------|---------|
| 1 | `-5000` | `"-5000".isdigit()` is False (minus sign) | Prints `Invalid salary. Enter a positive number.` and asks again |
| 2 | `abc` | `"abc".isdigit()` is False (letters) | Prints the same message and asks again |
| 3 | `30000` | Digits, and greater than 0 | Accepted, slip is generated |

The program does not crash and keeps asking until it gets a valid value. (In the screenshot a valid value, 30000, is entered at the end so the program can finish normally.)

![Test Case 3](screenshots/test_case_3.png)

### Test Case 4 – Different Valid Scenario (basic = 50000)

| Step | Calculation | Result |
|------|-------------|--------|
| HRA | 50000 × 20 / 100 | 10000 |
| DA | 50000 × 10 / 100 | 5000 |
| Gross | 50000 + 10000 + 5000 | 65000 |
| PF | 50000 × 12 / 100 | 6000 |
| Tax | 65000 is above 50000, so 10%: 65000 × 10 / 100 | 6500 |
| Net | 65000 − 6000 − 6500 | **52500** |

This case exercises the highest slab (the `else` branch).

![Test Case 4](screenshots/test_case_4.png)

**Branch coverage:** the valid test cases together cover all three tax branches (`if`, `elif`, `else`), and Test Case 3 covers both validation failure paths.

## 11. Edge Cases and Behaviour

- **Multiple employees:** typing `y` at the final prompt starts a fresh loop pass for the next employee. Each employee is calculated independently.
- **Exit:** any answer other than `y`/`Y` (including `n` or just pressing Enter) ends the program with `Thank you!`.
- **Whole-number display:** `int()` truncates (does not round) decimals on the slip. For example a basic of `12345` gives HRA 2469.0 shown as `2469`.
- **Decimal salaries:** values like `25000.50` are accepted and calculated using floating-point arithmetic.
- **Name and ID:** accepted as any text; they are not validated.
- **Tax boundary:** a gross of exactly 25000 or 50000 falls in the **lower** slab because the conditions use `<=`.
- **Tax jump:** because tax is flat on the whole gross, crossing a boundary makes tax jump (e.g. gross 25000 → tax 0, gross 25001 → tax about 1250).

## 12. Requirement Checklist

| Requirement | Status | Where |
|-------------|--------|-------|
| Python 3, one `.py` file, run from console | Done | `salary_calculator.py` |
| Take employee name, ID and basic salary as input | Done | `main()`, `get_basic_salary()` |
| Calculate HRA, DA, PF, tax using operators and conditions | Done | `calculate_*` functions, `calculate_tax()` uses `if/elif/else` |
| Functions such as `calculate_gross()` and `print_slip()` | Done | 8 helper functions plus `main()` |
| Neat salary slip | Done | `print_slip()` |
| Loop to allow more employees | Done | `while choice == "y"` in `main()` |
| Pass the 4 given test cases | Done | Section 10 |
| Documentation/report for GitHub | Done | `README.md`, `SUMMARY.md` |

## 13. Limitations and Future Improvements

**Current limitations**
- Tax is a flat slab rate, not progressive.
- Slip amounts are truncated to whole numbers.
- Employee name and ID are not validated (can be empty).
- Results are only printed, not saved.
- Whitespace around a number (e.g. `" 5000"`) is rejected.

**Possible improvements**
- Validate that name and ID are not empty.
- Strip spaces from input and show amounts with two decimals.
- Save each salary slip to a text or CSV file.
- Add a total/summary report for all employees in a session.
- Add a separate unit-test file for the calculation functions.

---

## Author

Amogh Agrawal – B.Tech CSE
