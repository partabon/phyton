#6. Write a function called calculate_slope
# which return the slope of a linear equation
def calculate_slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

print(calculate_slope(8,2,-4,-1))

#7.Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation,
#  solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    x1=(-b+(b**2-4*a*c)**.5)/(2*a)
    x2=(-b-(b**2-4*a*c)**.5)/(2*a)
    return [x1,x2]

print(solve_quadratic_eqn(5,-2,-1))