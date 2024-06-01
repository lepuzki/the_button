# The Button Game Simulation

Welcome to the Button Game Simulation! This project simulates a button-clicking game where each button press gives you 1 point, but with each press, the probability of losing all points increases by 1%. The simulation continuously runs and displays real-time statistics including the total number of tries, maximum points achieved, and tries per minute.

(simulates this game basically https://store.steampowered.com/app/1999740/THE_BUTTON_by_Elendow/)

## Features

- **Real-time Statistics**: Displays total tries, max points, and tries per minute.
- **Human-readable Format**: Choose between human-readable (e.g., 1.2K) and comma-separated (e.g., 1,234) number formats.
- **Interactive Control**: Press `q` to exit the simulation at any time.
- **Keyboard Interrupt Handling**: Gracefully handles keyboard interrupts (`Ctrl+C`).

## Requirements

- Python 3.x
- `colorama` for colored console output
- `keyboard` for key press detection

You can install the required packages using:
```
pip install colorama keyboard
```

# Usage

Clone the Repository:

```
git clone https://github.com/yourusername/button-game-simulation.git
```
Navigate to the project folder:
```
cd button-game-simulation
```
Run the Simulation:
```
python main.py
```
