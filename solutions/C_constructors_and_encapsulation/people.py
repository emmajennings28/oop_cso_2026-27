class Person:
    def __init__(self, first_name, last_name, age, is_left):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.is_left = is_left


class Employee:
    def __init__(self, id_num, first="Ken", last="Loggins", salary=10000, title="Choreography Intern"):
        self.first = first
        self.last = last
        self.id_num = id_num
        self._salary = salary
        self.title = title

    def get_salary(self):
        return self._salary

    def display(self):
        print(f"Employee[id: {self.id_num}, first name: {self.first}, last name: {self.last}, salary: €{self._salary}]")

    def calc_net_pay(self):
        yearly_tax = self._salary * 0.42
        take_home = self._salary - yearly_tax
        monthly = take_home / 12
        return monthly

    def calc_bonus(self):
        title = self.title.lower()
        if "manager" in title:
            bonus_rate = 0.15
        elif "intern" in title:
            bonus_rate = 0.02
        else:
            bonus_rate = 0.06

        bonus = self._salary * bonus_rate
        return bonus


if __name__ == "__main__":
    specific_emp = Employee(1, "Andrew", "Jackson", 8700, "Manager of United States")
    default_emp = Employee(2)
    partial_emp = Employee(3, "Holly", title="Staff")

    # Check values are being set correctly
    specific_emp.display()
    default_emp.display()
    partial_emp.display()

    # Check take home calculation works correctly
    specific_take_home = specific_emp.calc_net_pay()
    print(f"Take home for {specific_emp.first} {specific_emp.last}: €{specific_take_home}")

    default_take_home = default_emp.calc_net_pay()
    print(f"Take home for {default_emp.first} {default_emp.last}: €{default_take_home}")

    partial_take_home = partial_emp.calc_net_pay()
    print(f"Take home for {partial_emp.first} {partial_emp.last}: €{partial_take_home}")

    # Check bonus calculation works correctly for all 3 branches
    specific_bonus = specific_emp.calc_bonus()
    print(f"Bonus for {specific_emp.first} {specific_emp.last}: €{specific_bonus}")

    default_bonus = default_emp.calc_bonus()
    print(f"Bonus for {default_emp.first} {default_emp.last}: €{default_bonus}")

    partial_bonus = partial_emp.calc_bonus()
    print(f"Bonus for {partial_emp.first} {partial_emp.last}: €{partial_bonus}")