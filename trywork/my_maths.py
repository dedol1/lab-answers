
def calculate():
	num1 = float(input("Enter num1 : "))
	op = input("Enter operator : ")
	num2 = float(input("Enter num2 : "))

	if op =='+':
		print(float(num1) + float(num2))

	if op =='-':
                print(float(num1) - float(num2))

	if op =='*':
                print(float(num1) * float(num2))

	if op =='/':
                print(float(num1) /float(num2))
calculate()

