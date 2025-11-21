# Rock, Paper, Scissors Game 🎮

A simple and fun Rock, Paper, Scissors game implemented in Python. This project is designed for practicing object-oriented programming and game state management.

## 📖 About the Game

Rock, Paper, Scissors is a classic game where you compete against the computer. The first one to reach 3 points wins the game!

### Game Rules:
- **Rock** beats **Scissors** ✊
- **Scissors** beats **Paper** ✌️  
- **Paper** beats **Rock** ✋

## 🚀 Features

- **Player vs Computer** gameplay
- **Score tracking** until 3 points
- **Play again** option without restarting
- **Input validation** for user choices
- **Clean console interface**
- **Object-oriented design**

## 🛠️ Installation & Usage

### Prerequisites

- Python 3.6 or higher

### How to Run

1. Clone or download the project files
2. Navigate to the project directory
3. Run the game:

```bash
python game.py
```

## How to Play

- Run the script
- Enter your choice: rock, paper, or scissors
- See the computer's choice and who wins
- First to 3 points wins the round
- Choose to play again or quit

## 🎯 Game Structure

### Main Components:

- Game Class: Manages game state and logic
- Score Tracking: Keeps track of player and computer scores
- Input Handling: Validates user input
- Winner Determination: Applies game rules to determine winner

### Key Methods:

- pc_choice(): Generates computer's random choice
- user_choice(): Gets and validates user input
- decide_winner(): Determines round winner based on game rules
- play(): Manages single game session
- reset_scores(): Resets scores for new game

### 💡 Example Gameplay
```
-----------------------------------------
Rock, Paper, Scissors
Enter your choice: rock
user rock, pc scissors
user 1, pc 0

-----------------------------------------
Rock, Paper, Scissors
Enter your choice: paper
user paper, pc rock
user 2, pc 0

... continues until one player reaches 3 points
```