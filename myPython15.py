
enemies = 1

def increase_emenies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_emenies()
print(f"Emenies outside function: {enemies}")

"""
def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()
print(potion_strength)
"""

player_helth = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(potion_strength)
    drink_potion
print(player_helth)


game_level = 3
enemales = ["Skeleton", "Zombie", "Alies"]
if game_level < 5:
    new_enemy = enemies
print(new_enemy)

################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


