#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'The movie is about to begin, we recommend '
message1 = 'The movie that was selected is: '
message2 = 'The letter is : '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your connection speed in Mbps?"))

# if input value was higher or equal to 25
if connection >= 25:
    message = message + 'setting video to 4k.'
elif connection >= 5:
    message = message + 'setting video to 1080p.'
elif connection >= 2:
    message = message + 'setting video to 720p.'
else:
    message = message + 'finding another access network.'
print(message)

selection = float(input("Please enter a number between 1 - 4?"))
if selection == 1:
    message1 = message1 + 'harry potter'
elif selection == 2:
    message1 = message1 + 'Hobbit & Lord of the rings'
elif selection == 3:
    message1 = message1 + 'Chronicles of Narnia'
elif selection == 4:
    message1 = message1 + 'Indiana Jones'
else:
    message1 = ('Number is not valid')
print(message1)

score = float(input("Please enter a number score of 1 - 100?"))
if score <= 59:
    message2 = message2 + 'F'
elif score <= 69:
    message2 = message2 + 'D'
elif score <= 79:
    message2 = message2 + 'C'
elif score <= 89:
    message2 = message2 + 'B'
elif score <= 100:
    message2 = message2 + 'A'
else:
    message2 = 'Number is not valid'
print(message2)
