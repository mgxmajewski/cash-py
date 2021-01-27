from cs50 import get_float


# Prompts user to give valid number
while True:
    n = get_float("Change owed: ")
    if n > 0:
        break
    
