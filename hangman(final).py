import random
import string
print("H A N G M A N\n")
while True:
    play_choice=['play','exit']
    option=input('Type "play" to play the game, "exit" to quit: ')

    if option not in play_choice:
        continue

    elif option == 'play':



        words = ['python', 'java', 'kotlin', 'javascript']
        word = random.choice(words)
        guessed_list=[]
        attempts=8
        n = len(word)
        board = ['-' for i in range(n)]
        print(''.join(board))
        while attempts>=0:


    #guess = input("Input a letter: ")

            if ''.join(board) == word:
                print("You guessed the word! \nYou survived!")
                print("\n" + ''.join(board))
                break


            else:
                guess = input("Input a letter:")

                if len(guess) != 1 :
                    print("You should input a single letter\n")
                    print("\n" + ''.join(board))
                    continue

                else:

                    if guess not in string.ascii_lowercase:
                        print("It is not an ASCII lowercase letter\n")
                        print("\n" + ''.join(board))
                        continue

                    else:
                        if guess in guessed_list and guess not in board:
                            print("You already typed this letter")
                            print("\n" + ''.join(board))
                            continue

                        else:
                            guessed_list.append(guess)

                            if  guess in board:

                                print("You already typed this letter\n")

                                if attempts == 0:
                                    print("You are hanged!")
                                    break
                                else:

                                    print("\n" + ''.join(board))

                                    continue

                            elif guess in word:
                                indexes = [index for index, letter in enumerate(word) if letter == guess]
                                for num in indexes:
                                    board[num] = guess
                                print("\n" + ''.join(board))


                                continue


                            else:

                                attempts-=1
                                print("No such letter in the word")

                                if attempts == 0:
                                    print("You are hanged!")
                                    break
                                else:
                                    print("\n"+''.join(board))
                                    continue
            continue

    elif option == 'exit':
        exit()
        break
