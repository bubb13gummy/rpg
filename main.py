import random

player = {
    "name": "",
    "hp": 100,
    "max_hp": 100,
    "attack": 15,
    "level": 1,
    "exp": 0,
    "gold": 0,
    "potions": 3
}

enemies = [
    {"name": "Slime", "hp": 30, "attack": 5, "gold": 10, "exp": 15},
    {"name": "Goblin", "hp": 50, "attack": 8, "gold": 20, "exp": 25},
    {"name": "Skeleton", "hp": 70, "attack": 12, "gold": 35, "exp": 40},
    {"name": "Dark Knight", "hp": 100, "attack": 18, "gold": 60, "exp": 70}
]


def show_stats():
    print(f"""
=========================
      {player['name']}
=========================
Level   : {player['level']}
HP      : {player['hp']}/{player['max_hp']}
Attack  : {player['attack']}
EXP     : {player['exp']}
Gold    : {player['gold']}
Potions : {player['potions']}
=========================
""")


def level_up():
    need = player["level"] * 50

    # always check
    while player["exp"] >= need:
        player["level"] += 1
        player["max_hp"] += 20
        player["attack"] += 5
        player["hp"] = player["max_hp"]

        print("\nLEVEL UP!")
        print(f"You are now level {player['level']}!")


def battle():
    enemy = random.choice(enemies).copy()

    print(f"\nA wild {enemy['name']} appeared!")

    while enemy["hp"] > 0 and player["hp"] > 0:

        print(f"""
Your HP: {player['hp']}/{player['max_hp']}
{enemy['name']} HP: {enemy['hp']}

[1] Attack
[2] Heal
[3] Run
""")

        choice = input("> ")

        if choice == "1":
            damage = random.randint(
                player["attack"] - 3,
                player["attack"] + 3
            )

            enemy["hp"] -= damage

            print(f"\nYou hit {enemy['name']} for {damage} damage!")

        elif choice == "2":

            if player["potions"] > 0:
                heal = random.randint(20, 35)

                player["hp"] += heal

                if player["hp"] > player["max_hp"]:
                    player["hp"] = player["max_hp"]

                player["potions"] -= 1

                print(f"\nYou healed for {heal} HP!")

            else:
                print("\nNo potions left!")

        elif choice == "3":

            chance = random.randint(1, 100)

            if chance <= 50:
                print("\nYou escaped!")
                return
            else:
                print("\nFailed to escape!")

        else:
            print("\nInvalid choice.")
            continue

        if enemy["hp"] > 0:
            enemy_damage = random.randint(
                max(0, enemy["attack"] - 2), #check bound
                enemy["attack"] + 2
            )

            player["hp"] -= enemy_damage

            print(f"{enemy['name']} hit you for {enemy_damage} damage!")

    if player["hp"] <= 0:
        print("\nYou died...")
        print("Game Over.")
        player["alive"] = False
        return

    print(f"\nYou defeated {enemy['name']}!")

    player["gold"] += enemy["gold"]
    player["exp"] += enemy["exp"]

    print(f"You gained {enemy['gold']} gold!")
    print(f"You gained {enemy['exp']} EXP!")

    drop = random.randint(1, 100)

    if drop <= 30:
        player["potions"] += 1
        print("Enemy dropped a potion!")

    level_up()


def shop():
    while True:
        print(f"""
=========================
          SHOP
=========================
Gold: {player['gold']}

1. Small Potion (15 gold)
2. Leave
""")

        choice = input("> ")

        if choice == "1":

            if player["gold"] >= 15:
                player["gold"] -= 15
                player["potions"] += 1

                print("\nYou bought a potion.")

            else:
                print("\nNot enough gold.")

        elif choice == "2":
            return

        else:
            print("\nInvalid choice.")


def main_menu():
    while True:
        print(f"""
=========================
        TEXT RPG
=========================

HP: {player['hp']}/{player['max_hp']}
EXP: {player['exp']}
Level: {player["level"]}

1. Battle
2. Stats
3. Shop
4. Exit
""")

        choice = input("> ")

        if choice == "1":
            battle()

        elif choice == "2":
            show_stats()

        elif choice == "3":
            shop()

        elif choice == "4":
            print("\nGoodbye.")
            break

        else:
            print("\nInvalid choice.")


while True:
    print("=========================")
    print(" WELCOME TO TEXT RPG ")
    print("=========================")

    player["name"] = input("\nEnter your name: ")

    if len(player["name"]) > 10:
        print("[-] Name must be length 10!!\n\n")
        continue

    print(f"\nWelcome, {player['name']}!")

main_menu()
