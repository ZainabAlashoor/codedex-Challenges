# Codédex : Planet Weights

earth_weight = float(input('Enter your weight: '))
num = int(input('Enter a planet number: '))

if earth_weight ==1:
  destination_weight = earth_weight * 0.38
elif earth_weight ==2:
  destination_weight = earth_weight * 0.91
elif earth_weight ==3:
  destination_weight = earth_weight * 0.38
elif earth_weight ==4:
  destination_weight = earth_weight * 2.53
elif earth_weight ==5:
  destination_weight = earth_weight * 1.07
elif earth_weight ==6:
  destination_weight = earth_weight * 0.89
elif earth_weight ==7:
  destination_weight = earth_weight * 1.14
else:
  print('Invalid planet number')