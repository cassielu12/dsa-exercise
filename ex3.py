def square (N):
    dic = {}
    for i in range(N):
        dic.update({i+1: (i + 1) ** 2})
    return dic
text = input()
try:
    N = int(text.split('\n')[0])
    print (square(N))

except ValueError:
    print('The first line of input should contain an int')
    exit()

