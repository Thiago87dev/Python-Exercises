def multiplica(*args):
    total = 1
    for i in args:
        total *= i
    return total

num_mult = multiplica(1,3,5,7,9)
print(num_mult)
