
def calculate_monthly_loan_installment(loan,interest_rate,duration):
    monthly_interest_rate=(interest_rate/100)/12
    total_payment=duration*12
    monthly_loan_installment=loan*monthly_interest_rate*(1+monthly_interest_rate*total_payment)/(1+monthly_interest_rate*total_payment)
    return monthly_loan_installment

loan= 3000000
interest_rate= 4
duration=2  

monthly_loan_installment=calculate_monthly_loan_installment(loan,interest_rate,duration)
print(monthly_loan_installment)

#money expected per month
loan=3000000
interest_rate=4
duration=2
number_of_students=47

