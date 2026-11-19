import classes.Card as C
import random
import classes.Player as P
import func_help.printer as pr
import func_help.extraction as e
class Game:

    def run(self):
            while True:
                pr.print_stert_menu()
                chooice = input("please chooce an option ")
                if chooice == "1":
                    self.start_new_game()
                elif chooice == "2":
                    break
                else:
                    print("most be 1 or 2 only")


    def start_new_game(self):
        cards = self.create_new_deck()
        Shuffle_cards = self.Shuffle_the_deck(cards)
        player_cards = self.player_cards(Shuffle_cards)
        
        gamer = P.Player("shay",player_cards)
        computer_cards = self.player_cards(Shuffle_cards)
        computer = P.Player("computer",computer_cards)
        while True:
            if pr.print_turn_menu():
                self.play_turn(gamer,computer)
            else:
                break

    
    @staticmethod
    def create_new_deck():
        cards = []
        kinds = ["♥","♦","♠","♣"]
        for kind in kinds:
            for num in range(2,15):
                card = C.Card(num,kind)
                cards.append(card.to_propose())
        return cards


    def Shuffle_the_deck(self,cards):
        for i in range(1000):
            num_rand = random.randint(0,len(cards)-1)
            item = cards.pop(num_rand)
            cards.append(item)
        
        return cards


    @staticmethod
    def player_cards(Shuffle_cards):
        print(Shuffle_cards)
        player_cards_ = []
        while True:
            if len(player_cards_) < 26:
                card = Shuffle_cards.pop(0)
                player_cards_.append(card)
            else:
                return player_cards_

    
    def play_turn(self,gamer,computer):
        gamer_card = gamer.first_card()
        computer_card = computer.first_card()
        gamer_card_value = e.Value_Extraction(gamer_card)
        computer_card_value = e.Value_Extraction(computer_card)
        if gamer_card_value > computer_card_value:
            gamer.add_card(gamer_card,computer_card)
            winner = "gamer"
        elif gamer_card_value < computer_card_value:
            computer.add_card(gamer_card,computer_card)
            winner = "computer"
        elif gamer_card_value == computer_card_value:
             gamer.add_card(gamer_card)
             computer.add_card(computer_card)
             winner = "drow"
        pr.print_result(gamer_card,computer_card,winner,gamer,computer)


        
   

    
