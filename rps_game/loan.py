# loan calculator


money_owed = float(input("Loan ammout $"))
apr = float(input("Loan percentage rate %"))
payment = float(input("Monthy payment $"))
#months = int(input("Number of payments #"))
monthly_rate = apr/100/12
months_paid = 0
print('Month    int     balance')
while money_owed >= 0:
    months_paid = months_paid + 1
    intrest_paid =  money_owed*monthly_rate
    money_owed += intrest_paid
    money_owed -= payment
    print(f"{months_paid}     {intrest_paid:.2f}      {money_owed:.2f} ")
