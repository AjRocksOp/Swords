# To accept a title & a list, then print it as a menu

def menu(items, title="MENU"):
    print(f"\n\n\t {title}")
    for i in range(len(items)):
        print(f'{i+1}. {items[i]}')


if(__name__ == "__main__"):
    shopping_list = input(' Enter Shopping List (,) : ').split(',')

    menu(shopping_list, 'Shopping List')
