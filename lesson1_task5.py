# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
income = float(input("Enter your income: "))
costs = float(input("Enter your costs: "))
if income > costs:
    profitability = income-costs
    rent = profitability/costs
    print(f"Amazing! You earn {profitability}")
    worker = int(input("The number of employees: "))
    print(f"{profitability/worker} for one employee")
elif income == costs:
    print("You broke even!")
else:
    print("Put some muscle into your work!")
