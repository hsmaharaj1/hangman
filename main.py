# 
# Author: Himanshu
# Project : HangMan 
# File Type: Main
# 
# 
import sys
import re
from words import generate_words

class HangMan():
    def __init__(self):
        self.name = input("Enter your name: ")
        print("Good Luck! ", self.name)
        print("Starting H A N G M A N ...")
        self.new = None
        self.GAME_OVER = True
        self.new_words()
        self.game_loop()
        
    def new_words(self):
        self.new = str(generate_words()).upper()
        return self.new
        
    def game_loop(self):
        
        self.guess = input("How many attempts do you wanna make? [1-30]\n")
        # Main Game Loop
        if int(self.guess) != 0 and (1 <= int(self.guess) <= 30):
            print("Selecting a WORD....")
            while self.GAME_OVER:
                self.hid_word = "*" * (len((self.new).strip()))
                # print(len(self.new))
                self.lst_new = list(self.new)
                self.lst_hid_word = list(self.hid_word)
                self.str = ""
                self.lst_wrong = []
                self.str_wrong = ", "
                self.final_check = True
                print("Total Attempts - ", self.guess)
                
                
                for a in range(int(self.guess)):
                    print("----------------------------------")
                    print("Attempts Left - ", self.guess)
                    print("The Hidden Word is [ ", self.hid_word, " ]")
                    self.ltr = input("Enter >> ").upper()
                    # Logic for checking Result
                    if len(self.ltr) > 1:
                        if (re.match(self.new.strip(), self.ltr.strip())):
                            print("---------------------------------- \n")
                            print("You WON!!")
                            print("The Hidden Word is " + self.new)
                            print("----------------------------------")
                            self.final_check = False
                            return
                        else:
                            print("--> OOPs! Wrong")
                            pass

                    elif (self.ltr) in self.new and len(self.ltr) == 1:
                        print("--> Correct Guess!")
                        self.index = self.new.find(self.ltr)
                        
                        n = 0
                        for i in self.lst_new:
                            if i == self.ltr:
                                # self.lst_hid_word[self.index] = self.ltr
                                self.lst_hid_word[n] = self.ltr
                            n += 1
                                
                        self.hid_word = self.str.join(self.lst_hid_word)
                        
                        # When the word is matched
                        if (re.match((self.new).strip(), self.hid_word)):
                            print("----------------------------------")
                            print("You WON!!")
                            print("The Hidden Word is [ ", self.hid_word, " ]")
                            print("----------------------------------")
                            self.final_check = False
                            return

                    else:
                        self.lst_wrong.append(self.ltr)
                        print("Wrong Guesses  [", self.str_wrong.join(self.lst_wrong), "] ")
                        print("--> OOPs! Wrong")

                    self.guess = int(self.guess) - 1

                if self.final_check:
                    print("----------------------------------")
                    print("You failed to Guess the Word \n G A M E   O V E R")
                    print("The Word was ", self.new)        
                    self.GAME_OVER = False


        else:
            print("Please Enter a Valid Number")
            pass



if __name__ == "__main__":
    game = HangMan()
    print("Outta Loop")
    while True:
        ask = input("\nWanna Play Again? [Y/N] \n > ")
        if ask == 'y' or ask == 'Y':
            game = HangMan()
        elif ask == 'n' or ask == 'N':
            sys.exit()
        else:
            print("Invalid Input")
            pass
        
        
            

