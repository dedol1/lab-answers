n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')



def is_vowel(char):
    return is_in_list(char.lower(), 'aeiou')

def is_in_list(char, lst):
    if not lst:
        return False
    if char == lst[0]:
        return True
    return is_in_list(char, lst[1:])
