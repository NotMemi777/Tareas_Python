#7.5 Problem 5: Loan eligibility (income and debt ratio)

montly_incomme = float (input("Type your montly inclome: "))
montly_debt = float (input("Type your montly debt payments: "))
credit_score = int (input("Type your credit score: "))

if montly_incomme > 0 and montly_debt >= 0 and credit_score >=0:
    debt_ratio = montly_debt/montly_incomme
    eligible =  (montly_incomme >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)
    print(f"Debt ratio: {debt_ratio}")
    print (f"Eligible: {eligible}")
else:
    print ("Error: invalid input")


