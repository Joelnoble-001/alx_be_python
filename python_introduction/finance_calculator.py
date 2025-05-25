# finance calculator

# define variables

monthly_income = float(input("Enter your monthly income: ")) 
monthly_expenses = float(input("Enter your total monthly expenses: "))

# calculate monthly savings
monthly_savings = monthly_income - monthly_expenses 

print(f"Your monthly savings are: ${monthly_savings}")

# calculate projected annual savings after one year, incorporating the interest of 5%
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)  #adding 5% interest on the total annual savings

print(f"Projected annual savings after one year, with interest, will be: ${projected_savings}")