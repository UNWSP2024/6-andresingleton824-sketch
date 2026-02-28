# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025


def calculate_tax(total_sales):
    
    state_tax = total_sales * STATE_TAX_RATE
    county_tax = total_sales * COUNTY_TAX_RATE
    total_tax = state_tax + county_tax
    return county_tax, state_tax, total_tax



total_sales = float(input("Enter total sales for the month: $"))

county_tax, state_tax, total_tax = calculate_tax(total_sales)

print(f"County Sales Tax: ${county_tax:.2f}")
print(f"State Sales Tax:  ${state_tax:.2f}")
print(f"Total Sales Tax:  ${total_tax:.2f}")