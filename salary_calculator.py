# Employee Salary Calculator
# PS No. 10 - B.Tech CSE
# Concepts: Functions, Operators, Conditions, Loops

HRA_RATE = 0.20   # 20% of basic
DA_RATE = 0.10    # 10% of basic
PF_RATE = 0.12    # 12% of basic


def get_basic_salary():
    """Keep asking until the user enters a valid positive number."""
    while True:
        value = input("Enter basic salary: ")
        try:
            salary = float(value)
            if salary > 0:
                return salary
            print("Invalid salary. Enter a positive number.")
        except ValueError:
            print("Invalid salary. Enter a positive number.")


def calculate_hra(basic):
    return basic * HRA_RATE


def calculate_da(basic):
    return basic * DA_RATE


def calculate_gross(basic, hra, da):
    return basic + hra + da


def calculate_pf(basic):
    return basic * PF_RATE


def calculate_tax(gross):
    """Tax slab is applied on gross salary."""
    if gross <= 25000:
        return 0
    elif gross <= 50000:
        return gross * 0.05
    else:
        return gross * 0.10


def calculate_net(gross, pf, tax):
    return gross - pf - tax


def print_slip(name, emp_id, basic, hra, da, gross, pf, tax, net):
    print("\n" + "=" * 40)
    print("            SALARY SLIP")
    print("=" * 40)
    print(f"Employee Name : {name}")
    print(f"Employee ID   : {emp_id}")
    print("-" * 40)
    print(f"Basic Salary  : {basic:.0f}")
    print(f"HRA (20%)     : {hra:.0f}")
    print(f"DA (10%)      : {da:.0f}")
    print(f"Gross Salary  : {gross:.0f}")
    print("-" * 40)
    print(f"PF (12%)      : {pf:.0f}")
    print(f"Tax           : {tax:.0f}")
    print("-" * 40)
    print(f"NET SALARY    : {net:.0f}")
    print("=" * 40)
    # Short summary line (matches expected output format)
    print(f"HRA: {hra:.0f} | DA: {da:.0f} | Gross: {gross:.0f}")
    print(f"PF: {pf:.0f} | Tax: {tax:.0f} | Net Salary: {net:.0f}\n")


def main():
    print("===== Employee Salary Calculator =====")
    while True:
        name = input("\nEnter employee name: ")
        emp_id = input("Enter employee ID: ")
        basic = get_basic_salary()

        hra = calculate_hra(basic)
        da = calculate_da(basic)
        gross = calculate_gross(basic, hra, da)
        pf = calculate_pf(basic)
        tax = calculate_tax(gross)
        net = calculate_net(gross, pf, tax)

        print_slip(name, emp_id, basic, hra, da, gross, pf, tax, net)

        again = input("Calculate for another employee? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you!")
            break


main()
