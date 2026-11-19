



def print_stert_menu():
    print("""
=====================
      War Game
=====================
1. play new game
2. exit
""")



def print_turn_menu():
    while True:
        print("""
========== TURN ==========
1. to play
2. to exit
""")
        chooice = input("please chooce an option ")
        if chooice == "1":
            return True
        elif chooice == "2":
            return False
        else:
            print("most be 1 or 2 only")



def print_result(gamer_card,computer_card,winner,gamer,computer):
    print(f"""
{gamer.name} card       {gamer_card}
computer card    {computer_card}
win in this turn {winner}
{gamer.name} have {gamer.len_cards()} cards  computer have {computer.len_cards()} cards
""")