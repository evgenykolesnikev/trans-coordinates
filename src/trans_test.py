import math
import random
from polar import Polar
from cartesian2d import Cartesian2D

def test_polar_to_cartesian_and_back(num_points=10):
    # Generate random polar coordinates
    polar_points = [
        Polar(random.uniform(1, 100), random.uniform(0, 2 * math.pi)) for _ in range(num_points)
    ]
    
    for polar_point in polar_points:
        print(f"Polar coordinates: r = {polar_point.r:.2f}, theta = {polar_point.theta:.2f}")
        
        # Convert to Cartesian coordinates
        cartesian_point = Cartesian2D.from_polar(polar_point.r, polar_point.theta)
        print(f"Cartesian coordinates: x = {cartesian_point.x:.2f}, y = {cartesian_point.y:.2f}")
        
        # Convert back to polar coordinates
        polar_from_cartesian = Polar.from_cartesian(cartesian_point.x, cartesian_point.y)
        print(f"Back to polar coordinates: r = {polar_from_cartesian.r:.2f}, theta = {polar_from_cartesian.theta:.2f}")
        
        # Check for correctness
        assert math.isclose(polar_point.r, polar_from_cartesian.r, rel_tol=1e-9), "Error: Radii do not match"
        assert math.isclose(polar_point.theta, polar_from_cartesian.theta, rel_tol=1e-9), "Error: Angles do not match"
        
        print("Test finished!")

if __name__ == "__main__":
    test_polar_to_cartesian_and_back()
