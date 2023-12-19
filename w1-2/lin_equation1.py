a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())
s1 = float(input())
s2 = float(input())
main_det = a1 * b2 - a2 * b1
if main_det != 0:
    det_x = s1 * b2 - s2 * b1
    det_y = a1 * s2 - a2 * s1
    x = det_x / main_det
    y = det_y / main_det
    print(x, y)
else:
    print("")
