# Google Colab Setup Guide

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
