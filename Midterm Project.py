def open_new_tab():
    title = input("please input the title of the new Tab : ")
    url = input ("Please input the URL of the new Tab : ")

    new_tab = {title : url}
    print("your open tabs", new_tab)

open_new_tab()
