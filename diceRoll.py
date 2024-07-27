# # Codédex :: Dice Roll
import random 

d1 = random.randint(1,6)
d2 = random.randint(1,6)

total = d1+d2
guess = int(input('What is the total (2-12)? '))

while guess != total:
  guess = int(input('What is the total (2-12)? '))
  if (guess == total):
    break 

print('You got it!')