try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please enter a valid number.")
    int(input("Please enter a valid number."))
    
if age > 18:
    print("You can drive at age {age}.")
