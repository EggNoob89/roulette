import random 
import time

class RussianRoulette: 
    def __init__(self):
        self.play = None
        self.bullets = None 
        self.death = None
    def introduction(self):
        print('Welcome to russian roulette!')
        time.sleep(2)
    def play_mechanism(self):
        while self.play is None:
            self.play = input("Do you want to play(y/n)?> ").upper()
            if self.play in ["YES", "Y"]:
                print("it's a yes then!")
            elif self.play in ["NO", "N"]:
                print("It's a no uh?")
                time.sleep(2)
                print("GOODBYE THEN!")
                exit()
            else:
                print("Invalid Input!")
                time.sleep(1)
                print("Try again!")
                time.sleep(1)
                self.play = None
    def bullets_count(self):
        while self.bullets is None:
            try:
                self.bullets = int(input("How many bullets in the barrel?> "))
            except ValueError:
                print("Invalid Input")
                print("Input a digit")
                self.bullets = None
    def play_the_game(self):
        self.death = None
        print(f"There are {self.bullets} bullets in the barrel!")
        time.sleep(1)
        print("you pull the trigger")
        time.sleep(1)
        print("BANG!!")
        time.sleep(2)
        death_or_alive = random.randint(1, self.bullets)
        if death_or_alive == 1:
            print("The bullets goes through your head")
            time.sleep(1)
            print("You are dead bud")
            self.death = 1
            exit
        else:
            print("You live to see another day!")
            while self.death is None:
                want_to_go_again = input("Wanna keep playing the game?> ").upper()
                if want_to_go_again in ["Y", "YES"]:
                    print("alright bud let's keep going!")
                    self.bullets -= 1 
                    self.death = 1
                    self.play_the_game()
                elif want_to_go_again in ["N", "YES"]:
                    print("Alright, alright, alright!")
                    time.sleep(1)
                    print("Goodbye then friend!")
                    self.death = 1
                    exit
                else:
                    print("invalid input!")
                    time.sleep(1)
                    print("try again!")

if __name__ == "__main__":
    Russian = RussianRoulette()
    Russian.introduction()
    Russian.play_mechanism()
    Russian.bullets_count()
    Russian.play_the_game()