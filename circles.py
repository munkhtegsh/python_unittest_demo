from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError('Radius can be positive real number')

    if r < 0:
        raise ValueError('Value can not be negative number')

    return pi * (r ** 2)

# # test fn
# radii = [2, 0, -3, 2+5j, True, "radius"]

# for r in radii:
#     A = circle_area(r)
#     print(message.format(radius=r, area=A))


