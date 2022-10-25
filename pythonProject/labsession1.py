# Task 1 -  Completed
print("Hello World")

# Task 2 - Completed
print("Hello, Jason")

# Task 3 - Completed
Celcius = float(input("What is the temperature (C) today: "))
Fahrenheit = float((Celcius * 1.8) + 32)
print(Fahrenheit)
print()

# Task 4 - Completed
matchesPlayed = 609
battlesPlayed = 1014
notOut = 162
runScore = 48426

BattleAvg = runScore / (battlesPlayed - notOut)
print("The battle average is" + str(BattleAvg))
print()

# Task 5 - Completed
for x in range(3):
    StudentNum = int(input("How many students are there? "))
    StudentGroup = int(StudentNum // 24)
    LeftOverGroup = int(StudentNum % 24)
    print("Full groups: " + str(StudentGroup))
    print("Remaining people in left over group: " + str(LeftOverGroup))
    print()
