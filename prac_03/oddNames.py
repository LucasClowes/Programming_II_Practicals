"""Lucas Clowes"""


def main():
    name = input("Enter your name: ")
    while not name:
        print('Entry must not be blank')
        name = input("Enter your name: ")
    for i in range(1, len(name), 2):
        print(name[i])


main()
