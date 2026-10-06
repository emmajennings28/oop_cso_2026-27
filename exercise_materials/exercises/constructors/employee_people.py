from employee import Employee
employees = {
}
for i in range(5):
    print("Employee", i+1)

    user_id = int(input("Please enter the employee ID:"))

    while user_id in employees:
        print("ID already exists")

        user_id = int(input("Add another employee ID"))

    name = input("Please enter the employee name: ")
    gross_pay = float(input("Please enter the gross pay: "))
    tax = float(input("Please enter the tax: "))
    bonus_pay = float(input("Please enter the bonus pay: "))

    net_pay = gross_pay - tax
    employee = Employee(user_id,name,gross_pay,tax,net_pay,bonus_pay)
    employees[user_id] = employee

    lowest = None

    for employee in employees.values():
        if lowest is None or employee.net_pay < lowest.net_pay:
            lowest = employee


    highest = None

    for employee in employees.values():
        if highest is None or employee.bonus_pay > highest.bonus_pay:
            highest = employee

    print("Employee with lowest net pay:")
    lowest.display()

    print("Employee with highest bonus pay:")
    highest.display()
