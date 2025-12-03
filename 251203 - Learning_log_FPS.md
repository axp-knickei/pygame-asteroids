# Learning Log: Controlling FPS and Delta Time in Pygame

In this lesson, I learned how to control the frame rate of a Pygame application and how to work with *delta time* to make movement frame-rate independent.

## 1. Game Loop and Frame Rate
- A Pygame program typically runs in a `while True` loop, often called the game loop.
- Without any control, the loop runs as fast as the computer allows, which:
    - Wastes CPU.
    - Makes game speed depend on hardware performance.
- To create a stable experience, I need to limit how often each frame is updated and drawn. This is where FPS (frames per second) comes in.

## 2. Using `pygame.time.Clock`
- After calling `pygame.init()` and before starting the game loop, I created a clock object:

```
clock = pygame.time.Clock()
```

- The `Clock` object is responsible for:

    - Regulating the loop to a target FPS.
    - Measuring how much time passed between frames.
- It’s important to store the `Clock` in a variable (`clock`) so I can use it inside the loop. Calling `pygame.time.Clock()` without saving the result would make it impossible to use later.

## 3. Limiting the FPS with `.tick(60)`
- At the end of each iteration of the game loop, I called:

```
clock.tick(60)
```

- This does two important things:

    1. Pauses the loop just enough to target **60 FPS**.
    2. Returns the time (in milliseconds) that has passed since the last call to `.tick()`.
- Placing `.tick(60)` at the end of the loop makes sense because one full iteration represents one frame. I want each frame to be regulated to approximately 1/60th of a second.

## 4. Delta Time (`dt`)
- I introduced a `dt` (delta time) variable, initialized before the loop:

```
dt = 0
```

- Inside the game loop, I updated `dt` using the return value of `.tick(60)`:

```
dt = clock.tick(60) / 1000
```

- Key points:

    - `.tick(60)` returns elapsed time in **milliseconds**.
    - Dividing by `1000` converts milliseconds to seconds.
    - `dt` now represents “how much time passed since the last frame,” in seconds.

## 5. Why Delta Time Matters
- Game movement should depend on time, not on how fast frames are drawn.

- With dt, I can express movement like this:

```
position_x += speed * dt
```

- Here:

    - `speed` is in “units per second” (for example, pixels per second).
    - `dt` is the fraction of a second that passed since the last frame.
    - The product `speed * dt` gives the correct distance to move this frame.

-As a result:

    - If the game briefly slows down and a frame takes longer, `dt` is larger, and the object moves farther that frame to compensate.
    - If the game runs faster and frames are quick, `dt` is smaller, and the object moves less per frame.
    - Overall movement per real-world second stays consistent.

## 6. Temporary Debugging with `print(dt)`
- As part of the lesson, I printed `dt` each frame to observe how it changed:

```
print(dt)
```

- This showed that `dt` is not constant; it can fluctuate slightly as the CPU workload changes.

- After confirming that it worked, I removed the print statement to avoid cluttering the console.

---
## Summary
In this lesson, I:

- Set up a `pygame.time.Clock` to regulate the game loop.
- Used `.tick(60)` at the end of the loop to target 60 FPS.
- Captured the elapsed time between frames as `dt` and converted it from milliseconds to seconds.
- Understood that `dt` is essential for time-based (rather than frame-based) movement, keeping gameplay consistent across different machines.

This was my first exposure to the concepts of frame rate control and delta time in game development with Python and Pygame, and it forms the foundation for smooth and predictable game behavior.