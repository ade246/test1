"""Volume and area of cylinder, with exceptions.
This is the starter version, without exceptions.
The functions return a negative value if the height is negative.

TPRG 2131 Fall 2023 Test 1
### KHARI WALLACE, 100807131, TPRG 2131 ###
November 02, 2023
Khari Wallace <khari.wallace@dcmail.ca>
"""

from math import pi

def volume_cylinder(diameter, height):
    """Volume of a cylinder given diameter and height."""
    return pi * (diameter / 2.0)**2 * height

def area_cylinder(diameter, height):
    """Surface area of a cylinder given diameter and height."""
    radius = diameter / 2.0
    return 2.0 * pi * radius * (height + radius)  # simplified

if __name__ == "__main__":
    while True:
        dia = float(input("\nDiameter? "))
        high = float(input("Height? "))
        print("The volume is", volume_cylinder(dia, high))
        print("The area is", area_cylinder(dia, high))

