def custom_encoder(text):
    pos=0
    list=[]
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    for char in text.lower():
        if char in  reference_string :
            pos = reference_string.index(char)
        else:
            pos = -1
        list.append(pos)
    return list

        
        
        
