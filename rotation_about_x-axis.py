import math


def calcu__transform(X, Y):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def calcu_point(X, Y):
    result = [0, 0, 0]
    for i in range(len(X)):
        for j in range(len(Y)):
            result[i] += X[i][j] * Y[j]
    return result


def transform():
    coord = list(
        map(
            int,
            input("Enter point in x y z coordinates: ").strip().split(),
        )
    )[:3]
    theta = list(
        map(
            int,
            input(
                "Enter 3 angles of rotation about the x y z coordinates respect. in degrees: "
            )
            .strip()
            .split(),
        )
    )[:3]

    Rotation_x = [
        [1, 0, 0],
        [0, math.cos(math.radians(theta[0])), -math.sin(math.radians(theta[0]))],
        [0, math.sin(math.radians(theta[0])), math.cos(math.radians(theta[0]))],
    ]

    Rotation_y = [
        [math.cos(math.radians(theta[1])), 0, math.sin(math.radians(theta[1]))],
        [0, 1, 0],
        [-math.sin(math.radians(theta[1])), 0, math.cos(math.radians(theta[1]))],
    ]

    Rotation_z = [
        [math.cos(math.radians(theta[2])), -math.sin(math.radians(theta[2])), 0],
        [math.sin(math.radians(theta[2])), math.cos(math.radians(theta[2])), 0],
        [0, 0, 1],
    ]

    transformation = calcu__transform(Rotation_x, Rotation_y)
    transformation = calcu__transform(transformation, Rotation_z)
    final_result = calcu_point(transformation, coord)

    print(
        f"Coordinates of Point {coord[0], coord[1], coord[2]} with respect to original frame is {round(final_result[0], 5), round(final_result[1], 5), round(final_result[2], 5)}"
    )
    input("Press Enter to exit...")

if __name__ == "__main__":
    transform()
