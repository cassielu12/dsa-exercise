m = 0.0
def sum_num(text):
    n = 0
    global m
    n = float(text)
    m = m + n 
    return m


while True:
    text = input()
    if text == "0":
        print(f'The grand total is {m}')
        break
        
    else:
        try:
            sum_num(text)
            print(f'The total is now {m}')
        except ValueError:
            print ("That wasn’t a number.")
       
        
        