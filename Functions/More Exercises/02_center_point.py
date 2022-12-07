from math import floor


def center_point(x1, y1, x2, y2):
    sum_first_point = abs(x1) + abs(y1)
    sum_second_point = abs(x2) + abs(y2)
    if sum_first_point == sum_second_point:
        return floor(x1), floor(y1)
    else:
        if sum_first_point < sum_second_point:
            return floor(x1), floor(y1)
        else:
            return floor(x2), floor(y2)


point_x1 = float(input())
point_y1 = float(input())
point_x2 = float(input())
point_y2 = float(input())
print(center_point(point_x1, point_y1, point_x2, point_y2))
