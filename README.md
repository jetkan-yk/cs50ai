# CS50's Introduction to Artificial Intelligence with Python

## ‼️ WARNING ‼️

This repository contains solutions to the CS50 AI projects. If you intend to take this course in the future, please read the [Academic Honesty policy](https://cs50.harvard.edu/ai/2020/honesty/) before viewing the solutions. This course has a [**zero-tolerance plagiarism policy**](https://discord.com/channels/393846237255696385/690359206716637184/829384296900853781).

## 🩺 Test Cases [![test](https://github.com/jetkan-yk/cs50ai/actions/workflows/main.yml/badge.svg?event=push)](https://github.com/jetkan-yk/cs50ai/actions/workflows/main.yml)

Each project contains a `test.py` and a `unit_test.py` file which I've written while solving the problem. Feel free to use it to test your own solutions! The `test.py` files are _spoiler-free_ (does not contain solution to the projects).

## 📖 Table of Contents

| Week                                           | Lecture                                      | Concept                                                                                      | Name                                           | Description                                                                                                                                       | Test Case                                                   |
| ---------------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [0](https://cs50.harvard.edu/ai/2020/weeks/0/) | [Search](https://youtu.be/WbzNRTTrX0g)       | [BFS](https://cs50.harvard.edu/ai/2020/notes/0/#breadth-first-search)                        | [Degrees](lec0/degrees/degrees.py)             | [Determine how many “degrees of separation” apart two actors are.](https://cs50.harvard.edu/ai/2020/projects/0/degrees/)                          | [degrees_test.py](lec0/degrees/degrees_test.py)             |
| [0](https://cs50.harvard.edu/ai/2020/weeks/0/) | [Search](https://youtu.be/WbzNRTTrX0g)       | [Minimax](https://cs50.harvard.edu/ai/2020/notes/0/#minimax)                                 | [Tic-Tac-Toe](lec0/tictactoe/tictactoe.py)     | [Implement an AI to play Tic-Tac-Toe optimally.](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/)                                          | [tictactoe_test.py](lec0/tictactoe/tictactoe_test.py)       |
| [1](https://cs50.harvard.edu/ai/2020/weeks/1/) | [Knowledge](https://youtu.be/HWQLez87vqM)    | [Model Checking](https://cs50.harvard.edu/ai/2020/notes/1/#inference)                        | [Knights](lec1/knights/puzzle.py)              | [Solve the "Knights and Knaves" puzzles using AI.](https://cs50.harvard.edu/ai/2020/projects/1/knights/)                                          | [puzzle_test.py](lec1/knights/puzzle_test.py)               |
| [1](https://cs50.harvard.edu/ai/2020/weeks/1/) | [Knowledge](https://youtu.be/HWQLez87vqM)    | [Knowledge Engineering](https://cs50.harvard.edu/ai/2020/notes/1/#knowledge-engineering)     | [Minesweeper](lec1/minesweeper/minesweeper.py) | [Implement an AI to play Minesweeper optimally.](https://cs50.harvard.edu/ai/2020/projects/1/minesweeper/)                                        | [minesweeper_test.py](lec1/minesweeper/minesweeper_test.py) |
| [2](https://cs50.harvard.edu/ai/2020/weeks/2/) | [Uncertainty](https://youtu.be/D8RRq3TbtHU)  | [Bayesian Networks](https://cs50.harvard.edu/ai/2020/notes/2/#bayesian-networks)             | [Heredity](lec2/heredity/heredity.py)          | [Write an AI to assess the likelihood that a person will have a particular genetic trait.](https://cs50.harvard.edu/ai/2020/projects/2/heredity/) | [heredity_test.py](lec2/heredity/heredity_test.py)          |
| [2](https://cs50.harvard.edu/ai/2020/weeks/2/) | [Uncertainty](https://youtu.be/D8RRq3TbtHU)  | [Markov Models](https://cs50.harvard.edu/ai/2020/notes/2/#markov-models)                     | [PageRank](lec2/pagerank/pagerank.py)          | [Write an AI to rank web pages by importance.](https://cs50.harvard.edu/ai/2020/projects/2/pagerank/)                                             | [pagerank_test.py](lec2/pagerank/pagerank_test.py)          |
| [3](https://cs50.harvard.edu/ai/2020/weeks/3/) | [Optimization](https://youtu.be/qK46ET1xk2A) | [Constraint Satisfaction](https://cs50.harvard.edu/ai/2020/notes/3/#constraint-satisfaction) | [Crossword](lec3/crossword/generate.py)        | [Write an AI to generate crossword puzzles.](https://cs50.harvard.edu/ai/2020/projects/3/crossword/)                                              | [generate_test.py](/lec3/crossword/generate_test.py)        |
| [4](https://cs50.harvard.edu/ai/2020/weeks/4/) | [Learning](https://youtu.be/-g0iJjnO2_w)     | [Notes](https://cs50.harvard.edu/ai/2020/notes/4/)                                           | [Shopping](lec4/shopping/shopping.py)          | [Write an AI to predict whether online shopping customers will complete a purchase.](https://cs50.harvard.edu/ai/2020/projects/4/shopping/)       | *Work in Progress*                                          |
| [4](https://cs50.harvard.edu/ai/2020/weeks/4/) | [Learning](https://youtu.be/-g0iJjnO2_w)     | [Reinforcement Learning](https://cs50.harvard.edu/ai/2020/notes/4/#reinforcement-learning)   | [Nim](lec4/nim/nim.py)                         | [Write an AI that teaches itself to play Nim through reinforcement learning.](https://cs50.harvard.edu/ai/2020/projects/4/nim/)                   | *Work in Progress*                                          |

## 🛠️ How to Run Tests

### Guide

1. Make sure you have [Python3](https://www.python.org/downloads/) installed in your machine. Anything above `Python 3.4` should work.
2. Install `pytest` by running `pip install pytest` in a terminal. More information about `pip` [here](https://realpython.com/what-is-pip/).
3. Make a copy of the test file and paste it in the **same folder** as the project that you want to test.
    > For example, if you want to test your code for `degrees.py`, make a copy of `degrees_test.py` in the **same folder** as your `degrees.py` and other files that came along with the project, like `util.py`, `large/` and `small/`.
4. Navigate to the project folder and run `pytest` or `pytest <project>_test.py` in a terminal.
    > For example, navigate to `degrees/` and run `pytest` or `pytest degrees_test.py`.

### Example

![example](https://user-images.githubusercontent.com/36299141/128583985-a56b4371-a092-430a-8c08-4483137367d6.png)

## 🚩 Useful pytest Flags

- Run `pytest -s` to show print statements in the console
- Run `pytest -vv` for verbose mode
- Combine both flags `pytest -s -vv` for extra verbose mode
- Run `pytest --durations=n` to see the `n` slowest execution time
- Install `pytest-repeat` with `pip` and then run `pytest --count n` to repeat the test for *n* times

## 🤹 Improvement

I am currently auditing this course (no certificate bearing, just interested in AI and Brian's teaching style), more solutions and test cases will be added in the near future!</br>

This is a self-initiated project. Passing these test cases **does not** guarantee that you will also receive a full grade from the HavardX teaching team.</br>

If you notice any error in the test cases, or even better, would like to contribute to this repository, please create a new issue [here](https://github.com/jetkan-yk/cs50ai/issues). I would greatly appreciate any constructive feedback regarding my code too! ♥️

## 💻 My Setup

Each test case should take less than 30 seconds, depending on Python's I/O and your code efficiency.

- Windows 10 Home Build 19042
- Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
- Python 3.9.5 64-bit
- Visual Studio Code w/Pylance (latest release)
- Code formatter: black

## 🏛️ License

Retrieved from <https://cs50.harvard.edu/ai/2020/license/>

![license](https://user-images.githubusercontent.com/36299141/128539744-ee267826-82fb-4fd2-831b-9d40413be9dc.png)
