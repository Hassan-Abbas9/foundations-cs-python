tabs = []

def open_new_tab():
    number = int(input("please enter the number of tabs : "))
    for i in range(number):
        title = input(f'Please input the TITLE of Tab {i + 1} : ')
        url = input(f'Please input the URL of Tab {i + 1} : ')
        new_tab = {title: url}
        tabs.append(new_tab)
        print(f"You opened {new_tab} tab successfully!")

    print("your opened tabs are : ", tabs)


open_new_tab()


def close_tab():

    if not tabs:  # same as if tabs == [], simplified to fix "Expression can be simplified" weak warning.
        print("There are no tabs open.")

    print("\nThe opened tabs are of the following indexes: ")
    for i in range(len(tabs)):
        print(f"\n{i+1}. {tabs[i]}")

