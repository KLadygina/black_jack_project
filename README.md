# Blackjack Terminal Game 🎲🃏

A Python terminal-based Blackjack game where you play against the dealer to get as close to 21 as possible without going over. This project demonstrates basic Python programming skills like loops, conditionals, OOP, and input handling.

## Game Features
- Draw cards to increase your total score.
- Decide whether to "Hit" for more cards or "Stand" to hold your total.
- The dealer will automatically draw until they reach 17 or higher.
- The game follows standard Blackjack rules with face cards worth 10 and Aces worth 1 or 11.
- You can choose to play again after each round.

## Getting Started
### Prerequisites
- **Python 3.x** (version 3.7 or later) must be installed on your machine. You can download the latest version from python.org.

### How to Run the Game
1. Clone this repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/blackjack-terminal-game.git
    ```
2. Navigate to the project directory:
    ```bash
    cd blackjack-terminal-game
    ```
3. Run the game using Python:
    ```bash
    python blackjack.py
    ```

## Game Rules
- The goal is to get your hand value as close to 21 as possible without exceeding it.
- **Commands**:
    - `h` or `+` to Hit (draw a card)
    - `st` or `=` to Stand (end your turn)
    - `sur` or `-` to Surrender (quit the game)
- The dealer must hit until their total is 17 or higher.
- If either the player or dealer goes over 21, they lose the round.

## How It Works
- The game uses a deck of cards represented by a combination of card values and suits.
- Player and dealer hands are tracked, and the game dynamically updates their totals based on drawn cards.
- The game logic includes handling of Aces, which can count as either 1 or 11 depending on the player's hand.

## Future Improvements 
- Implement support for multiple players.
- Add the option to split or double down.
- Create a GUI version using libraries like Pygame.


