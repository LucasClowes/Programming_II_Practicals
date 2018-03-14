out_file = open("user_names.txt", 'w')

user_name = input("Enter your name: ")
print(user_name, file=out_file)  # can also be outFile.write(name)
out_file.close()

in_file = open("user_names.txt", 'r')
name = in_file.read().strip()
print("Your name is {}".format(name))
in_file.close()

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()
