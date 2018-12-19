import random
import time
import os


def work(b,a):
        
        if b==a:
            return True
        elif b>a:
            print('Too high..! Wanna guess again? ')
            
           
        elif b<a:
            print('Too low..! Wanna guess again? ')
            
        return False    
    
        
def main():
    a= random.randrange(100);
    c = 'e'
    guess = 0;

    while c != 'q':
        print()
        try:
                b = int(input('ENTER YOUR NUMBER '))
                print('Checking...Please Wait!!')
                time.sleep(1)
                print()
                guess += 1
                if work(b,a):
                    print('CORRECT ANSWER..!! You did that in %  guesses ' %guess)
                    break
                else:
                    print('Press ENTER to continue or q to exit ')
                    c = input()
        except:
                print('Invalid Input....TRY AGAIN')
    print('Thank you...!! ')
    print()
    print()
    time.sleep(2)
    print('Press ENTER if you want to play again, and E to EXIT')
    if input() != 'E':
        os.system('cls')
        main()
