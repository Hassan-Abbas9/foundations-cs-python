import os  # https://realpython.com/working-with-files-in-python/ used for handling the OS files to read and write
import requests  # pip install requests used this in terminal  https://pypi.org/project/beautifulsoup4/
from bs4 import BeautifulSoup  # pip install beautifulsoup4 used this in terminal
import json

tabs = []


def get_html_content(url):
    response = requests.get(url)  # Send an HTTP GET request to the URL of the selected tab - https://www.w3schools.com/PYTHON/ref_requests_get.asp
    html_content = response.text  # Get the HTML content of the response content above
    soup = BeautifulSoup(html_content, 'html.parser')  # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start
    return soup.prettify()  # https://pypi.org/project/beautifulsoup4/ it is the BeautifulSoup object method that prettifies the content.


def open_new_tab():
    number = int(input("Please enter the number of tabs you want to input : "))

    for i in range(number):
        title = input(f'Please input the TITLE of Tab {i + 1} : ')
        url = input(f'Please input the URL of Tab {i + 1} : ')

        if url.startswith("https://") or url.startswith("http://"):  # https://www.w3schools.com/python/ref_string_startswith.asp - startswith function in strings
            new_tab = {title: url}
            tabs.append(new_tab)
            print(f"You opened {new_tab} tab successfully!")
        else:
            print("Your input is invalid!! please start the URL with https:// or http://")

    print("\nyou opened these tabs : ", tabs)


def close_tab():
    if not tabs:                               # same as if tabs == [], simplified to fix "Expression can be simplified" weak warning.
        print("\nThere are no tabs open for you to close.")
        return

    print("\nThe opened tabs are of the following : ")

    for i in range(len(tabs)):  # for loop for displaying our tabs, so that we know which tab index to close.
        print(f"{i + 1}. {tabs[i]}")

    close_index = input("\nEnter the number of the tab you want to close OR press ENTER to close the last tab : ")
    if close_index == "":  # if empty input, means we remove the last TAB
        closed_tab = tabs.pop()  # https://www.w3schools.com/python/ref_list_pop.asp method used to CLOSE the last tab directly from the users tabs list
        print(f"\nYou closed the last tab {closed_tab}")
    else:
        close_index = int(close_index)
        if 1 <= close_index <= len(tabs):
            closed_tab = tabs.pop(close_index - 1)
            print(f"\nYou closed the last tab {closed_tab}")
        else:
            print("\nInvalid Number. No tab closed")
            return


def switch_tab():
    if not tabs:
        print("\nThere are no tabs opened.")
        return

    print("\nThe opened tabs are of the following indexes: ")

    for i in range(len(tabs)):  # for loop for displaying our tabs, so that we know which tab index to open.
        print(f"\n{i + 1}. {tabs[i]}")

    switch_index = input("Enter the Number of the tab you want to display the HTML content for : ")
    url = ""
    if switch_index == "":
        for key, value in tabs[len(tabs) - 1].items():
            url = value
    else:
        switch_index = int(switch_index)
        for key, value in tabs[len(tabs) - 1].items():
            url = value
        if 1 <= switch_index <= len(tabs):
            print(f"\nYou opened the last tab {switch_tab}")
            content = get_html_content(url)
            print(content)
        else:
            print("Invalid Number. No tabs displayed.")


def display_all_tabs():
    if not tabs:
        print("\nThere are no tabs opened")
        return

    else:
        print("\nThe opened tabs are the following : ")
        for i in range(len(tabs)):
            for key, value in tabs[i].items():
                title = key
                print(f"{title}")


def open_nested_tab():
    if not tabs:
        print("\nThere are no tabs opened")
        return
    else:
        print("Where would you like to open the nested tab : ")

        for i in range(len(tabs)):
            print(f"\n{i + 1}. {tabs[i]}")

        index_parent_tab = int(input("Enter the number of the parent tab you want to add tabs too  :  "))
        index_parent_tab -= 1

        if tabs[index_parent_tab] in tabs != []:
            title = input("Enter the title of the nested tab : ")
            url = input("Enter the url of the nested tab : ")

            if url.startswith("https://") or url.startswith("http://"):
                new_nested_tab = {title: url}
                tabs[index_parent_tab].update(new_nested_tab)  # The update method in dictionaries
                # https://www.w3schools.com/python/ref_dictionary_update.asp

            else:
                print("Your input URL is wrong. Make sure it starts with https:// or http://")
                return

    print("list of the opened tabs now are : ", tabs)


def clear_all_tabs():
    tabs.clear()
    print("***********You just cleared all of your tabs***********")


def save_tabs():
    # JSON = DICTIONARY
    folder_path = input("Please enter a file path to save the current state of open tabs  -  ")
    file_name = input("Enter the file name & type you want to save in your file path  -  ")

    exact_path = os.path.join(folder_path, file_name)  # used to join the 2 parameters with \ or / depending on the users OS.
    with open(exact_path, mode="w") as file:      # https://realpython.com/working-with-files-in-python/ - open() opens files for writing and returns a file handle.
        resultant_dict = {"tabs": tabs.copy()}           # here we are creating a copy of the opened tabs.
        contents = {}                                                  # {"url": "content", "url2".....}

        # loop over the tabs and scrape their content to be saved in the contents dict.
        for tab in resultant_dict["tabs"]:
            for key, value in tab.items():
                print(f"Scrapping {value} content...")
                contents[value] = get_html_content(value)        # for each key URL. we place the Prettified html from the function.

        resultant_dict["contents"] = contents
        json_string = json.dumps(resultant_dict, indent=4)  # https://www.w3schools.com/python/python_json.asp - used to convert Python object to JSON
        file.write(json_string)                                                   # https://realpython.com/working-with-files-in-python/  -  writing the data

        print(f"\nWritten to {exact_path}")



def import_tabs():
    folder_path = input("Please enter a file path to open  -  ")
    file_name = input("Enter the file name & type you want to open in your file path  -  ")

    exact_path = os.path.join(folder_path, file_name)
    with open(exact_path, mode="r") as file:   # r to read the file
        data = json.load(file)                                # load the data from the file using load method - https://www.geeksforgeeks.org/json-load-in-python/
        tabs = data["tabs"].copy()
        print(f"\nloaded tabs: {tabs}")


def display_menu():
    print(
        "\nHello USER, you just entered the advanced browser stimulation :) \nThis is your main menu: \n1. Open Tab \n2. Close Tab \n3. Switch Tab \n4. Display All Tabs "
        "\n5. Open Nested Tab  \n6. Clear All Tabs \n7. Save Tabs \n8. Import Tabs \n9. Exit \n\nPlease choose a number from 1-9: ")


def main():
    print("****Welcome to the Advanced Browser Tabs Simulation****")
    choice = 0
    while choice != 9:
        display_menu()
        choice = int(input("\nEnter your choice   :   "))

        if choice == 1:
            open_new_tab()

        elif choice == 2:
            close_tab()

        elif choice == 3:
            switch_tab()

        elif choice == 4:
            display_all_tabs()

        elif choice == 5:
            open_nested_tab()

        elif choice == 6:
            clear_all_tabs()

        elif choice == 7:
            save_tabs()

        elif choice == 8:
            import_tabs()

        elif choice == 9:
            print("****You exited the program****")
            break

        else:
            print("Wrong input please, choose 1-9.")
            pass


main()