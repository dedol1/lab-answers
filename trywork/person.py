
# a function to retrieve age from a user
def get_age():
        age = int(input('How old are you? '))
        return age

# a fuction to  retrieve the name of a user
def get_name():
	name = input('Enter your name')
	return name

print(get_age())
print(get_name())

print('your name is '+get_name()+' and you are '+str(get_age())+' old')
