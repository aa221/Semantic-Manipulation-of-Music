import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import os
import os
import numpy as np
import matplotlib.pyplot as plt


def plot_weighted_point_in_circle(p1, p2, p3, p4, path):
    # Handle empty or invalid path
    if not path or os.path.basename(path) == '':
        directory = 'circle_images'
        filename = "unknown_pattern.png"
        path = os.path.join(directory, filename)
    else:
        directory = os.path.dirname(path)
    
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    
    # Circle parameters
    radius = 1
    theta = np.linspace(0, 2*np.pi, 100)

    # Calculate weighted average position, assuming a simplistic mapping for demonstration
    x = (p1 - p3) * radius
    y = (p2 - p4) * radius

    # Ensure the point lies within the circle
    distance = np.sqrt(x**2 + y**2)
    if distance > radius:
        x, y = x / distance * radius, y / distance * radius

    # Plotting
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    
    # Plot circle
    ax.plot(radius * np.cos(theta), radius * np.sin(theta), 'b')  # Circle outline
    
    # Plot Cartesian coordinates
    ax.axhline(0, color='black', lw=1)  # Horizontal line
    ax.axvline(0, color='black', lw=1)  # Vertical line

    # Plot weighted point
    ax.plot(x, y, 'ro')  # 'ro' for red dot

    # Set limits and labels for clarity
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    if 'melody' in path:
        ax.set_title('The Russel Diagram Before Mood Transformation')
    else: 
        ax.set_title('The Russel Diagram After Mood Transformation')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    # Add labels for the emotions
    scale_factor = 0.88  # Adjust this as needed to scale the points inside the circle
    emotions = {
        'HAPPY': (0.9 * scale_factor, 0.1 * scale_factor),
        'AROUSED': (0.3 * scale_factor, 0.9 * scale_factor),
        'SAD': (-0.9 * scale_factor, -0.3 * scale_factor),
        'TIRED': (-0.1 * scale_factor, -0.9 * scale_factor),
    }

    for emotion, (ex, ey) in emotions.items():
        ax.text(ex, ey, emotion, fontsize=8, ha='center', va='center')

    # Save the plot to the specified path
    plt.savefig(path)
    print(f"Plot saved at: {path}")
    
    # Close the plot window to free up memory
    plt.close()

# Example usage
#plot_weighted_point_in_circle(0.5372056,  0.04071891, 0.11824992, 0.3038256, 'circle_images/105/104_chord_gen.png')