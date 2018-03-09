import sys

def main():
    print 'Welcome to Rock Paper Scissor Game'
    while True:
        quit = raw_input('enter "enter" to continue: ')
        if quit != 'enter':
            break
        else:            
            input1= str(raw_input('Player 1 enter your choice: '))
            input2= str(raw_input('Player 2 enter your choice: '))

            if (input1 == 'rock' and input2 == 'scissor') or (input1 == 'scissor' and input2 == 'paper') or (input1 == 'paper' and input2 == 'rock'):
                print 'Congratulations to Player 1'
            elif (input1 == 'rock' and input2 == 'paper') or (input1 == 'scissor' and input2 == 'rock') or (input1 == 'paper' and input2 == 'scissor'):
                print 'Congratulations to Player 2'
            elif input1 == input2:
                print 'Match is draw'

if __name__ == '__main__':
    main()