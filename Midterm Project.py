import requests  # pip install requests used this in terminal  https://pypi.org/project/beautifulsoup4/
from bs4 import BeautifulSoup  # pip install beautifulsoup4 used this in terminal

tabs = []


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

    print("you opened these tabs : ", tabs)


open_new_tab()


def close_tab():
    if not tabs:  # same as if tabs == [], simplified to fix "Expression can be simplified" weak warning.
        print("\nThere are no tabs open for you to close.")
        return

    print("\nThe opened tabs are of the following indexes : ")

    for i in range(len(tabs)):  # for loop for displaying our tabs, so that we know which tab index to close.
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


def switch_tab():
    if not tabs:
        print("There are no tabs opened.")
        return

    print("\nThe opened tabs are of the following indexes: ")

    for i in range(len(tabs)):  # for loop for displaying our tabs, so that we know which tab index to open.
        print(f"\n{i + 1}. {tabs[i]}")

    switch_index = input("Enter the index of the tab you want to display the HTML content for : ")
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
            response = requests.get(url)  # Send an HTTP GET request to the URL of the selected tab - https://www.w3schools.com/PYTHON/ref_requests_get.asp
            html_content = response.text  # Get the HTML content of the response content above
            soup = BeautifulSoup(html_content, 'html.parser')  # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start
            print(soup.prettify())  # https://pypi.org/project/beautifulsoup4/ it is the BeautifulSoup object method that prettifies the content.
        else:
            print("Invalid Index. No tabs displayed.")


switch_tab()

