# Infinite Monkey Theorem Simulator

This project implements a basic simulation of the **Infinite Monkey Theorem**, where a monkey randomly types characters to match a user-provided sentence. The simulation demonstrates how randomness and probability can be used to eventually approximate a target string over repeated trials.

## Overview

The Infinite Monkey Theorem suggests that a monkey hitting keys at random on a typewriter for an infinite amount of time will almost surely type any given text. This Python-based implementation models that behavior in a constrained and finite way by generating random strings and checking their similarity to the target string.

## Features

- Accepts a user-defined sentence to match.
- Randomly generates strings of the same length using lowercase alphabets and spaces.
- Compares the generated string to the target string using a scoring system.
- Tracks and updates the best score over time.
- Allows user to continue or stop after every 10,000 unsuccessful attempts.

## How It Works

1. **Input**: User provides a target string.
2. **Generation**: The program generates random strings of the same length using the characters a–z and space.
3. **Scoring**: Each generated string is compared character-by-character to the target string. A percentage score is calculated based on matching characters.
4. **Termination**:
   - If a perfect match (100%) is found, the simulation stops.
   - After every 10,000 generations without a perfect match, the user is prompted to continue or terminate the simulation.

## Classes and Methods

### `Monkey`

#### Attributes:
- `best`: Tracks the highest score achieved so far.
- `sen`: The target sentence provided by the user.

#### Methods:
- `sentence_input()`: Prompts the user to enter the target string.
- `generate()`: Generates a random string of equal length and evaluates its score.
- `match(gen)`: Compares generated string with the target. Stops if a match is found.
- `score(gen)`: Calculates and returns the match score.
- `best_score_update(gen)`: Updates the highest score if the current generation is better.

## Use Cases

This project can serve as:
- A basic example of genetic algorithm principles (random generation, fitness evaluation).
- A demonstration of probability and random search.
- An engaging teaching tool for programming, randomness, or simulations.

## Limitations

- Only works with lowercase alphabets and spaces.
- Highly inefficient for long strings due to the combinatorial explosion in possible string permutations.
- No memory or evolution logic; each generation is entirely random and independent.

This project is intended for educational and experimental purposes only.
