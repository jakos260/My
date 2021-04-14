def my_cubic_interpolation(x, f, x_new):
    dy1 = derivative(f, x[0])
    dy2 = derivative(f, x[len(x)-1])

#
#     for i in range(len(x_new)):
#         pl, vl = four_closest_points(x, f, x_new[i])
#         array = make_equations(pl)
#
# def four_closest_points(x, f, x_new):
#     point_list = []
#     value_list = []
#
#     for i in range(len(x)-2):
#         if x_new - x[i] < x[i] - x[i+2]:
#             point_list.append(x[i])
#             value_list.append(f[i])
#         if len(point_list) == 4:
#             break
#     return point_list, value_list
#
# def solve_equation(array, value_list):