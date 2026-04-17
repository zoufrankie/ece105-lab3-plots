"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.
def generate_data(seed):
    """Generate synthetic temperature sensor data.

    Parameters
    ----------
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    sensor_a : ndarray
        Temperature readings from Sensor A, shape (200,) with mean 25°C and std 3°C.
    sensor_b : ndarray
        Temperature readings from Sensor B, shape (200,) with mean 27°C and std 4.5°C.
    timestamps : ndarray
        Time values in seconds, shape (200,) uniformly distributed from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed=seed)
    
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)
    
    return sensor_a, sensor_b, timestamps
# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Create a scatter plot of sensor temperature readings over time.

    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings from Sensor A, shape (n,).
    sensor_b : ndarray
        Temperature readings from Sensor B, shape (n,).
    timestamps : ndarray
        Time values in seconds, shape (n,).
    ax : matplotlib.axes.Axes
        Axes object to plot on. Modified in place.

    Returns
    -------
    None
    """
    order = np.argsort(timestamps)
    t = timestamps[order]
    a = sensor_a[order]
    b = sensor_b[order]
    
    ax.scatter(t, a, s=30, alpha=0.7, label='Sensor A', color='C0')
    ax.scatter(t, b, s=30, alpha=0.7, label='Sensor B', color='C1')
    ax.set_title('Temperature Sensor Readings Over Time')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.legend()
# Create plot_histogram(sensor_a, sensor_b, ax) that draws
# overlapping histograms of both sensors on the given Axes object.
# Use NumPy-style docstring. Modify ax in place, return None.
def plot_histogram(sensor_a, sensor_b, ax):
    """Create overlapping histograms of sensor temperature readings.

    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings from Sensor A, shape (n,).
    sensor_b : ndarray
        Temperature readings from Sensor B, shape (n,).
    ax : matplotlib.axes.Axes
        Axes object to plot on. Modified in place.

    Returns
    -------
    None
    """
    bins = 20
    ax.hist(sensor_a, bins=bins, alpha=0.6, label='Sensor A', color='C0', edgecolor='black')
    ax.hist(sensor_b, bins=bins, alpha=0.6, label='Sensor B', color='C1', edgecolor='black')
    ax.set_title('Temperature Distribution by Sensor')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.legend()
# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.
def main():
    """Generate sensor plots and save them to disk.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    sensor_a, sensor_b, timestamps = generate_data(seed=42)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])

    boxplot_fn = globals().get('plot_boxplot')
    if callable(boxplot_fn):
        boxplot_fn(sensor_a, sensor_b, axes[2])
    else:
        axes[2].set_title('Box Plot')
        axes[2].text(0.5, 0.5, 'plot_boxplot not implemented', ha='center', va='center')
        axes[2].set_axis_off()

    fig.tight_layout()
    fig.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    plt.close(fig)


if __name__ == '__main__':
    main()