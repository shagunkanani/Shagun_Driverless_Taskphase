import numpy as np

car_x = 10
car_y = 5
theta = np.deg2rad(30)

v = 5
a = 1
omega = np.deg2rad(10)

t = 0.2
dt = 0.001
steps = int(t / dt)

cones = {
    "B1": (12, 7),
    "B2": (8, 6),
    "Y1": (13, 4),
    "Y2": (9, 3)
}

def transform_to_car_frame(x, y, car_x, car_y, theta):
    dx = x - car_x
    dy = y - car_y

    R = np.array([
        [np.cos(theta), np.sin(theta)],
        [-np.sin(theta), np.cos(theta)]
    ])

    disp = np.array([dx, dy])
    cone_wrt_car = R @ disp 

    return cone_wrt_car


for name, coord in cones.items():
    x, y = coord
    result = transform_to_car_frame(x, y, car_x, car_y, theta)
    print(f"Transformed coordinates of {name} in car frame: {result}")

x = car_x
y = car_y

for i in range(steps):
    x = x + v * np.cos(theta) * dt
    y = y + v * np.sin(theta) * dt
    v = v + a * dt
    theta = theta + omega * dt

print("New x:", x)
print("New y:", y)
print("New heading:", np.rad2deg(theta))

print("\nCones in car frame at new pose:")

for name, coord in cones.items():
    cone_x, cone_y = coord

    result = transform_to_car_frame(
        cone_x, cone_y, x, y, theta
    )

    print(f"{name}: {np.round(result, 4)}")