"""Lucas Clowes"""


def main():
    name = get_name()
    for i in range(1, len(name), 2):
        print(name[i])


def get_name():
    name = input("Enter your name: ")
    while not name:
        print('Entry must not be blank')
        name = input("Enter your name: ")
    return name


main()
