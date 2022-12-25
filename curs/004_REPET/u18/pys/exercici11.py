def sum_divisors(n):
  sum = 0
  i = n -1
  while i != 0 and n != 0:
    if (n % i) == 0:
        sum = sum + i
    i -= 1
  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
