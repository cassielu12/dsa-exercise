def coun(string):
    i = 0
    for char in string:
        if char.lower() in ["a","e","i","o","u"]:
            i = i + 1
    return i
string=input()
print (f'Number of vowels: {coun(string)}')
    
        
            