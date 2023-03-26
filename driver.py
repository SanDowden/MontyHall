import random
import argparse
import math
from decimal import Decimal

def generate_doors(number_of_doors: int) -> list[bool]:
    '''
    Generates a list of given length. One random element is true, the rest are false. 
    Simulation a game show where we have a collection of doors - one has a prize and the rest are empty.
    '''
    # pick the winning door at random
    winning_door: int = random.randint(0, (number_of_doors-1))
    # generate list of doors where True = win, False = lose
    door_list: list[bool] = []
    for i in range(number_of_doors):
        if i != winning_door:
            door_list.append(False)
        else:
            door_list.append(True)
    return door_list

def get_numeric_input(message: str) -> int:
    '''
    Get valid Integer from console user input
    '''
    # leave as None until valid int is given
    val: int = None
    while(val == None):
        try:
            # try to get input
            val = int(input(message + "\r\n"))
        except Exception as ex:
            # if it can't be converted to int, message user and start loop again
            print("Not a valid number. Try again!")
    return val

def play(doors: list[bool], swap: bool) -> bool:
        # player makes choice
        choice: int = random.randint(0, (num_doors-1))
        # host removes doors until 2 are left
        if doors[choice]:
            # if the player originally picked correctly, then the door picked by the host will be a losing door
            # stay = win, swap = loss
            doors = [True, False]
        else:
            # if the player originally picked incorrectly, then the door picked by the host will be the winning door
            # stay = loss, swap = win
            doors = [False, True]

        if not swap:
            return doors[0]
        else:
            return doors[1]
        
        
if __name__ == "__main__":
    # configure command line argument parser for the option of running directly via cmd arguments
    arg_parser = argparse.ArgumentParser(description="Simulate the Monty Hall game show problem")
    arg_parser.add_argument("-d", "--doors", type=int, help="Number of doors in the game")
    arg_parser.add_argument("-c", "--count", type=int, help="Number of times the game is simulated")
    arg_parser.add_argument("-s", "--swap", action='store_true', help="If present, the player will swap")
    args, remaining = arg_parser.parse_known_args()

    num_doors: int = args.doors
    num_runs: int = args.count
    swap: bool = args.swap

    # if no cmd args were passed, get from user console input
    if num_doors == None:
        num_doors: int = get_numeric_input("How many doors?")
    if num_runs == None:
        num_runs: int = get_numeric_input("How many times should the game be simulated?")
    
    wins: int = 0

    interval: int = math.floor(num_runs / 10)
    pct: int = 1
    print("Progress:")
    for i in range(num_runs):
        if i != 0 and i % interval == 0:
            print(pct, end=" ", flush=True)
            pct += 1
        doors: list[bool] = generate_doors(num_doors)
        if play(doors, swap):
            wins += 1
    print("Done! \r\n")

    losses: int = num_runs - wins

    ratio: Decimal = Decimal(wins) / Decimal(num_runs)
    ratio_pct: Decimal = Decimal(ratio) * Decimal(100)

    print("Summary:")
    print(f"Runs: {num_runs}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Ratio: {ratio} ({ratio_pct}%)")
        
