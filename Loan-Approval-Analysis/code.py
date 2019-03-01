# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)

numerical_var = bank.select_dtypes(include='number')
print(numerical_var)



# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'], axis=1)
#print(banks.head(5))

banks.isnull().sum()

bank_mode = banks.mode()
print("Mode : ", bank_mode)

banks = banks.fillna(banks.mode().iloc[0])

banks.isnull().sum()
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks, index=['Gender','Married','Self_Employed'],
values='LoanAmount')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here







loan_approved_se = len(banks[(banks['Loan_Status']=='Y') & (banks['Self_Employed']=='Yes')])

loan_approved_nse = len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])

print(loan_approved_se)
print(loan_approved_nse)


Loan_Status = len(banks)
print(Loan_Status)

percentage_se = ((loan_approved_se)/Loan_Status)*100

percentage_nse = ((loan_approved_nse)/Loan_Status)*100

print(percentage_se)
print(percentage_nse)

# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x : (x/12))
#print(loan_term)

loan_term_temp = list(loan_term)
big_loan_term = len([num for num in loan_term_temp if num >=25])
print(big_loan_term)

# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
#print(loan_groupby.groups)
mean_values = loan_groupby.mean()
print(mean_values)



# code ends here


