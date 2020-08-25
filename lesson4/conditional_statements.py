# Write an if statement that lets a competitor know which of these prizes they
# won based on the number of points they scored, which is stored in the integer
# variable points.
# All of the lower and upper bounds here are inclusive, and points can only
# take on positive integer values up to 200.
#
# In your if statement, assign the result variable to a string holding the
# appropriate message based on the value of points. If they've won a prize,
# the message should state "Congratulations! You won a [prize name]!" with the
# prize name. If there's no prize, the message should state "Oh dear, no prize
# this time."

points = 174  # use this input to make your submission

result = ""
# write your if statement here
if points >= 1 and points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points >= 51 and points <= 150:
    result = "Oh dear, no prize this time."
elif points >= 151 and points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
elif points >= 181 and points <= 200:
    result = "Congratulations! You won a penguin!"
else:
    result = "Oh dear, no prize this time."

print(result)


# '''
# You decide you want to play a game where you are hiding
# a number from someone.  Store this number in a variable
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 50
guess = 20

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"

print(result)


# '''
# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = "CA" #Either CA, MN, or NY
purchase_amount = 400 #amount of purchase

if state == "CA": #provide conditional for checking state is CA
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "MN": #provide conditional for checking state is MN
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "NY": #provide conditional for checking state is NY
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)
