i = 0
while (i < 10 ): 
   i = i + 1
   print (i)
#   print range(12,21,2)


for i in range(12,21,2):
	print(i)


def even():
	rangeSt = float(input('Enter range start :'))
	rangeStop = float(input('Enter range ending :'))
	while(rangeSt<rangeStop):
	   if(rangeSt % 2 == 0):
	       print(rangeSt)
	   rangeSt+=1
even()



def reverse_even():
	number =[]
	num1 =float(input('Enter first number :'))
	num2 =float(input('Enter second number:'))
	for num in range(num1-1, num2):
		if( num % 2 == 0):
			number.append(num)
	return number
print('calling reverse even numbers')
reverse_list = reverse_even()
reverse_list.reverse()
print(reverse_list)

