# Monty Hall Simulator

## The Problem: 
Imagine being on a game show. In front of you there are 3 doors. Behind one of the doors is a prize - the remaining doors have nothing behind them.

You choose a door. Before revealing the results, the host opens all remaining doors except one. There are now 2 doors left: your door, and the host's final door.

The host asks you if you want to switch your choice. Is it more likely that the prize is behind your door, or behind the door the host left closed?

The answer is surprising - it is better to switch!

Let's say there are 3 doors. When you make your choice, you have a 1/3 chance of picking correctly and a 2/3 chance of picking incorrectly. When the host cuts down the other doors, it feels natural that we would say that there are now 2 doors left, so the chance is 50/50. That is incorrect - if we do that, we neglect a key fact: by removing doors that are guaranteed to lose - we are essentially given new infomation during the game. That 2/3 chance we started with does not go away - it stays in the host's door. Since it was 2/3 chance that the winning door was not your door, it now makes sense to switch.

Numberphile has a great video explaining in more detail:

https://www.youtube.com/watch?v=4Lb-6rxZxx0

I first discovered the problem in S4E8 of Brooklyn 99, and wanted to simulate it. This is the result!

## Usage
Written using Python 3.10

All code is contained in one script, which is just driver.py

A few main dependencies, specified in the imports at the beginning of the script:
1. random : to generate board configurations and simulate picking a door
2. argparse : to configure cli argument options
3. math : to get the floor function for printing out progress
4. decimal : to handle floating point division when calculating win/loss ratio

To run the script:
- Open terminal window
- Navigate to the directory where the script resides
- If you want the simulation to stick with the first door choice, run command `python driver.py`
- If you want the simulation to swap the door choice, run command `python driver.py -s`

Now, you will be prompted for input via console/command line.
First, you will need to specify how many doors are in the game. Input must be an integer.
Next, you will need to specify how many times the game is simulated. Input, again, must be an integer. The more simulations - the more the ratio tends to flatten out.

At this point, the simulation will begin. You will see the console start counting up from 1. When it hits 10, the simulation is done. This is just a way to provide feedback to the user. Without feedback, it is impossible to know whether the script is working until it is terminates.

When the simulation is complete, the results will be output to console in a summarized view.

As an alternative to console input - you can also run with command line arguments:
`python driver.py --help` for options

We already saw the `-s` flag is used to tell whether we want to simulate swapping or not

The other main options are:
- `-d, --doors, for doors. Number of doors in the game`
- `-c, --count, for count. Number of times the game is simulated`

For example:

`python driver.py -d3 -c1000` will run the simulation 1000 times, where each game has 3 doors. The user will not swap. In this case, we see the win to loss ratio hovering around 1 in 3.

```
python driver.py -d3 -c1000
Progress:
1 2 3 4 5 6 7 8 9 Done!

Summary:
Runs: 1000
Wins: 333
Losses: 667
Ratio: 0.333 (33.300%)
```

`python driver.py -d3 -c1000 -s` will run the simulation 1000 times, where each game has 3 doors. The user will swap. In this case, we see the win to loss ratio hovering around 2 in 3.
```
python driver.py -d3 -c1000 -s
Progress:
1 2 3 4 5 6 7 8 9 Done! 

Summary:
Runs: 1000
Wins: 675
Losses: 325
Ratio: 0.675 (67.500%)
```

