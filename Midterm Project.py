tabs = []


def open_new_tab():
    number = int(input("Please enter the number of tabs : "))
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
        print("\nThere are no tabs open for you to close.")
    else:
        print("\nThe opened tabs are of the following indexes : ")

    for i in range(len(tabs)):
        print(f"\n{i + 1}. {tabs[i]}")

    close_index = input("\nEnter the index of the tab you want to close / press ENTER to close the last tab : ")
    if close_index == "":  # if empty input, means we remove the last TAB
        closed_tab = tabs.pop()  # https://www.w3schools.com/python/ref_list_pop.asp method used to CLOSE the last tab directly from the users tabs list
        print(f"\nYou closed the last tab {closed_tab}")
    else:
        close_index = int(close_index)
        if 1 <= close_index <= len(tabs):
            closed_tab = tabs.pop(close_index - 1)
            print(f"\nYou closed the last tab {closed_tab}")
        else:
            print("\nInvalid Index. No tab closed")
            return


close_tab()
