while True: 
    hours_worked = float(input("Enter hours worked"))
    hourly_rate = float(input("Enter hourly rate"))
    if (hours_worked > 40):
        regular_hours = 40
        overtime_hours = (hours_worked - 40)
        regular_pay = (regular_hours * hourly_rate)
        overtime_pay = (overtime_hours * (hourly_rate * 1.5))
        gross_pay = (regular_pay + overtime_pay)
        print (gross_pay)
    else:
        gross_pay = (hours_worked * hourly_rate)
        print (gross_pay)
else:
    stop

    
