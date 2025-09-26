#!/usr/bin/env python3
"""
Repository Setup Script for Complex Systems Modeling Course
This script creates the complete directory structure and essential files.
"""

import os
import json
from pathlib import Path

def create_directory_structure():
    """Create the complete directory structure for the course repository."""
    
    directories = [
        # Main directories
        "lectures",
        "notebooks", 
        "exercises",
        "miniprojects",
        "resources",
        "data",
        "tools",
        "assessments",
        
        # Lecture subdirectories
        "lectures/week01_introduction",
        "lectures/week02_emergence", 
        "lectures/week03_cellular_automata",
        "lectures/week04_agent_based",
        "lectures/week05_networks",
        
        # Notebook subdirectories
        "notebooks/session01_intro_python",
        "notebooks/session01_intro_python/solutions",
        "notebooks/session02_chaos_game",
        "notebooks/session02_chaos_game/solutions",
        "notebooks/session03_cellular_automata",
        "notebooks/session03_cellular_automata/solutions",
        "notebooks/session04_agent_based",
        "notebooks/session04_agent_based/solutions",
        "notebooks/session05_networks",
        "notebooks/session05_networks/solutions",
        
        # Exercise subdirectories
        "exercises/week01_basic_patterns",
        "exercises/week01_basic_patterns/solutions",
        "exercises/week02_fractals",
        "exercises/week02_fractals/solutions",
        "exercises/week03_cellular_automata",
        "exercises/week03_cellular_automata/solutions",
        "exercises/week04_agents",
        "exercises/week04_agents/solutions",
        "exercises/week05_networks",
        "exercises/week05_networks/solutions",
        
        # Mini-project subdirectories
        "miniprojects/project01_flocking_behavior",
        "miniprojects/project01_flocking_behavior/data",
        "miniprojects/project01_flocking_behavior/reference_solution",
        "miniprojects/project02_epidemic_modeling",
        "miniprojects/project02_epidemic_modeling/data",
        "miniprojects/project02_epidemic_modeling/reference_solution",
        "miniprojects/project03_traffic_flow",
        "miniprojects/project03_traffic_flow/data",
        "miniprojects/project03_traffic_flow/reference_solution",
        
        # Resource subdirectories
        "resources/visualization_gallery",
        "resources/visualization_gallery/fractal_examples",
        "resources/visualization_gallery/complex_systems_examples",
        
        # Data subdirectories
        "data/sample_datasets",
        "data/real_world_data",
        "data/synthetic_data",
        
        # Assessment subdirectories
        "assessments/midterm_project",
        "assessments/final_project",
        "assessments/grading_rubrics"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {directory}")

def create_readme_files():
    """Create README files for each major section."""
    
    readme_contents = {
        "lectures/README.md": """# Lecture Materials

This directory contains all theoretical content for the course.

## Structure
- Each week has its own subdirectory
- Slides are provided in PDF format
- Reading lists included for each topic
- Additional resources linked

## Usage
- Review slides before each class session
- Use reading lists for deeper understanding
- Slides are designed to complement hands-on notebooks
""",

        "notebooks/README.md": """# Interactive Notebooks

This directory contains all hands-on coding materials for the course.

## Structure
- One subdirectory per class session
- Student versions with TODO sections
- Complete solutions provided separately
- Progressive difficulty throughout course

## Usage
- Open in Google Colab or Jupyter
- Work through during class sessions
- Complete TODO sections as guided exercises
- Check solutions for self-assessment

## Google Colab Links
Each notebook includes a "Open in Colab" badge for easy access.
""",

        "exercises/README.md": """# Weekly Exercises

This directory contains practice problems for each week of the course.

## Structure
- One subdirectory per week
- Multiple exercises per week
- Solutions provided for self-assessment
- Increasing complexity as course progresses

## Assessment
- Exercises contribute 40% of final grade
- Lowest score dropped
- Focus on understanding over completion
- Collaboration encouraged with proper attribution

## Submission
- Submit via course management system
- Include both .ipynb and .html exports
- Document any collaboration or external resources used
""",

        "miniprojects/README.md": """# Mini-Projects

This directory contains larger applied modeling projects.

## Projects Overview
1. **Flocking Behavior**: Agent-based model of collective motion
2. **Epidemic Modeling**: Disease spread on networks  
3. **Traffic Flow**: Cellular automata for traffic dynamics

## Structure
- Project description and requirements
- Starter template notebook
- Sample data when applicable
- Reference solution (for instructors)
- Grading rubric

## Assessment
- Projects contribute 30% of final grade
- Emphasis on creativity and insight
- Professional presentation expected
- Real-world applications encouraged
""",

        "resources/README.md": """# Course Resources

This directory contains supplementary materials and guides.

## Contents
- Python cheatsheet and reference
- Google Colab setup guide
- Mathematical background materials
- Visualization gallery and examples
- Links to external resources

## Usage
- Reference materials for coding
- Background reading for concepts
- Inspiration for visualizations
- Troubleshooting guides
"""
    }
    
    for filepath, content in readme_contents.items():
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Created README: {filepath}")

def create_gitignore():
    """Create .gitignore file for the repository."""
    
    gitignore_content = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Course specific
*_SOLUTIONS.ipynb
*_SOLUTION.ipynb
solutions_hidden/
grading_private/
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    print("Created .gitignore")

def create_requirements():
    """Create requirements.txt for local installation."""
    
    requirements_content = """# Core scientific computing
numpy>=1.21.0
matplotlib>=3.5.0
scipy>=1.7.0
pandas>=1.3.0

# Jupyter ecosystem
jupyter>=1.0.0
ipywidgets>=7.6.0

# Network analysis
networkx>=2.6.0

# Additional visualization
seaborn>=0.11.0
plotly>=5.0.0

# Utilities
tqdm>=4.62.0
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements_content)
    print("Created requirements.txt")

def create_license():
    """Create LICENSE file."""
    
    license_content = """Creative Commons Attribution-ShareAlike 4.0 International License

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 
International License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-sa/4.0/ or send a letter to 
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose, 
  even commercially.

Under the following terms:
- Attribution — You must give appropriate credit, provide a link to the 
  license, and indicate if changes were made. You may do so in any reasonable 
  manner, but not in any way that suggests the licensor endorses you or your use.
- ShareAlike — If you remix, transform, or build upon the material, you must 
  distribute your contributions under the same license as the original.

No additional restrictions — You may not apply legal terms or technological 
measures that legally restrict others from doing anything the license permits.
"""
    
    with open('LICENSE', 'w') as f:
        f.write(license_content)
    print("Created LICENSE")

def create_sample_files():
    """Create some sample files to get started."""
    
    # Sample Python cheatsheet
    cheatsheet_content = """# Python Cheatsheet for Complex Systems Modeling

## Basic Data Types
```python
# Numbers
x = 5          # integer
y = 3.14       # float

# Lists (sequences)
points = [1, 2, 3, 4]
coordinates = [(0, 0), (1, 1), (2, 0)]

# Strings
message = "Hello, complex world!"
```

## Control Flow
```python
# Loops
for i in range(10):
    print(f"Step {i}")

for point in coordinates:
    x, y = point
    print(f"Position: ({x}, {y})")

# Conditionals
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```

## Functions
```python
def midpoint(p1, p2):
    "Calculate midpoint between two points"
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

# Usage
result = midpoint((0, 0), (2, 4))
```

## Essential Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
import random

# NumPy arrays
arr = np.array([1, 2, 3, 4])
matrix = np.array([[1, 2], [3, 4]])

# Plotting
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Simple Plot')
plt.show()

# Random numbers
random_point = (random.random(), random.random())
random_choice = random.choice(['red', 'blue', 'green'])
```

## Common Patterns in Complex Systems
```python
# Chaos game step
def chaos_step(current, vertices, fraction=0.5):
    chosen = random.choice(vertices)
    new_x = current[0] + fraction * (chosen[0] - current[0])
    new_y = current[1] + fraction * (chosen[1] - current[1])
    return (new_x, new_y)

# Distance between points
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Visualization template
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x_coords, y_coords, s=1, alpha=0.7)
ax.set_aspect('equal')
ax.set_title('Complex System Visualization')
plt.show()
```
"""
    
    with open('resources/python_cheatsheet.md', 'w') as f:
        f.write(cheatsheet_content)
    print("Created Python cheatsheet")
    
    # Sample Colab guide
    colab_guide_content = """# Google Colab Setup Guide

## What is Google Colab?
Google Colaboratory (Colab) is a free cloud-based Jupyter notebook environment that requires no setup and runs entirely in the cloud.

## Getting Started

### 1. Access Colab
- Go to [colab.research.google.com](https://colab.research.google.com)
- Sign in with your Google account
- No installation required!

### 2. Opening Course Notebooks
- Click on any notebook link from the course repository
- Choose "Open in Colab" 
- The notebook will open in a new tab

### 3. Saving Your Work
- **Important**: Make a copy to your Google Drive!
- File → Save a copy in Drive
- This creates your personal copy that you can edit

### 4. Running Code Cells
- Click the play button (▶) next to each code cell
- Or use Shift + Enter to run a cell
- Cells run in order from top to bottom

## Key Features

### Code Cells
```python
# This is a code cell
import numpy as np
print("Hello, complex systems!")
```

### Text Cells
Text cells use Markdown formatting:
- **Bold text**
- *Italic text*
- `Code snippets`
- Mathematical formulas: $E = mc^2$

### Visualizations
Plots appear directly in the notebook:
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 2])
plt.show()
```

## Pro Tips

### Keyboard Shortcuts
- `Shift + Enter`: Run current cell and move to next
- `Ctrl + M, A`: Insert cell above
- `Ctrl + M, B`: Insert cell below
- `Ctrl + M, D`: Delete cell

### Managing Runtime
- Runtime → Restart runtime: Fresh start
- Runtime → Run all: Execute all cells
- Sessions timeout after ~12 hours of inactivity

### Sharing Your Work
- File → Share: Get shareable link
- Make sure permissions are set correctly
- Can share view-only or edit access

## Troubleshooting

### Common Issues
1. **"Module not found"**: Run the import cell first
2. **Variables undefined**: Run cells in order from top
3. **Slow performance**: Restart runtime if needed
4. **Lost work**: Always save a copy to Drive!

### Getting Help
- Use `help(function_name)` for documentation
- Add `?` after function name for quick help
- Check the course discussion forum
- Ask during office hours

## Best Practices
- Save frequently (File → Save)
- Run cells in order
- Add comments to explain your code
- Use descriptive variable names
- Test small changes incrementally
"""
    
    with open('resources/colab_guide.md', 'w') as f:
        f.write(colab_guide_content)
    print("Created Colab guide")

def create_project_template():
    """Create a sample mini-project template."""
    
    project_description = """# Mini-Project 1: Flocking Behavior

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
"""
    
    with open('miniprojects/project01_flocking_behavior/project_description.md', 'w') as f:
        f.write(project_description)
    print("Created sample project description")

def main():
    """Run the complete setup process."""
    
    print("🚀 Setting up Complex Systems Modeling Course Repository")
    print("=" * 60)
    
    print("\n1. Creating directory structure...")
    create_directory_structure()
    
    print("\n2. Creating README files...")
    create_readme_files()
    
    print("\n3. Creating configuration files...")
    create_gitignore()
    create_requirements()
    create_license()
    
    print("\n4. Creating sample resources...")
    create_sample_files()
    
    print("\n5. Creating project template...")
    create_project_template()
    
    print("\n" + "=" * 60)
    print("✅ Repository setup complete!")
    print("\nNext steps:")
    print("1. Initialize git repository: git init")
    print("2. Add files: git add .")
    print("3. Commit: git commit -m 'Initial course repository setup'")
    print("4. Create GitHub repository and push")
    print("5. Add your course notebooks to appropriate directories")
    print("6. Customize README.md with your specific details")
    print("\n🌟 Your complex systems course repository is ready!")

if __name__ == "__main__":
    main()