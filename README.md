# pygame-asteroids

An Asteroids-style arcade game built with **Python** and **Pygame** as part of the [Boot.dev](https://www.boot.dev) game development curriculum.

Right now, this project is in the early stages: I’ve set up Pygame, created a window, and implemented a basic game loop that logs game state and draws a black screen.

---

## Features (Current Progress)

- Initializes Pygame and creates a window using preset `SCREEN_WIDTH` and `SCREEN_HEIGHT` constants.
- Basic game loop that:
  - Logs game state to `game_state.jsonl` using `log_state()`.
  - Fills the screen with black each frame.
  - Uses `pygame.display.flip()` to update the display.
  - Handles the window close event so the game exits cleanly.

More features (player, asteroids, collisions, scoring, etc.) will be added as I continue the Boot.dev course.

---

## Tech Stack

- Python 3
- [Pygame](https://www.pygame.org/)
- Project structure and assignments from [Boot.dev](https://www.boot.dev)

---

## Setup and Run

Clone the repository and install dependencies (using `uv` as in the course):

```bash
uv run main.py
```

This will open the game window and start the game loop. Close the window or press `Ctrl+C` in the terminal to stop.

# About Boot.dev
This project is part of the Boot.dev curriculum, which teaches backend development and Python through hands-on coding challenges and text-based lessons rather than videos.

If you want to learn by building real projects (like this game), check them out at Boot.dev.

```


          .       .        *        .       .
   .        .         .         .       .       *
        .        .       .        .        .
             *        .       .        .    

        ____        _                 _     
       / __ \      | |               | |    
      | |  | |_   _| |_ ___  _ __ ___| |__  
      | |  | | | | | __/ _ \| '__/ __| '_ \ 
      | |__| | |_| | || (_) | | | (__| | | |
       \___\_\\__,_|\__\___/|_|  \___|_| |_|
                                           
          ASTEROIDS • PYTHON • PYGAME
              Crafted with Boot.dev

```