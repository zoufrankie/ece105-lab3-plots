# ECE105 Lab 3 Sensor Plot Generation

Generates synthetic two-sensor temperature data and produces a combined analysis figure with scatter, histogram, and box plot visualizations.

## Installation

Activate the course Conda environment, then install required plotting dependencies with Conda or Mamba.

```bash
conda activate ece105
conda install numpy matplotlib
```

Or with Mamba:

```bash
conda activate ece105
mamba install numpy matplotlib
```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

## Example Output

The script produces one image file:

- `sensor_analysis.png`: a 1x3 figure containing:
  - a time-based scatter plot comparing Sensor A and Sensor B temperatures
  - overlapping histograms showing both sensors' temperature distributions
  - side-by-side box plots summarizing spread, median, and outliers for each sensor

## AI Tools Used and Disclosure

I used GitHub Copilot (CLI and VS Code chat) to generate initial implementations of plotting functions and help convert notebook code into a Python script. All generated code was reviewed, tested, and manually edited for correctness and compliance with NumPy docstring formatting requirements. I also used Copilot assistance to debug Git and Matplotlib issues during development.
