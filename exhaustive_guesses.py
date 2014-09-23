x = float(raw_input("Enter a positive number: "))

epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while (abs(ans**2 - x)) >= epsilon and ans <= x:
 ans += step
 numGuesses += 1
print('numGuesses = ' + str(numGuesses))
if abs(ans**2-x) >= epsilon:
 print('Failed on square root of ' + str(x))
else:
 print(str(ans) + ' is close to the square root of ' + str(x))

print "*********"

epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
 print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
 numGuesses += 1
 if ans**2 < x:
  low = ans
 else:
  high = ans
 ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))