user_input = str(input("Enter the sentance:"))
split_input = user_input.split()
print(split_input)
a = ' '
print(a)
for i in split_input:
	a = a+str(i[0].upper())
print(a)