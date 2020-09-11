# variables
secret_word = "caterpillar"
first = secret_word[0].capitalize()
last = secret_word[len(secret_word) - 1]
board = []
for lettere in range(len(secret_word)):
    board.append("_")
board[0] = first
board[len(board) - 1] = last

game_still_going = True

used_letters = []
wrong_letters = []


def display_board():
    print(board)
def attempts_number():
    print("                                          Remaining attemps: " + str(7-len(wrong_letters)))
def play_game():
    display_board()
    attempts_number()
    global game_still_going
    while game_still_going:
        handle_turn()
        check_for_winner()


def handle_turn():
    global used_letters
    global count_start
    global game_still_going

    lettere = input("Choose a letter: ")
    used_letters.append(lettere)
    if not lettere in secret_word:
        wrong_letters.append(lettere)
        set(wrong_letters)
    print("Wrong letters: " + str(list(set(wrong_letters))))
    attempts_number()
    for lettere in used_letters:
        set(used_letters)
    print("Used letters: " + str(list(set(used_letters))))

    if len(used_letters) == 7:
        lettere = secret_word[0]

    while not (lettere in secret_word) or not \
            (0 < len(lettere) < 2) and (not len(wrong_letters) == 7)\
            and (not len(lettere) == len(secret_word)):
        lettere = input("Wrong letter. Choose another letter: ")
        display_board()
        used_letters.append(lettere)
        if not lettere in secret_word:
            wrong_letters.append(lettere)
            set(wrong_letters)
        print("Wrong letters: " + str(list(set(wrong_letters))))
        attempts_number()
        for lettere in used_letters:
            set(used_letters)
        print("Used letters: " + str(list(set(used_letters))))

        if len(wrong_letters) == 7:
            lettere = secret_word[0]

    def find_all(p, s):
        # Yields all the positions of the pattern p in the string s
        i = s.find(p)
        while i != -1:
            yield i
            i = secret_word.find(p, i + 1)

    find_all(lettere, secret_word)
    for i in find_all(lettere, secret_word):
        board[i] = lettere
    display_board()


def check_for_winner():
    global count_start
    global game_still_going
    global lettere
    if (not "_" in board) or (secret_word in board):
        game_still_going = False
        print("YOU WON")
        print(secret_word.upper())

    if len(wrong_letters) >= 7:
        game_still_going = False
        print("YOU LOST!")

play_game()

