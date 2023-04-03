def is_point_inside_square(point, center, side_length):
    half_side = side_length / 2
    x_min, x_max = center[0] - half_side, center[0] + half_side
    y_min, y_max = center[1] - half_side, center[1] + half_side

    return (x_min <= point[0] <= x_max) and (y_min <= point[1] <= y_max)

table_1_raw = """
0,2 1,5 1,3 1,0 2,2 1,2 1,1 6,6
"""

table_2_raw = """
2,3 0,1 2,4 0,0 1,2 0,2 2,2 1,1
"""

table_1 = [tuple(map(int, coords.split(','))) for coords in table_1_raw.split()]
table_2 = [tuple(map(int, coords.split(','))) for coords in table_2_raw.split()]

larger_square_center = (2, 2)
larger_square_side = 4
smaller_square_center = (2, 2)
smaller_square_side = 2

points_table_1 = {'inside_larger': [], 'inside_smaller': [], 'outside': [], 'boundary': []}
points_table_2 = {'inside_larger': [], 'inside_smaller': [], 'outside': [], 'boundary': []}

for point in table_1:
    if is_point_inside_square(point, larger_square_center, larger_square_side):
        if is_point_inside_square(point, smaller_square_center, smaller_square_side):
            points_table_1['inside_smaller'].append(point)
        else:
            points_table_1['inside_larger'].append(point)
    else:
        points_table_1['outside'].append(point)

for point in table_2:
    if is_point_inside_square(point, larger_square_center, larger_square_side):
        if is_point_inside_square(point, smaller_square_center, smaller_square_side):
            points_table_2['inside_smaller'].append(point)
        else:
            points_table_2['inside_larger'].append(point)
    else:
        points_table_2['outside'].append(point)
# Print the categorized points for Table 1 and Table 2
print("Points in Table 1:")
for category, points in points_table_1.items():
    print(f"- {category.capitalize().replace('_', ' ')}: {points}")

print("\nPoints in Table 2:")
for category, points in points_table_2.items():
    print(f"- {category.capitalize().replace('_', ' ')}: {points}")