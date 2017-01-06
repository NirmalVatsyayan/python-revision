import math

#absolute value || negative to positive
print("abs(-119) : ", abs(-119))
print("abs(100.12) : ", abs(100.12))

#float absolute value || will not work on complex
#fabs could only work on value which could be converted
#to float
print("fabs(-119) : ",math.fabs(-119))
print("fabs(100.12) : ",math.fabs(100.12))
#print(math.fabs(3+4j)) # will give error as complex - float is issue

#max
print("max(10, 20, 30) : ", max(10, 20, 30))

#min
print("min(10, 20, 30) : ", min(10, 20, 30))

#power || will return result in float
print("math.pow(10, 2) : ", math.pow(10, 2))
print("math.pow(10, -2) : ", math.pow(10, -2))

#square root
print("math.sqrt(100) : ", math.sqrt(100))
print("math.sqrt(math.pi) : ", math.sqrt(math.pi))

#rounding off
print(round(100.11))
print(round(100.1111, 2))  # 2nd parameter is upto what decimal place
print(round(100.1111, 3))

#ceil - smallest integer not less than argument
print(math.ceil(100.2))
print(math.ceil(-100.2))

#floor - immediate big number than argument
print(math.floor(100.2))
print(math.floor(-100.2))

#exp - returns e^x (x being argument)
#match results from https://www.easycalculation.com/e-power-x.php
print(math.exp(2))

#log
print("math.log(1) : ", math.log(1))
print("math.log(88.88) : ", math.log(88.88))
