# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

a = int(input('Enter the lengths of the three sides of a triangle: '))
b = int(input('Enter the lengths of the three sides of a triangle: '))
c = int(input('Enter the lengths of the three sides of a triangle: '))


if a == b and b == c:
  print(f'A triangle with sides of {a}, {b}, and {c} is a type of equalateral triangle')
elif a != b and b != c and a != c:
  print(f'A triangle with sides of {a}, {b}, and {c} is a type of scalene triangle')
else:
  print(f'A triangle with sides of {a}, {b}, and {c} is a type of isosceles triangle')


