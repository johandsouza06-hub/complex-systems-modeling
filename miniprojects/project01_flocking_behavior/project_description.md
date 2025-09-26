# Mini-Project 1: Flocking Behavior

## Overview
In this project, you'll implement the famous "Boids" model created by Craig Reynolds in 1986. This model shows how simple local rules for individual agents can create complex flocking behavior similar to birds, fish, or other group-moving animals.

## Learning Objectives
- Implement agent-based modeling
- Understand emergence in collective behavior
- Practice object-oriented programming
- Create interactive visualizations
- Analyze parameter sensitivity

## The Three Rules of Flocking

Each "boid" (bird-like object) follows three simple rules:

1. **Separation**: Steer to avoid crowding local flockmates
2. **Alignment**: Steer towards the average heading of neighbors  
3. **Cohesion**: Steer to move toward the average position of neighbors

## Implementation Tasks

### Part 1: Basic Boid Class (25 points)
Create a `Boid` class with:
- Position (x, y)
- Velocity (vx, vy)
- Methods for updating position and velocity

### Part 2: Flocking Rules (40 points)
Implement the three flocking behaviors:
- `separate()`: Avoid nearby boids
- `align()`: Match velocity of neighbors
- `cohesion()`: Move toward center of neighbors

### Part 3: Simulation Loop (20 points)
Create the main simulation that:
- Updates all boids each time step
- Handles boundary conditions
- Visualizes the flock movement

### Part 4: Analysis (15 points)
Investigate how parameters affect behavior:
- Number of boids
- Neighborhood radius
- Strength of each rule
- Speed limits

## Deliverables

1. **Working Code** (60%): Complete Boids implementation
2. **Visualization** (20%): Clear, informative plots/animations
3. **Analysis** (15%): Parameter study with insights
4. **Documentation** (5%): Clear code comments and explanations

## Getting Started

Use the provided template notebook: `flocking_starter_template.ipynb`

## Resources
- Original paper: Reynolds, C. (1987). "Flocks, herds and schools"
- Online demos: [boids.org](http://boids.org)
- Course materials on agent-based modeling

## Due Date
[Insert due date]

## Grading Rubric
See `grading_rubric.md` for detailed assessment criteria.
