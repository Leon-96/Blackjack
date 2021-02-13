from art import logo
import os
import random
import pyfiglet

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def black_jack():
    os.system('clear')

    print(logo, "\n")
    print('''Welcome to Leon's Casino \n''')
    print("The House rules are as follows : \n")
    print('''##The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.\n''')

    choice2 = input("Do you want to continue?Type 'y' for yes and 'n' for no to quit the program :\n")
    if choice2 == 'y':
        ucard1 = random.choice(cards)
        ucard2 = random.choice(cards)

        if ucard1 == 11:
            if ucard1 + ucard2 > 21:
                ucard1 = 1
        if ucard2 == 11:
            if ucard1 + ucard2 > 21:
                ucard2 = 1
        dlrcard1 = random.choice(cards)

        usrcard = [ucard1, ucard2]

        dlrcard = [dlrcard1, "?"]

        print("Your Cards : ", usrcard)
        print(f"Your total is : {sum(usrcard)}\n")
        print(f"The Dealer Has : {dlrcard}")

        if ucard1 == 11:
            if ucard2 == 10:
                print(pyfiglet.figlet_format("BLACKJACK!"))
                print("You've hit Blackjack! You've won")
                again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                if again == 'y':
                    black_jack()
                else:
                    os.system('clear')
                    exit()

        if ucard2 == 11:
            if ucard1 == 10:
                print(pyfiglet.figlet_format("BLACKJACK!"))
                print("You've hit Blackjack! You've won")
                again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                if again == 'y':
                    black_jack()
                else:
                    os.system('clear')
                    exit()

        keep_hittin = True

        while keep_hittin:
            hos = input("HIT or STAND? Type 'h' for HIT or 's' for STAND \n")

            if hos == 'h':

                usrfurtcard = random.choice(cards)
                usrcard.append(usrfurtcard)
                print(f"Your Cards : {usrcard}")
                print(f"Your total is : {sum(usrcard)}\n")
                if sum(usrcard) > 21:
                    print(pyfiglet.figlet_format("BUST!"))
                    print("You've gone bust!")
                    print("The Dealer Wins.")
                    keep_hittin = False
                    again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                    if again == 'y':
                        black_jack()
                    else:
                        os.system('clear')
                        exit()
            if hos == 's':
                keep_hittin = False

                dlrcard = [dlrcard1]

                dealer_hittin = True

                while dealer_hittin:

                    dlrfurtcard = random.choice(cards)

                    dlrcard.append(dlrfurtcard)
                    print(f"The Dealer has : {dlrcard}")
                    print(f"The Dealer's total is  {sum(dlrcard)}\n")

                    if sum(dlrcard) > 21:
                        print(pyfiglet.figlet_format("BUST!"))
                        print("The Dealer has gone BUST! You Win!")
                        dealer_hittin = False
                        again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                        if again == 'y':
                            black_jack()
                        else:
                            os.system('clear')
                            exit()

                    if dlrcard1 == 11:
                        if dlrcard1 + dlrfurtcard > 21:
                            dlrcard1 = 1
                    if dlrfurtcard == 11:
                        if dlrcard1 + dlrfurtcard > 21:
                            dlrfurtcard = 1

                    if dlrcard1 == 11:
                        if dlrfurtcard == 10:
                            print(pyfiglet.figlet_format("BLACKJACK!"))
                            print("The Dealer has BlackJack! The Dealer Wins.")
                            dealer_hittin = False
                            again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                            if again == 'y':
                                black_jack()
                            else:
                                os.system('clear')
                                exit()

                    if dlrfurtcard == 11:
                        if dlrcard1 == 10:
                            print(pyfiglet.figlet_format("BLACKJACK!"))
                            print("The Dealer has BlackJack! The Dealer Wins.")
                            dealer_hittin = False
                            again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                            if again == 'y':
                                black_jack()
                            else:
                                os.system('clear')
                                exit()

                    if sum(usrcard) < sum(dlrcard):
                        print(pyfiglet.figlet_format("YOU LOST : ("))
                        print("The Dealer Wins!")
                        dealer_hittin = False
                        again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                        if again == 'y':
                            black_jack()
                        else:
                            os.system('clear')
                            exit()

                    if sum(dlrcard) > 21:
                        print(pyfiglet.figlet_format("BUST!"))
                        print("The Dealer has gone BUST! You Win!")
                        dealer_hittin = False
                        again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                        if again == 'y':
                            black_jack()
                        else:
                            os.system('clear')
                            exit()

                    if sum(usrcard) > sum(dlrcard):
                        dealer_hittin = True

                        if sum(dlrcard) < 17:
                            dealer_hittin = True

                        if sum(dlrcard) >= 17:
                            dealer_hittin = False
                            if sum(dlrcard) > 21:
                                print(pyfiglet.figlet_format("BUST!"))
                                print("The Dealer has gone BUST! You Win!")
                                again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                                if again == 'y':
                                    black_jack()
                                else:
                                    os.system('clear')
                                    exit()

                            elif sum(dlrcard) > sum(usrcard):
                                print(pyfiglet.figlet_format("YOU LOST : ("))
                                print("The Dealer Wins!")
                                dealer_hittin = False
                                again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                                if again == 'y':
                                    black_jack()
                                else:
                                    os.system('clear')
                                    exit()
                            elif sum(usrcard) > sum(dlrcard):
                                print(pyfiglet.figlet_format("YOU WIN! : )"))
                                print("You Win!\n")
                                dealer_hittin = False
                                again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                                if again == 'y':
                                    black_jack()
                                else:
                                    os.system('clear')
                                    exit()
                    if sum(usrcard) == sum(dlrcard):
                        print(pyfiglet.figlet_format("Tie!"))
                        dealer_hittin = False
                        again = input("Do you want to play again? Type 'y' for yes and 'n' for no\n")
                        if again == 'y':
                            black_jack()
                        else:
                            os.system('clear')
                            exit()

                    print('The Dealer is picking again.\n')

    if choice2 == 'n':
        os.system('clear')
        exit()


black_jack()
