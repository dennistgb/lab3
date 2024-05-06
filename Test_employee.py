import employee_info as info

def test_age():
    test = info.get_employees_by_age_range(20,30)
    result =[{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000}, {'name': 'Mary', 'age': 23, 'department': 'Marketing', 'salary': 56000}]
    assert(result == test)

def test_salary():
    test = info.calculate_average_salary()
    assert(test == 60166.67)

def test_employees():
    test = info.get_employees_by_dept("Engineering")
    assert(test == [{'name': 'Chloe', 'age': 35, 'department': 'Engineering', 'salary': 70000}, {'name': 'Mike', 'age': 32, 'department': 'Engineering', 'salary': 65000}])