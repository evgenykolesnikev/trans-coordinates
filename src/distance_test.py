import matplotlib.pyplot as plt
import time
from cartesian2d import Cartesian2D
from polar import Polar
from spherical import Spherical
from cartesian3d import Cartesian3D
import random

# Generate an array of point pairs for each coordinate system
def generate_cartesian_points(count):
    return [(Cartesian2D(random.uniform(50, 1000), random.uniform(50, 1000)), 
             Cartesian2D(random.uniform(50, 1000), random.uniform(50, 1000))) for _ in range(count)]

def generate_cartesian3d_points(count):
    return [(Cartesian3D(random.uniform(50, 1000), random.uniform(50, 1000), random.uniform(50, 1000)),
             Cartesian3D(random.uniform(50, 1000), random.uniform(50, 1000), random.uniform(50, 1000))) for _ in range(count)]

def generate_polar_points(count):
    return [(Polar(random.uniform(50, 1000), random.uniform(0, 2 * 3.1415)),
             Polar(random.uniform(50, 1000), random.uniform(0, 2 * 3.1415))) for _ in range(count)]

def generate_spherical_points(count):
    return [(Spherical(random.uniform(50, 1000), random.uniform(0, 2 * 3.1415), random.uniform(0, 3.1415)),
             Spherical(random.uniform(50, 1000), random.uniform(0, 2 * 3.1415), random.uniform(0, 3.1415))) for _ in range(count)]

# Function to measure average execution time
def benchmark(func, point_pairs, iterations=10):
    total_time = 0
    for _ in range(iterations):
        start_time = time.time() * 1000
        func(point_pairs)
        total_time += (time.time() * 1000 - start_time)
    return total_time / iterations  # Return average time

# Example functions that calculate distances between pairs of points
def calculate_distances_cartesian(points):
    for point1, point2 in points:
        point1.distance(point2)

def calculate_distances_cartesian3d(points):
    for point1, point2 in points:
        point1.distance(point2)

def calculate_distances_polar(points):
    for point1, point2 in points:
        point1.distance(point2)

def calculate_distances_spherical_volume(points):
    for point1, point2 in points:
        point1.distance_through_volume(point2)

def calculate_distances_spherical_surface(points):
    for point1, point2 in points:
        point1.distance_on_surface(point2)

# Generating an array of sizes for point pairs
start_size = 10000
end_size = 100000
step = 10000
point_sizes = list(range(start_size, end_size + 1, step)) 

cartesian_times = []
cartesian3d_times = []
polar_times = []
spherical_volume_times = []
spherical_surface_times = []

# Number of iterations for benchmarking
iterations = 4

for size in point_sizes:
    cartesian_pairs = generate_cartesian_points(size)
    cartesian3d_pairs = generate_cartesian3d_points(size)
    polar_pairs = generate_polar_points(size)
    spherical_pairs = generate_spherical_points(size)

    # Measuring average execution time for each coordinate system
    cartesian_time = benchmark(calculate_distances_cartesian, cartesian_pairs, iterations)
    cartesian3d_time = benchmark(calculate_distances_cartesian3d, cartesian3d_pairs, iterations)
    polar_time = benchmark(calculate_distances_polar, polar_pairs, iterations)
    spherical_volume_time = benchmark(calculate_distances_spherical_volume, spherical_pairs, iterations)
    spherical_surface_time = benchmark(calculate_distances_spherical_surface, spherical_pairs, iterations)

    cartesian_times.append(cartesian_time)
    cartesian3d_times.append(cartesian3d_time)
    polar_times.append(polar_time)
    spherical_volume_times.append(spherical_volume_time)
    spherical_surface_times.append(spherical_surface_time)

# Plotting the graphs
plt.plot(point_sizes, cartesian_times, label='Cartesian 2D', marker='o')
plt.plot(point_sizes, cartesian3d_times, label='Cartesian 3D', marker='o')
plt.plot(point_sizes, polar_times, label='Polar', marker='o')
plt.plot(point_sizes, spherical_volume_times, label='Spherical by Volume Distance', marker='o')
plt.plot(point_sizes, spherical_surface_times, label='Spherical by Surface Distance', marker='o')

plt.title('Execution Time of Distance Calculations')
plt.xlabel('Array Size (number of point pairs)')
plt.ylabel('Execution Time (milliseconds)')
plt.legend()

plt.get_current_fig_manager().set_window_title('Graphical Results')

plt.show()
