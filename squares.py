# Codédex :: Squares

number = int(input('Enter a number: '))
total = 0

for i in range(1, number+1):
  total += i**2

print(total)