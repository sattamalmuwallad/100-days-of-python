year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994: # fixed so when adding 1994 year no bugs
    print("You are a Gen Z.")
