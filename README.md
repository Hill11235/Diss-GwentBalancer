# Dissertation - Gwent & Automated Balancer

Ethan Hill master's thesis
* Can play Gwent via the command line.
* Created a Monte Carlo tree search agent to play the game.
* Created a system which runs game simulations using said agent, generates data, and uses this data to adjust card strength. This process is then iterated a specified number of times.

Game Gwent based on CD Projekt Red's game of the same name in their 2015 game "The Witcher 3 - Wild Hunt". Game rules and description as per https://witcher.fandom.com/wiki/Gwent.

## Set up

Navigate to the directory this README is in. Then run one of the below set up code sections in your terminal to create a virtual environment, install the necessary packages, and set the path variable.

Set up for linux and macOS:\
`python3 -m venv envo`\
`source envo/bin/activate`\
`pip3 install pandas numpy matplotlib seaborn pyfiglet`\
`export PYTHONPATH="{PYTHONPATH}:/path/to/project/root/directory"]`

Set up for windows:\
`python3 -m venv envo`\
`source envo/bin/activate`\
`pip3 install pandas numpy matplotlib seaborn pyfiglet`\
`set PYTHONPATH=%PYTHONPATH%;C:\path\to\your\project\`

## Run instructions
After running the above set up code and with the virtual environment active, the below commands can be used to run the different processes from the root directory:

### Run full balancing process
Parameters such as the search time and number of iterations can be amended in the balance.py and simulation_cycle.py files.

`python3 balancing_system/balance.py`


### Run the playable command line version of Gwent

`python3 gwent/play_game.py`


### Run the random agent vs agents with varying time budgets

`python3 agent/agent_test.py`



Alternatively run via your favourite IDE. This project was written and run using PyCharm.

Have fun!