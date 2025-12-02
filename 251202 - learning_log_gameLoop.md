# Notes from Building My First Pygame Game Loop (Boot.dev Asteroids)

While working through Boot.dev’s Asteroids project up to Chapter 2 – Lesson 3: Game Loop, I learned a series of foundational concepts about Python, Pygame, Git, and basic project workflow. This is a structured summary of what I practiced and struggled with along the way.

# 1. Initializing Pygame
Before using any Pygame functionality, I need to:

```
import pygame

pygame.init()
``

Key points:

- `import pygame` loads the Pygame library.
- `pygame.init()` initializes all the modules Pygame needs (display, audio, etc.).
- If initialization fails, the program will throw an error when I run it (e.g., with `uv run main.py`).

I also learned that some warnings (like ALSA audio warnings on Linux) can appear in the terminal but aren’t fatal errors; as long as the program runs and no Python traceback appears, Pygame is generally fine.

# 2. Using Constants for Screen Size

The project uses a constants.py module to store screen dimensions:

```
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
```

Lessons:

- Keeping configuration values (like screen size) in a separate file improves clarity and consistency.
- These constants are used to set up the display window.

# 3. Creating the Game Window with `pygame.display.set_mode`

Pygame exposes the display functionality as a submodule on the main pygame module:

- display is accessed as pygame.display, not imported separately.
- The window is created via:

```
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
```

Important details:

- `pygame.display.set_mode` expects a tuple `(width, height)` as a single argument.
- I use the constants I imported to avoid magic numbers.
- The returned `screen` is a `Surface` object that I draw on later.

Understanding that `display` is a submodule (`pygame.display`) and `set_mode` is a function on it was a new conceptual step.

# 4. Structuring main() and the Entry Point

The project follows a common Python pattern:

```
def main():
    # game setup
    # game loop

if __name__ == "__main__":
    main()
```

Key ideas:

- `main()` contains the game logic: initialization, window creation, and the game loop.
- The `if __name__ == "__main__":` guard ensures the game only runs when the file is executed directly, not when imported as a module.

I also moved `pygame.init()` and `pygame.display.set_mode` inside `main()` for better structure and to match the project’s expectations.

# 5. Building the Infinite Game Loop

The core of every real-time game is the game loop. For this lesson, I built a minimal loop that:

1. Logs game state.
2. Handles the quit event.
3. Draws a black screen.
4. Updates the display.

The basic loop looks like this:

```
while True:
    log_state()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    screen.fill("black")
    pygame.display.flip()
```

Concepts I solidified:

- **Infinite loop**: use `while True:` instead of trying to simulate infinity with counters like `while number > 0`.
- The loop runs many times per second, representing “frames” of the game.
- Ordering matters:
    - `log_state()` first (so each frame is recorded),
    - then event handling,
    - then drawing (`screen.fill("black")`),
    - then display update (`pygame.display.flip()`).

# 6. Event Handling and Exiting Cleanly

Without event handling, the window might open but not respond properly to the close button.

The pattern I used:

```
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return
```

Key lessons:

- `pygame.event.get()` fetches the current events (like key presses, mouse actions, window actions).
- Checking for `pygame.QUIT` lets the game exit the loop and return from `main()`, closing cleanly.
- The `return` exits `main()`; since the script ends after that, the program terminates.

# 7. Drawing and Updating the Screen

To “draw the game” (even if it’s just a black background at first):

```
screen.fill("black")
pygame.display.flip()
```

Notes:

- `screen.fill("black")` fills the entire surface with a solid color. The color can be a string like `"black"` or an RGB tuple (e.g., `(0, 0, 0)`).
- Pygame treats unquoted `black` as a variable name, which would cause an error. Using `"black"` (a string) is correct.
- `pygame.display.flip()` swaps the buffers and shows the latest drawing on the actual window. It must be called at the end of each frame.

This is step 3 of the typical game loop: **draw the game to the screen**.

# 8. Logging Game State with `log_state()`

The project includes a custom `log_state()` function imported from `logger.py`:

```
from logger import log_state
```

In the loop:

```
log_state()
```

Key ideas:

- `log_state()` (no arguments) records the current game state to a file called `game_state.jsonl`.
- Running the game loop for a while generates multiple JSON lines. These logs are then used by automated tests.
- For the tests to pass, I need to:
    - call `log_state()` every frame,
    - run the game long enough to generate entries,
    - ensure `game_state.jsonl` is non-empty.

The tests read from `game_state.jsonl` to verify that the logged `screen_size` matches `SCREEN_WIDTH` and `SCREEN_HEIGHT`.


# 9. Running and Testing the Game

To run the game locally (using `uv`, as set up by the project):

```
uv run main.py
```

Observations:

- Pygame prints a banner with its version.
- My own `print` statements (when present) show up in the terminal.
- A window opens and stays open, filled with black, until I close it or press `Ctrl+C` in the terminal.

To run the Boot.dev lesson tests:

```
bootdev run e54942c0-0333-41bb-892f-e8a3049018df -s
```

The important part is that the game must be run first so that `game_state.jsonl` is populated; otherwise, the tests won’t find the expected data.

# 10. Basic Git and GitHub Workflow

Alongside the code, I practiced basic Git operations:

- Check status:

    ```
    git status
    ```

- Stage changes:

    ```
    git add main.py
    # or all changes:
    git add .
    ```

- Commit with a message:

    ```
    git commit -m "Add basic pygame init and game loop"
    ```

- Push to GitHub:

    - Initially, my branch was named `master`, but I wanted `main`:

        ```
        git branch -m master main
        ```

    - Then push and set upstream:

        ```
        git push -u origin main
        ```

Concepts reinforced:

- `origin` is the default remote name pointing to the GitHub repository.
- The local branch name (`main` or `master`) must match what I push: `git push origin main`.

# 11. Project Metadata: README and License

To make the repository presentable and shareable, I added:

- A *README* describing:
    - The project (`pygame-asteroids`),
    - Current features (basic game loop, logging, black screen),
    - Tech stack (Python, Pygame, Boot.dev),
    - How to run the game.

- An *MIT License* in a `LICENSE` file, granting users permission to use, modify, and distribute the code.

This is part of treating even learning projects like real software projects.

# 12. Big Picture: What I Actually Learned

From Chapter 1 through Chapter 2, Lesson 3, the main takeaways are:

- How to *initialize* and use Pygame.
- How to create a window with `pygame.display.set_mode`.
- How to structure a Python program with a `main()` function and an `if __name__ == "__main__":` guard.
- How to implement a basic *game loop*:
    - handling input/events,
    - updating/logging state,
    - drawing and flipping the display.
- How to use a logging function (`log_state`) to record game state to a JSON lines file.
- How to run local tests and interpret their failures based on output.
- How to manage branches, commits, and pushes in Git/GitHub.

All of this forms the foundation for more advanced features in the Asteroids game: movement, collisions, scoring, and beyond.


