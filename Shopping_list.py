# Task 1

grocery_list = []

def main():
    while True:
        ans = input('''
What would you like to do with your grocery list?
Enter the corresponding number:

    1- ADD item
    2- Remove itme
    3- View your list
    4- Quit
''')
        if ans == '1':
            add()
        elif ans == '2':
            remove()
        elif ans == '3':
            view_list()
        elif ans == '4':
            print("Enjoy the day!!!")
            break

def add():
    ans = input('what would you like to add: ')
    grocery_list.append(ans)

def remove():
    ans = input('what would you like to remove: ')
    grocery_list.append(ans)

def view_list():
    ans = input('Here is your shopping list')
    print(grocery_list)

main()