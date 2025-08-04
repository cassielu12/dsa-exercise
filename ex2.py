def compute (a, b):
    result_dic = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b if b != 0 else "error: b cannot be zero",
        '%': a % b if b != 0 else "error: b cannot be zero",
        '^': a ** b
    }
    return result_dic
try:
    a = int (input ( ))
    b = int (input ( ))
except ValueError:
    print ("please enter just the integer")
    exit ()

result_dic = compute(a, b)
for operater, result in result_dic.items():
    print (f"{a} {operater} {b} is {result}")