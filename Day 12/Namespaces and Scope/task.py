enemies = 1

# Local Scope
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
# 오직 안에 있을때만 접근이 가능하다 .

increase_enemies()

print(f"enemies outside function: {enemies}")




# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(potion_strength)
        print(player_health)

    drink_potion()
print(player_health)