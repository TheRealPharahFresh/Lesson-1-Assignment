#Task 1: /// Grocery Store Math
#  Calculate the total cost of three items you'd commonly find in a grocery store, 
# given their individual prices. 
# For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic! /// push -u

bread = 4.00
peanut_butter = 2.00
jelly = 1.00
total_cost = bread + peanut_butter + jelly
print(total_cost)


#Task 2: /// Task 2: Bank Interest 
# If you have a savings account with a particular initial amount and a fixed yearly interest rate,
#  calculate the total amount in your account after a year.
#  So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. 
# For the example the expected outcome would be $10,700. ///

bank_account = 10000
interest_rate = float(0.07)
result_of_interest = bank_account * interest_rate + bank_account
amount_of_years = 1
total_amount = result_of_interest * amount_of_years
print(int(total_amount))

