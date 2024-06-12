import random
import requests

player_1 = input("What is your name?")
print("Hi " + player_1 + "! " + "\n" + "Welcome to  Top Trumps: Pokemon Edition")
print()

def game_loop():
    def trumps_game():
        def generate_random_numbers():
            random_numbers = random.sample(range(1, 151), 3)
            return random_numbers

        number_selection = generate_random_numbers()
        print("Your three pokemon options are:", number_selection)

        chosen_number = input("Which pokemon do you want?")


        def random_pokemon(chosen_number):
            url = "https://pokeapi.co/api/v2/pokemon/{}/".format(int(chosen_number))
            response = requests.get(url)
            # print(response)
            pokemon = response.json()
            return {
                "name": pokemon["name"],
                "id": pokemon["id"],
                "base experience": pokemon["base_experience"],
                "height": pokemon["height"],
                "weight": pokemon["weight"],
                "type": pokemon["types"][0]["type"]["name"]
            }

        def random_pokemon_opponent():
            your_number = random.randrange(1, 151)
            return random_pokemon(your_number)

        my_pokemon = random_pokemon(chosen_number)
        print("You got number", my_pokemon["id"], ",", my_pokemon["name"],"!")
        print()

        def poke_battle():
            print("Here are your stats:")
            print("base experience:", my_pokemon["base experience"], "\n", "height:", my_pokemon["height"], "\n", "weight:", my_pokemon["weight"], "\n", "type:", my_pokemon["type"])

            chosen_stat = input("Which stat do you want to battle with?")

            opponent_pokemon = random_pokemon_opponent()
            print("Your opponent's pokemon is", opponent_pokemon["name"], "!")
            print()
            ready = input("Are you ready?")
            if ready == "yes" or ready == "y":
                print()
                print("Battle time!", my_pokemon["name"], "vs", opponent_pokemon["name"])
            elif ready == "no" or ready == "n":
                print("I guess we'll just wait...")
            else:
                print("Not valid")

            print()

            t_1 = "normal"
            t_2 = "fighting"
            t_3 = "flying"
            t_4 = "poison"
            t_5 = "ground"
            t_6 = "rock"
            t_7 = "bug"
            t_8 = "ghost"
            t_9 = "steel"
            t_10 = "fire"
            t_11 = "water"
            t_12 = "grass"
            t_13 = "electric"
            t_14 = "psychic"
            t_15 = "ice"
            t_16 = "dragon"
            t_17 = "dark"
            t_18 = "fairy"
            t_19 = "unknown"
            t_20 = "shadow"

            my_stat = my_pokemon[chosen_stat]
            opponent_stat = opponent_pokemon[chosen_stat]
            if chosen_stat == "type":
                if my_stat == t_1 and opponent_stat in [t_5, t_7, t_11, t_12, t_13, t_17, t_18, t_20, t_19]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_1 and opponent_stat not in [t_1, t_5, t_7, t_11, t_12, t_13, t_17, t_18, t_20, t_19]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_2 and opponent_stat in [t_1, t_4, t_5, t_7, t_12, t_14, t_17, t_18, t_19]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_2 and opponent_stat not in [t_2, t_1, t_4, t_5, t_7, t_12, t_14, t_17, t_18, t_19]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_4 and opponent_stat in [t_1, t_2, t_5, t_7, t_11, t_12, t_14, t_16, t_18]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_4 and opponent_stat not in [t_4, t_1, t_2, t_5, t_7, t_11, t_12, t_14, t_16, t_18]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_5 and opponent_stat in [t_6, t_9, t_13, t_14, t_16, t_17, t_18, t_19, t_20]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_5 and opponent_stat not in [t_5, t_6, t_9, t_13, t_14, t_16, t_17, t_18, t_19, t_20]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_6 and opponent_stat in [t_1, t_3, t_4, t_9, t_10, t_13, t_14, t_15, t_18, t_19]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_6 and opponent_stat not in [t_6, t_1, t_3, t_4, t_9, t_10, t_13, t_14, t_15, t_18, t_19]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_7 and opponent_stat in [t_5, t_6, t_8, t_9, t_12, t_14, t_16, t_18, t_19]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_7 and opponent_stat not in [t_7, t_5, t_6, t_8, t_9, t_12, t_14, t_16, t_18, t_19]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_8 and opponent_stat in [t_1, t_2, t_3, t_4, t_5, t_6, t_9, t_10, t_11, t_16]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_8 and opponent_stat not in [t_8, t_1, t_2, t_3, t_4, t_5, t_6, t_9, t_10, t_11, t_16]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_9 and opponent_stat in [t_1, t_2, t_4, t_12, t_13, t_14, t_16, t_18, t_19]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_9 and opponent_stat not in [t_9, t_1, t_2, t_4, t_12, t_13, t_14, t_16, t_18, t_19]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_10 and opponent_stat in [t_1, t_2, t_4, t_5, t_7, t_9, t_12, t_15, t_17, t_20]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_10 and opponent_stat not in [t_10, t_1, t_2, t_4, t_5, t_7, t_9, t_12, t_15, t_17, t_20]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_11 and opponent_stat in [t_2, t_5, t_6, t_7, t_9, t_10, t_16, t_17, t_18, t_19]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_11 and opponent_stat not in [t_11, t_2, t_5, t_6, t_7, t_9, t_10, t_16, t_17, t_18, t_19]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_12 and opponent_stat in [t_5, t_6, t_8, t_11, t_13, t_14, t_17, t_18, t_19, t_20]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_12 and opponent_stat not in [t_12, t_5, t_6, t_8, t_11, t_13, t_14, t_17, t_18, t_19, t_20]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_13 and opponent_stat in [t_2, t_3, t_4, t_7, t_8, t_10, t_11, t_14, t_15, t_16]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_13 and opponent_stat not in [t_13, t_2, t_3, t_4, t_7, t_8, t_10, t_11, t_14, t_15, t_16]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_14 and opponent_stat in [t_1, t_3, t_8, t_10, t_11, t_15, t_16, t_18, t_20]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_14 and opponent_stat not in [t_14, t_1, t_3, t_8, t_10, t_11, t_15, t_16, t_18, t_20]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_15 and opponent_stat in [t_1, t_2, t_3, t_4, t_5, t_7, t_8, t_9, t_11, t_12]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_15 and opponent_stat not in [t_15, t_1, t_2, t_3, t_4, t_5, t_7, t_8, t_9, t_11, t_12]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_16 and opponent_stat in [t_1, t_2, t_3, t_6, t_10, t_12, t_15, t_17, t_20]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_16 and opponent_stat not in [t_16, t_1, t_2, t_3, t_6, t_10, t_12, t_15, t_17, t_20]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_17 and opponent_stat in [t_3, t_4, t_6, t_7, t_8, t_9, t_13, t_14, t_15, t_20]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_17 and opponent_stat not in [t_17, t_3, t_4, t_6, t_7, t_8, t_9, t_13, t_14, t_15, t_20]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_18 and opponent_stat in [t_3, t_8, t_10, t_13, t_15, t_16, t_17, t_19, t_20]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_18 and opponent_stat not in [t_18, t_3, t_8, t_10, t_13, t_15, t_16, t_17, t_19, t_20]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_19 and opponent_stat in [t_3, t_4, t_8, t_10, t_13, t_14, t_15, t_16, t_17, t_20]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_19 and opponent_stat not in [t_19, t_3, t_4, t_8, t_10, t_13, t_14, t_15, t_16, t_17, t_20]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_20 and opponent_stat in [t_2, t_4, t_6, t_7, t_8, t_9, t_11, t_13, t_15]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_20 and opponent_stat not in [t_20, t_2, t_4, t_6, t_7, t_8, t_9, t_11, t_13, t_15]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                elif my_stat == t_3 and opponent_stat in [t_1, t_2, t_5, t_6, t_7, t_9, t_10, t_11, t_12, t_20]:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat == t_3 and opponent_stat not in [t_3, t_1, t_2, t_5, t_6, t_7, t_9, t_10, t_11, t_12, t_20]:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                else:
                    print("oh no... It's a draw!")
                    return "Draw"
            else:
                if my_stat > opponent_stat:
                    print("Victory! You win this round", player_1, "!!!!")
                    return "You"
                elif my_stat < opponent_stat:
                    print("Defeat...You got your butt kicked this round", player_1, "...")
                    return "Opponent"
                else:
                    print("oh no... It's a draw!")
                    return "Draw"

        winner = poke_battle()
        return winner

    player_wins = {"You": 0, "Opponent": 0}

    for i in range(3):
        winner = trumps_game()
        if winner != "Draw":
            player_wins[winner] += 1

    print("BATTLE RESULTS:")
    print(player_1, ":", player_wins["You"])
    print("Opponent:", player_wins["Opponent"])
    if player_wins["You"] > player_wins["Opponent"]:
        print("YOU TOTALLY RULE!!")
    elif player_wins["You"] < player_wins["Opponent"]:
        print("TOTAL DEFEAT!!! Go try and catch some more pokemon!!")
    else:
        print("How lame, it's an overall draw...")

    try_again = input("Are you ready to try again?")

    if try_again == "yes" or try_again == "y":
        game_loop()
    else:
        print("Come back when you've leveled up, then!")

game_loop()

