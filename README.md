# 🐍 Snake AI Direction Problem — Toroidal Grid

This is a minimal toy problem inspired by the classic Snake game.  
You are given a function signature and must implement logic to guide a snake toward a fruit while avoiding collisions — all within a **wrapped (toroidal)** grid.

## 🧠 Your Task

Implement the function:

```python
def best_snake_dir(your_snake, other_snake, fruit, horizontal_cells, vertical_cells) -> str:
```
Return the best direction for your snake to move: `'U'`, `'D'`, `'L'`, or `'R'`.

## 📜 Rules

- The game is played on a grid of size `HORIZONTAL_CELLS × VERTICAL_CELLS`.
- The grid **wraps around**: moving off one edge brings the snake to the opposite side (like Pac-Man).
- The function should return one of the four directions: `'U'` (up), `'D'` (down), `'L'` (left), or `'R'` (right).
- Avoid any collision with:
  - Your own snake's body
  - The other snake's body
- Choose a direction that brings the snake closer to the fruit using the shortest wrapped (toroidal) path.

## 🗂 Files

- `answer.py`: Contains the function signature and problem description
- `main.py`: (Optional) You can add custom test cases here, a default gameplay is already set

## 🚀 Contribute

This repository contains only the problem — no solution is provided.

Feel free to:
- Fork the repo and implement your own version of the function.
- Extend it with your own features (AI logic, animations, etc.).
- Share it with others as a coding challenge.

Pull requests are welcome if you’d like to contribute improvements or variations of the problem!
