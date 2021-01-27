from cs50 import get_float


# Prompts user to give valid number
while True:
    dollar = get_float("Change owed: ")
    if dollar > 0:
        break
    
cents = round(dollar*100)
coins = 0

nominals = [25, 10, 5, 1]

for i in range(len(nominals)):
    while cents >= nominals[i]:
        cents -= nominals[i]    
        coins += 1

    
print(coins)

    



