import re

txt= 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

regex_pattern = r'\d+|-\d+'  # d is a special character which means digits, + mean one or more times
points = re.findall(regex_pattern, txt)
print(points)  # ['6', '2019', '8', '2021'] - now, this is better!

int_points= [int(i) for i in points]
print(int_points)

#bueno, ya está ordenada, pero si no fuera el caso, tendríamos que hacer:
int_points.sort()
distance = int_points[-1]-int_points[0]

print(distance)