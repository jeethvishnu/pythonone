def sum_of_digits(num, is_even=True):

  sum = 0
  while num > 0:
    digit = num % 10
    if digit % 2 == 0 if is_even else digit % 2 != 0:
      sum += digit
    num //= 10
  return sum

def difference_of_odd_even_sums(num):

  sum_even = sum_of_digits(num)
  sum_odd = sum_of_digits(num, False)
  return sum_even - sum_odd

num = 123456789
difference = difference_of_odd_even_sums(num)
print(f"Difference between sum of odd and even digits in {num} is: {difference}")
