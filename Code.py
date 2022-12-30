import pandas as pd
import time

# PART 1:
# Pull in the data
pulling_data = pd.read_html("https://www.ssa.gov/oact/STATS/table4c6.html")
df = pulling_data[0]
df.drop([120], inplace=True)

# print all columns of the dataframe
#print(df.columns.tolist())

# Convert columns from objects to numbers
df['Exact age'] = df['Exact  age'].astype(int)
df['Male'] = df['Male'].astype(float)
df['Female'] = df['Female'].astype(float)

df_male = df['Male', 'Life  expectancy']
df_female = df['Female', 'Life  expectancy']

male_life_expectancy = df_male.to_dict()
female_life_expectancy = df_female.to_dict()


# Part 2:
# Exception handling

# Exception check first name
def get_first_name(name):
    # Checks for non-whitespace characters in the original input
    if name.isspace() is False:

        # Makes sure the name us an allowable character limit
        while len(name) > 20:
            name = input("You have reached the character limit. \nPlease enter your first name: ")

        # Makes sure the name is entered
        while len(name) == 0:
            name = input("Please enter your first name: ")

        # Outlines all forbidden characters
        forbidden_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '!', '@', '#', '$', '%',
                                '^', '&', '*', '(', ')', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':',
                                '"', ',', '<', '.', '>', '/', '?', '-', "'"]

        # Checks each element of the name against the forbidden characters
        for character in name:
            if character in forbidden_characters:
                name = input(
                    "Please refrain from entering numbers or special characters.\nPlease enter your first name: ")
                return get_first_name(name)

        # Checks for whitespace with the new inputs
        if name.isspace() is True:
            name = input("Please enter your first name: ")
            return get_first_name(name)

    # Corrects for whitespace in the original inputs
    else:
        name = input("Please enter your first name: ")
        return get_first_name(name)

    # Standardizes the return
    return name.upper().replace(" ", "")


# Exception check last name
def get_last_name(name):
    # Checks for non-whitespace characters in the original input
    if name.isspace() is False:

        # Makes sure the name us an allowable character limit
        while len(name) > 20:
            name = input("You have reached the character limit. \nPlease enter your last name: ")

        # Makes sure the name is entered
        while len(name) == 0:
            name = input("Please enter your last name: ")

        # Outlines all forbidden characters
        forbidden_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '!', '@', '#', '$', '%',
                                '^', '&', '*', '(', ')', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':',
                                '"', ',', '<', '.', '>', '/', '?', '-', "'"]

        # Checks each element of the name against the forbidden characters
        for character in name:
            if character in forbidden_characters:
                name = input(
                    "Please refrain from entering numbers or special characters.\nPlease enter your last name: ")
                return get_last_name(name)

        # Checks for whitespace with the new inputs
        if name.isspace() is True:
            name = input("Please enter your last name: ")
            return get_last_name(name)

    # Corrects for whitespace in the original inputs
    else:
        name = input("Please enter your last name: ")
        return get_last_name(name)

    # Standardizes the return
    return name.upper().replace(" ", "")


# Exception check age
def get_age(age):
    # Checks for non-whitespace characters in the original input
    if age.isspace() is False:

        # Makes sure the age is entered
        while len(age) == 0:
            age = input("Please enter your age: ")
            return get_age(age)

        # Outlines all forbidden characters
        forbidden_characters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
                                'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
                                'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
                                'Y', 'y', 'Z', 'z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                                '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', '"', ',', '<', '.', '>', '/',
                                '?', '-', "'", " "]

        # Checks each element of the age against the forbidden characters
        for number in age:
            if number in forbidden_characters:
                age = input("Please refrain from entering letters, special characters, "
                            "or spaces.\nPlease enter your age: ")
                return get_age(age)

        # Sets parameters on the age
        if int(age) > 119:
            age = input(
                "You're blessed to live a long life! There's no need to continue. \nIf you would like to continue, "
                "please enter an age less than or equal to 119: ")
            return get_age(age)

        # Checks for whitespace with the new inputs
        if age.isspace() is True:
            age = input("Please enter your age: ")
            return get_age(age)

    # Corrects for whitespace in the original inputs
    else:
        age = input("Please enter your age: ")
        return get_age(age)

    # Standardizes the return
    return age.replace(" ", "")


# Exception check sex
def get_sex(sex):
    # Checks for non-whitespace characters in the original input
    if sex.isspace() is False:

        # Removes whitespace entered
        sex = sex.replace(" ", "")

        # Sets length parameters on the input
        while len(sex) != 1:
            sex = input("Please enter your sex with 'm' for male or 'f' for female: ")
            return get_sex(sex)

        # Outlines all forbidden characters
        forbidden_characters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'G', 'g', 'H', 'h',
                                'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'N', 'n', 'O', 'o', 'P', 'p',
                                'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
                                'Y', 'y', 'Z', 'z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
                                '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', '"', ',', '<', '.', '>', '/', '?',
                                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', "'"]

        # Checks the sex against the forbidden characters
        for character in sex:
            if character in forbidden_characters:
                sex = input("""Please enter your sex with "m" for male or "f" for female: """)
                return get_sex(sex)

        # Checks for whitespace with the new inputs
        if sex.isspace() is True:
            sex = input("""Please enter your sex with "m" for male or "f" for female: """)
            return get_sex(sex)

    # Corrects for whitespace in the original inputs
    else:
        sex = input("""Please enter your sex with "m" for male or "f" for female: """)
        return get_sex(sex)

    # Standardizes the return
    return sex.upper()


# Exception check retirement age
def get_retirement_age(retirement_age):
    # Checks for non-whitespace characters in the original input
    if retirement_age.isspace() is False:

        # Makes sure the retirement age is entered
        while len(retirement_age) == 0:
            retirement_age = input("Please enter your desired retirement age: ")
            return get_retirement_age(retirement_age)

        # Outlines all forbidden characters
        forbidden_characters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
                                'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
                                'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
                                'Y', 'y', 'Z', 'z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                                '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', '"', ',', '<', '.', '>', '/',
                                '?', '-', "'", " "]

        # Checks each element of the age against the forbidden characters
        for number in retirement_age:
            if number in forbidden_characters:
                retirement_age = input("Please refrain from entering letters, special characters, or spaces."
                                       "\nPlease enter your desired retirement age: ")
                return get_retirement_age(retirement_age)

        # Sets upper limit to retirement age
        if int(retirement_age) > 99:
            retirement_age = input("Woah there! I would love to be able to live and work that long,"
                                   "but perhaps we should look to retire before age 100."
                                   "\nPlease enter your desired retirement age: ")
            return get_retirement_age(retirement_age)

        # Checks for whitespace with the new inputs
        if retirement_age.isspace() is True:
            retirement_age = input("Please enter your desired retirement age: ")
            return get_retirement_age(retirement_age)

    # Corrects for whitespace in the original inputs
    else:
        retirement_age = input("Please enter your desired retirement age: ")
        return get_retirement_age(retirement_age)

    # Standardizes the return
    return retirement_age.replace(" ", "")


# Exception check current_income
def get_current_income(current_income):
    # Checks for non-whitespace characters in the original input
    if current_income.isspace() is False:

        # Makes sure the amount is entered
        while len(current_income) == 0:
            retirement_age = input('Please enter your current gross income (rounded to the nearest USD): ')
            return get_current_income(current_income)

        # Outlines all forbidden characters
        forbidden_characters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
                                'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
                                'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
                                'Y', 'y', 'Z', 'z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                                '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', '"', ',', '<', '.', '>', '/',
                                '?', '-', "'", " "]

        # Checks each element of the age against the forbidden characters
        for number in current_income:
            if number in forbidden_characters:
                current_income = input("Please refrain from entering letters, special characters, or spaces."
                                       '\nPlease enter your current gross income (rounded to the nearest USD): ')
                return get_current_income(current_income)

        # Sets lower limit to retirement age
        if int(current_income) < 0:
            current_income = input("We are sorry to hear about your situation,"
                                   "but our calculations only work on positive amounts."
                                   '\nPlease enter your current gross income (rounded to the nearest USD): ')
            return get_current_income(current_income)

        # Checks for whitespace with the new inputs
        if current_income.isspace() is True:
            current_income = input('Please enter your current gross income (rounded to the nearest USD): ')
            return get_current_income(current_income)

    # Corrects for whitespace in the original inputs
    else:
        current_income = input('Please enter your current gross income (rounded to the nearest USD): ')
        return get_current_income(current_income)

    # Standardizes the return
    return current_income.replace(" ", "")




# Part 3:
# Calculations

# Determines total life expectancy using inputs and table
# The table is from https://www.ssa.gov/oact/STATS/table4c6.html
def life_expectancy(sex, age):
    if sex == "M":
        return male_life_expectancy[age] + age
    if sex == "F":
        return female_life_expectancy[age] + age


# Using Schwab Estimates:
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


# PART 4:
# Driver code

# Introduction
print("Hello and thank you for using our Robo-advisor!")
# Gives it a human feel
time.sleep(.5)
print("To get started, we're going to need some personal information.")

# Retrieves first name
first_name = input("Please enter your first name: ")
# Exception checks and updates input
correct_first_name = first_name.replace(first_name, f"{get_first_name(first_name)}")

# Retrieves last name
last_name = input("Please enter your last name: ")
# Exception checks and updates input
correct_last_name = last_name.replace(last_name, f"{get_last_name(last_name)}")

# Retrieves age
self_age = input("How old are you (rounded to the nearest whole year): ")
# Exception checks and updates input
correct_self_age = int(self_age.replace(self_age, f"{get_age(self_age)}"))

# Retrieves sex
self_sex = input("""What is your sex (enter "m" for male or "f" for female): """)
# Exception checks and updates input
correct_self_sex = self_sex.replace(self_sex, f"{get_sex(self_sex)}")

# Retrieves retirement age
self_retirement_age = input("Please enter your desired retirement age: ")
# Exception checks and updates input
correct_self_retirement_age = int(self_retirement_age.replace(self_retirement_age, f"{get_retirement_age(self_retirement_age)}"))

# Retrieves income
current_income = input('Please enter your current gross income (rounded to the nearest USD): ')
# Exception checks and updates input
correct_current_income = int(current_income.replace(current_income, f"{get_current_income(current_income)}"))

# Retrieves number of children
children = input('Do you currently have children? (y/n): ')

# Retrieves target savings goal
retirement_goal = input('Please enter your retirement savings goal rounded to the nearest USD: ')

# Retrieves current retirement savings
current_savings =input('Please enter your current retirement savings amount rounded to the nearest USD: ')

# Retrieves house status
housing = input('Do you currently own a home? (y,n):')
if housing == 'y':
    mortgage_rate = input('What is your current interest rate?')



# If has 401k, Retrieves 401k % match
company_401k = input('Does your company offer a 401k? (y,n):')
if company_401k == 'y':
    company_match =int(input('How much does the company match?'))

# Roth vs Traditional 
roth_vs_traditional = input('Do you expect to pay more in taxes during retirement than you currently are? (y,n):')

# Investment percentage
investment_percentage = .15

# Annual Investment
annual_investment = current_income * investment_percentage

# Determines how many years until retirement
yrs_to_retirement = correct_self_retirement_age - correct_self_age




# Part 5:
# results

# Shows results to user
print("One moment while we calculate your optimal asset allocation.")
# Gives program a more human feel
time.sleep(3)
print("Hi", correct_first_name, correct_last_name)
print("Based on your life expectancy of", life_expectancy(correct_self_sex, correct_self_age), "years")
print("We suggest you invest", stock_allocation(yrs_to_retirement), "% in stocks,", bond_allocation(yrs_to_retirement),
      "% in bonds, and", cash_allocation(yrs_to_retirement), "% in cash.")
print("Based on your total income of $", current_income,"and investment percentage of", investment_percentage,
      "%, you will be investing $", annual_investment," annually")
# at this pace and an average roi of %, we calculate your expected savings at # years old to be $
# that means you are ahead/behind by $ a year or $ a month


# product suggestion

print("Based on your input, we would like to suggest some products to you.")
# if have kid, offer 529
if children == 'y':
    print('We suggest that you start contributing to a 529 plan for your children if you havent done so already')
# if interest rate higher than today, refinance
# if company match greater than 0, match up to mactch % or $ annually
if company_match > 0:
    print('We suggest you contribute at least ', company_match, 'of your salary annually to your 401k to take advatntage of your company match. ')
# if roth_vs_traditional == 'y' , then roth 401k/ira
if roth_vs_traditional == 'y':
    print('Based on your future tax assumptions, we suggest you take advantage of the ROTH 401k/IRA options.')
if roth_vs_traditional == 'n':
    print('Based on your future tax assumptions, we suggest you stick with the Traditional 401k/IRA options.')


