
def sort (string1):
  char_list = sorted (string1)
  string2 = "".join(char_list)
  return string2

string1 = input ("input: ")
output = sort(string1)
print (output)