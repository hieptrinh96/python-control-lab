# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

# (n - 1) + (n - 2)
fib = {
  'term': 0,
  'number': 0
}

# result from fib(50)
# 12,586,269,025

# my results
# 12,586,269,025


current = fib['number']
previous = 1 

while fib['term'] != 51:
  if (fib['term'] == 0):
    print(f'{fib}')
  else:
    acc = current + previous
    previous = current
    current = acc
    fib['number'] = acc
    print(f'{fib}')
  fib['term']+=1
