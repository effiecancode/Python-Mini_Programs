is_stop = False

while is_stop == False:

    hours_worked = int(input("number of hours worked: "))
    hour_rate = int(input("Rate per hour: "))


    nhif = int(input("nhif amount: "))
    Tax = int(input("Tax payable: "))

    deductables = nhif + Tax

    basic_salary = hours_worked * hour_rate
    print(f"Your basic_salary is: {basic_salary}")

    Gross = basic_salary - deductables
    print(f"Your Gross salary is: {Gross}")

    q = input("Would you like to calculate another payroll? yes or no: ")

    if q == "no":
        is_stop = True
