a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
main_det = a * d - c * b
det_x = e * d - f * b
det_y = a * f - c * e
if main_det != 0:
    x = det_x / main_det
    y = det_y / main_det
    print(x, y)
elif main_det = 0 and det_x = 0 and det_y = 0:
    print(1, -c / d, f / d)
elif main_det = 0 and det_x = 0 and det_y != 0:
    print(3, -c / d, f / d)
elif main_det = 0 and det_x != 0 and det_y = 0:
    print(4, -c / d, f / d)
else:
    print(0)
