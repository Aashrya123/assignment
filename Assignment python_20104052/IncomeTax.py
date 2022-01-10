#Compute a person's income tax- 

gross_inc = float(input("Enter gross income "))
dependents = int(input("Enter the number of dependents "))
dep_deduction = 3000
std_deduction = 10000
tax_rate = (20/100)

taxable_inc = gross_inc - std_deduction-(dep_deduction*dependents)
tax = taxable_inc*tax_rate
print("The tax is ", tax)

