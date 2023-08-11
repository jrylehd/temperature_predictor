# greet users.
print('Welcome to our Temperature Predictor!')

'''
Then we have to define our variables. The variables I used were the names of the days themselves.
Since the inputting will produce a string, we also have to change the outputs to floats to be able to use floating-point arithmetic.
'''
today = float(input('Enter the temperature of today : '))
yesterday = float(input('Enter the temperature of yesterday : '))
two_days_ago = float(input('Enter the temperature of two days ago : '))

# define our output using the variables above, making a new variable named "tomorrow"
tomorrow = 3*today - 3*yesterday + two_days_ago

# print our inputs along with the wanted message, and print our output; the predicted temperature for tomorrow
print('Given', str(round(today, 1)), 'of today,', str(round(yesterday, 1)), 'and', str(round(two_days_ago, 1)), 
'of the two previous days,\nthe predicated temperature of tomorrow is', str(round(tomorrow, 1)) + '.')