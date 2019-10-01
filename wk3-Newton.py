# Lecture from Week 3 of Machine Learning and Statistics
# Adapted from: https://tour.golang.org/flowcontrol/8
def sqrt(x):
    # Initial guess
    z = 1.0

    # Keep getting a better estimate for the square root of x 
    # until you are within 2 decimal places
    while abs(z*z - x) >= 0.01:
        #Get a better approximation for the square root.
        z -= (z*z - x) / (2*z)

    # Return z
    return z

sqrt(8.0) 