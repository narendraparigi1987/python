import sys

def main():
    print '''choose any one of the below values
            rock
            paper
            scissor
          '''
    while True:
        if str(raw_input('Type "yes" to continue with game or "no" to exit: ')) != 'yes':
            break
        else:
            game_dict = {'rock':1, 'paper':2, 'scissor':3}
            input1 = str(raw_input('player 1: enter your choice: '))
            input2 = str(raw_input('player 2: enter your choice: '))
            a = game_dict.get(input1)
            b = game_dict.get(input2)
            diff = b-a
            if diff in [-1,2]:
                print 'player 1 wins'
            elif diff in [1,-2]:
                print 'player 2 wins'
            elif diff in [0]:
                print 'draw'

if __name__ == '__main__':
    main()