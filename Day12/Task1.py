enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies inside function: {enemies}")

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
#print(potion_strength) ## can't access since its oinly defined in the local scope


player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

game()
print(player_health)