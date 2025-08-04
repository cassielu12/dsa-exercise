def sum_fun (n):
    sum_result = n * (n + 1)/ 2
    return sum_result

try:
    n = int(input ())
    if n > 0:
        print(f'The sum of the first {n} positive integers is {int(sum_fun(n))}')
    else:
        print('should enter a positive integer')
        exit()
except ValueError:
    print('should enter an integer')