from cs50 import get_float


# Prompts user to give valid number
while True:
    dollar = get_float("Change owed: ")
    if dollar > 0:
        break
    
cents = round(dollar*100)
coins = 0

while cents >= 25:
    cents -= 25    
    coins += 1

while cents >= 10:
    cents -= 10    
    coins += 1

while cents >= 5:
    cents -= 5    
    coins += 1

while cents >= 1:
    cents -= 1    
    coins += 1
    
print(coins)

    



