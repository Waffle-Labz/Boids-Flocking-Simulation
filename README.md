# Boids Flocking Simulation

<img width="969" height="969" alt="image" src="https://github.com/user-attachments/assets/8823fdf1-6cf3-406a-82d5-077d1cc111a1" />

A 2D flocking simulation built with Python and Pygame, demonstrating how complex group behaviour can emerge from a small set of simple rules.

Boids move independently while responding to nearby boids and obstacles, producing flocking patterns without a central controller.

## Features

- **Cohesion:** Boids steer towards the average position of nearby flockmates.
- **Separation:** Boids steer away from nearby flockmates to avoid overcrowding.
- **Alignment:** Boids adjust their velocity towards the average velocity of nearby flockmates.
- **Obstacle avoidance:** Boids steer away from obstacles in their path.
- **Screen wrapping:** Boids reappear on the opposite edge when leaving the simulation area.
- **Speed-based colouring:** Boid colours are interpolated between configurable minimum and maximum colours according to their speed.
- **Configurable parameters:** Flocking strengths, perception radii, speed limits, and obstacle avoidance settings can be adjusted centrally.

## Requirements

- Python 3
- Pygame

## How It Works

Each boid maintains its own position, velocity, and acceleration. During each update, it responds to three flocking rules:

1. **Cohesion** encourages boids to move towards their neighbours.
2. **Separation** encourages boids to maintain distance from one another.
3. **Alignment** encourages boids to travel in similar directions.

The combined effects of these local interactions produce emergent flocking behaviour. Obstacle avoidance adds another steering behaviour, allowing boids to navigate around obstacles while continuing to interact with the flock.

The simulation uses configurable perception radii to determine which neighbours influence each boid. Speed-based colour interpolation provides a visual indication of movement speed.

## Configuration

Simulation parameters are defined in `config.py`, including:

- Minimum and maximum boid speeds
- Boid size
- Perception radii for each flocking rule
- Cohesion, separation, and alignment strengths
- Obstacle avoidance radius and strength
- Minimum and maximum boid colours
- Simulation dimensions

Adjusting these values changes the resulting flocking patterns and movement behaviour.

## Project Structure

```text
boids-flocking-simulation/
├── main.py
├── boid.py
├── rules.py
├── obstacle.py
├── config.py
└── README.md
```

## Technologies

- Python
- Pygame

## Possible Future Improvements

- Predictive obstacle avoidance
- Interactive controls for adding boids and obstacles
- Frame-rate-independent movement
- Performance optimisation for larger flocks
- Visualisation of perception radii and steering forces
