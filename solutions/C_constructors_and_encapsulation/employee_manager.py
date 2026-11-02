from people import Employee

def find_lowest_net_pay(employees_list):
    # If there are no Employees, return None
    if not employees_list:
        return None

    # No clean initial value, so use data from first employee in list
    lowest = employees_list[0]
    min_net = lowest.calc_net_pay()

    # Loop through all employees
    for emp in employees_list:
        # Calculate current net pay
        emp_net_pay = emp.calc_net_pay()
        # Compare to current min, store this one if it's smaller
        if emp_net_pay < min_net:
            min_net = emp_net_pay
            lowest = emp

    return lowest

def find_highest_bonus(employees_list):
    # Very clean initial value (-1 is not a valid bonus value, so safe to be used)
    # so no need to use value from list (or check if list contains data before starting)
    highest = None
    max_bonus = -1

    # For each employee in the list
    for emp in employees_list:
        # Calculate current employee's bonus - if it's higher than current max, save it
        emp_bonus = emp.calc_bonus()
        if emp_bonus > max_bonus:
            max_bonus = emp_bonus
            highest = emp

    return highest


if __name__ == "__main__":
    # Store employees in a dictionary to make ID searching fast and efficient
    employees = {}

    # Track how many employees have been made
    count = 0

    # While we have not made 5 yet, keep going
    while count < 2:
        # Ask for id
        new_id = input("Please enter new Employee's ID:")
        # Check if it's already present/used, try again
        if new_id in employees:
            print("ID already in use. Please select a new one.")
            # Continue skips on to next iteration of loop,
            # it will ignore all the rest of the code for this one
            continue

        # If we make it here, the id is valid - take in remainder of data
        first = input("Employee first name: ")
        last = input("Employee last name: ")
        salary = float(input("Employee salary: "))
        title = input("Employee title: ")

        # Create Employee from the data and add it to the dictionary
        new_emp = Employee(new_id, first, last, salary, title)
        employees[new_id] = new_emp

        # Increase count of Employees created
        count+=1


    # Find Employee with the lowest net pay
    lowest_paid = find_lowest_net_pay(list(employees.values()))
    # If there was a lowest paid Employee found, display it.
    # Otherwise don't, as you can't call a method on a None
    if lowest_paid:
        print("Lowest paid employee:")
        lowest_paid.display()

    # Find Employee with highest bonus pay
    max_bonus_emp = find_highest_bonus(list(employees.values()))
    # If there was an Employee with the highest bonus found, display it.
    # Otherwise don't, as you can't call a method on a None
    if max_bonus_emp:
        print("Employee receiving highest bonus: ")
        max_bonus_emp.display()
