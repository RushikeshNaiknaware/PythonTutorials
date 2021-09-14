import random
import sys
from typing import Final

# Generate a lottery
lottery = random.randint(10,99)
print("Lottery number is ready.")

MIN_LIMIT :Final = 10
MAX_LIMIT :Final = 99

guess_str = input("Please enter the two digit guess number for your lottery:")

if(len(guess_str) != 2):
	print("Please enter the valid two digit guess number only.")
	sys.exit(0)

if(len(guess_str.lstrip('0')) != 2):
	print("Leading 0's are not permitted, Please enter the valid two digits without leading 0's.")
	sys.exit(0)

guess = eval(guess_str)

print("Guess number ",guess)
lfd = lottery // 10
lsd = lottery % 10
gfd = guess // 10
gsd = guess % 10


if (lottery == guess):
    print("Congratulations, you have won Rs 10,000")
elif(lfd == gsd and lsd == gfd):
    print("Congratulations, you have won Rs 3,000")
elif(lfd == gfd or lfd == gsd or lsd == gfd or lsd == gsd):
    print("Congratulations, you have won Rs 1,000")
else:
    print("Sorry, better luck next time")
