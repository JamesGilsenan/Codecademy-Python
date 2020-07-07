def get_y(m, b, x):
    y = (m * x) + b
    return y

def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    y_value = get_y(m, b, x_point)
    difference = y_value - y_point
    return abs(difference)

print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)
#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))
#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))