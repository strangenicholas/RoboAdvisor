import pandas as pd
import time
import numpy_financial as np



# PART 1:
# Pull in the data
pulling_data = pd.read_html("https://www.ssa.gov/oact/STATS/table4c6.html")
df = pulling_data[0]
df.drop([120], inplace=True)

#print all columns of the dataframe
#print(df.columns.tolist())

# Convert columns from objects to numbers
df['Exact age'] = df['Exact  age'].astype(int)
df['Male'] = df['Male'].astype(float)
df['Female'] = df['Female'].astype(float)

df_male = df['Male', 'Life  expectancy']
df_female = df['Female', 'Life  expectancy']

male_life_expectancy = df_male.to_dict()
female_life_expectancy = df_female.to_dict()

# Add Exception Handling?

# Part 2:
# Calculations

# Determines total life expectancy using inputs and table 
# The table is from https://www.ssa.gov/oact/STATS/table4c6.html
def life_expectancy(sex, age):
    if sex == "M":
        return male_life_expectancy[age] + age
    if sex == "F":
        return female_life_expectancy[age] + age


# Using Schwab Estimates: #NEED TO AUTOMATE
# https://www.schwab.wallst.com/Prospect/Research/mutualfunds/overview/solutions.asp?type=targetFunds

# Determines stock allocation based on the number of years until retirement
def stock_allocation(years_to_retirement):
    if years_to_retirement >= 34:
        return 100
    if 34 > years_to_retirement >= 30:
        return 91
    if 30 > years_to_retirement >= 25:
        return 84
    if 25 > years_to_retirement >= 20:
        return 78
    if 20 > years_to_retirement >= 15:
        return 71
    if 15 > years_to_retirement >= 10:
        return 64
    if 10 > years_to_retirement >= 5:
        return 51
    if 5 > years_to_retirement >= 0:
        return 43
    if 0 > years_to_retirement >= -5:
        return 38
    if -5 > years_to_retirement >= -10:
        return 35
    if -10 > years_to_retirement >= -15:
        return 30
    if -15 > years_to_retirement >= -20:
        return 26
    if years_to_retirement < -25:
        return 25


# Determines bond allocation based on the number of years until retirement
def bond_allocation(years_to_retirement):
    if years_to_retirement >= 34:
        return 0
    if 34 > years_to_retirement >= 30:
        return 8
    if 30 > years_to_retirement >= 25:
        return 15
    if 25 > years_to_retirement >= 20:
        return 21
    if 20 > years_to_retirement >= 15:
        return 27
    if 15 > years_to_retirement >= 10:
        return 32
    if 10 > years_to_retirement >= 5:
        return 44
    if 5 > years_to_retirement >= 0:
        return 52
    if 0 > years_to_retirement >= -5:
        return 57
    if -5 > years_to_retirement >= -10:
        return 60
    if -10 > years_to_retirement >= -15:
        return 65
    if -15 > years_to_retirement >= -20:
        return 69
    if years_to_retirement < -20:
        return 70


# Determines cash allocation based on the number of years until retirement
def cash_allocation(years_to_retirement):
    if years_to_retirement >= 34:
        return 0
    if 34 > years_to_retirement >= 30:
        return 1
    if 30 > years_to_retirement >= 25:
        return 1
    if 25 > years_to_retirement >= 20:
        return 1
    if 20 > years_to_retirement >= 15:
        return 2
    if 15 > years_to_retirement >= 10:
        return 4
    if 10 > years_to_retirement >= 5:
        return 5
    if 5 > years_to_retirement >= 0:
        return 5
    if years_to_retirement < 0:
        return 5


# PART 3:
# Driver code

# Introduction
print("Hello and welcome to Automated Financial Advisor")
# Delay for personal touch
time.sleep(1)
print("To get started, we're going to need some personal information.")

# Retrieves first name
first_name = input("Please enter your first name: ")

# Retrieves last name
last_name = input("Please enter your last name: ")

# Retrieves age
self_age = int(input("How old are you (rounded to the nearest whole year): "))

# Retrieves sex
self_sex = input("""What is your sex (enter "m" for male or "f" for female): """)

# Retrieves retirement age
self_retirement_age = int(input("Please enter your desired retirement age: "))

# Retrieves income
current_income = int(input('Please enter your current gross income (rounded to the nearest USD): '))

# Retrieves number of children
children = input('Do you currently have children? (y/n): ')

# Retrieves target savings goal
retirement_goal = int(input('Please enter your retirement savings goal rounded to the nearest USD: '))

# Retrieves current retirement savings
current_savings =int(input('Please enter your current retirement savings amount rounded to the nearest USD: '))

# Retrieves house status
housing = input('Do you currently own a home? (y,n):')
if housing == 'y':
    mortgage_rate = input('What is your current interest rate?')

# If has 401k, Retrieves 401k % match
company_401k = input('Does your company offer a 401k? (y,n):')
if company_401k == 'y':
    company_match =int(float(input('How much does the company match (ex: 0.05)?')))

# Roth vs Traditional 
roth_vs_traditional = input('Do you expect to pay more in taxes during retirement than you currently are? (y,n):')


# Part 4: Financial Calculations

# Investment Assumptions
investment_percentage = .15
stock_roi = .07
bond_roi = .05

# Annual Investment
annual_investment = current_income * investment_percentage

# Determines how many years until retirement
yrs_to_retirement = self_retirement_age - self_age

# Calculate expected roi
expected_roi = ((stock_allocation(yrs_to_retirement) * stock_roi) + (bond_allocation(yrs_to_retirement) * bond_roi))/100

# Calculate current FV portfolio
FV_Current = np.fv(expected_roi/12 , yrs_to_retirement*12, -annual_investment/12, -current_savings)

# Part 5:
# results

# Shows results to user
print("One moment while we calculate your optimal asset allocation.")
# Gives program a more human feel
time.sleep(3)
print("Hi", first_name, last_name)
print("Based on your life expectancy of", life_expectancy(self_sex, self_age), "years")
print("We suggest you invest", stock_allocation(yrs_to_retirement), "% in stocks,", bond_allocation(yrs_to_retirement),
      "% in bonds, and", cash_allocation(yrs_to_retirement), "% in cash. We calculate the ROI of this portfolio to be around",round(expected_roi*100,2) ,"%.")
print("Based on your total income of $", current_income,"and investment percentage of", investment_percentage,
      "%, you will be investing $", annual_investment," annually")
print("Wow! We calculate your portfolio balance at retirement to be $",FV_Current)
# at this pace and an average roi of %, we calculate your expected savings at # years old to be $
if FV_Current > retirement_goal:
    print("Congratulations! Based on our assumptions, you are projected to have",FV_Current-retirement_goal,"more than your original retirement goal at age", self_retirement_age)
if FV_Current < retirement_goal:
    print("Unfortunately at this rate, you will be",retirement_goal-FV_Current,"under your retirement goal at age", self_retirement_age)
else:
    print("You're right on track!")

# Product Suggestions

print("Based on your input, we would like to suggest some products to you.")
# if have kid, offer 529
if children == 'y':
    print('We suggest that you start contributing to a 529 plan for your children if you havent done so already')
# if interest rate higher than today, refinance
# if company match greater than 0, match up to match %
if company_401k == 'y' and company_match > 0:
    print('We suggest you contribute at least ', company_match, 'of your salary annually to your 401k to take advatntage of your company match. ')
else:
    pass
# if roth_vs_traditional == 'y' , then roth 401k/ira
if roth_vs_traditional == 'y':
    print('Based on your future tax assumptions, we suggest you take advantage of the ROTH 401k/IRA options.')
if roth_vs_traditional == 'n':
    print('Based on your future tax assumptions, we suggest you stick with the Traditional 401k/IRA options.')


