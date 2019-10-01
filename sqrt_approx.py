#adapted from the lecture of Dr. Ian McLoughlin

def sqrt(x):
    # Initial guess or start number using a float to tell python to use float instead of an int
    z = 1.0

    # tell python to calculate a better estimate for the
    # square root of x until within set number of decimal places

    while abs(z*z - x) >=0.0001:

        z -=(z*z - x) / (2*z)

    return z

z = sqrt(63.0)

print(z)

print(z*z)
