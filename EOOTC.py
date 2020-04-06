from random import choice, randint, shuffle


"""
Used to run.
"""
def main():
    print("Welcome to Countdown!")
    print("")
    user_reply = input("Auto-generate numbers? [Y]/[N]: ")
    
    if ((user_reply == "Y") or (user_reply == "y")):
        numbers = auto_generate_numbers()
    else:
        numbers = generate_numbers()
    
    goal = generate_goal()
    answer = generate_answers(goal, numbers)


"""
Picks which numbers to select.
"""
def generate_numbers():
    small_numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    large_numbers = [25, 50, 75, 100]
    tiles = []

    while len(tiles) < 6:
        input_num = input("Small or large number? [S]/[L]: ")
        
        if ((input_num == "S") or (input_num == "s")):
            rand_s_int = choice(small_numbers)
            print(f'The number is: {rand_s_int}')
            tiles.append(rand_s_int)
            small_numbers.remove(rand_s_int)
            print(f'Remaining small numbers left: {small_numbers}')
            
        elif ((input_num == "L") or (input_num == "l")):
            if not large_numbers:
                print("There are no more large numbers!")
                print("")
                continue
            rand_l_int = choice(large_numbers)
            print(f'The number is: {rand_l_int}')
            tiles.append(rand_l_int)
            large_numbers.remove(rand_l_int)
            print(f'Remaining large numbers left: {large_numbers}')
            
        else:
            print("Incorrect statement.")
            print("")
            continue
            
        if (len(tiles) != 6):
            print(f'Tiles so far: {tiles}')
        print("")

    print(f'Final six tiles: {tiles}')
    return tiles


"""
Auto-generate the numbers.
"""
def auto_generate_numbers():
    small_numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    large_numbers = [25, 50, 75, 100]
    tiles = []

    while len(tiles) < 6:
        small_or_large = randint(1, 2)
        print(small_or_large)
        if (small_or_large == 1) or (large_numbers):
            rand_s_int = choice(small_numbers)
            tiles.append(rand_s_int)
            small_numbers.remove(rand_s_int)
        else:
            rand_l_int = choice(large_numbers)
            tiles.append(rand_l_int)
            large_numbers.remove(rand_l_int)
        print(tiles)

    print(f'Final six tiles: {tiles}')
    return tiles


"""
Helper function to generate a goal.
"""
def generate_goal():
    goal = randint(0, 999)
    print("")
    print(f'The goal is: {goal}')
    return goal


"""
Generates an answer.
"""
def generate_answers(goal, numbers):
    answers = []

    nums_summed = 0
    nums_multi = 0

    count = 20

    while count != 20:
        shuffle(numbers)
        print(f'numbers = {numbers}')
        for num in numbers:
            print(f'num = {num}')
            nums_summed += num
            nums_multi *= num
        
        
        
     
    if (len(answers) == 0):
        print("I didn't find any solutions!")
    else:
        for answer in answers:
            if (c == 0) and (len(answers) < 1):
                print("I found multiple solutions.")
            elif (c == 0) and (len(answers) == 1):
                print("I only found one solution.")

    print("")
    user_reply = input("Try again? [Y]/[N]: ")
    if ((user_reply == "Y") or (user_reply == "y")):
        main()
    else:
        print("Goodbye!")
            

main()
