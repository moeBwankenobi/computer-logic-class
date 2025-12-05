while True: 
    gross_pay = float(input("enter gross pay"))
    state_tax = (gross_pay * 0.056)
    federal_tax = (gross_pay * 0.079)
    Total_deductions = (state_tax + federal_tax)
    net_pay = (gross_pay - Total_deductions)
    print ("net pay" , net_pay)
    print ("State Tax", state_tax)
    print ("Federal Tax", federal_tax)
    print ("Total Deductions", Total_deductions)
else:
    stop
