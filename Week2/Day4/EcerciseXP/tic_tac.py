print("Welcome to TIC TAC TOE!")

def display_board(*args):
        print("TIC TAC TOE")
        print("*"*15)
        print(f"*  {display["one"]} |   |    *")
        print(f"* ---|---|--- *")
        print(f"*  {display["four"]} |   |    *")
        print(f"* ---|---|--- *")
        print(f"*    |   |    *")
        print(f"*"*15)


display = {"one":   [1,1],   "two":   [1,2], "three": [1,3],
                 "four":  [2,1], "five":  [2,2], "six":   [2,3],
                 "seven": [3,1], "eight": [3,2], "nine":  [3,3]}
player = True
# X id odd
# O id even

row = 0
column = 0
def player_input(row, column):
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    game(row, column)

def game(row, column):

        if (display["one"][0] == row) and (display["one"][1] == column):
            display.update({"one": "X"})
            display_board(display["one"])
        elif (display["four"][0] == row) and (display["four"][1] == column):
            display.update({"four": "X"})
            display_board(display["four"])


player_input(row, column)


print("    0   1   2")
print("")
print("0   {board['00']['value']} | {board['10']['value']} | {board['20']['value']} ")
print("   -----------")
print("1   {board['01']['value']} | {board['11']['value']} | {board['21']['value']} ")
print("   -----------")
print("2   {board['02']['value']} | {board['12']['value']} | {board['22']['value']} ")
print("")
