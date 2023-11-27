class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_value = Node(value)
        self.head = new_value
        self.tail = new_value
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_nodes(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

def main():
    value = int(input("Enter the initial value for the linked list: "))
    linked_list = LinkedList(value)

    while True:
        print("\na. Add Node")
        print("b. Display Nodes")
        print("c. Delete Node")
        print("d. Return to main menu")

        choice = input("Enter your choice: ").lower()

        if choice == "a":
            value = int(input("Enter the value to add: "))
            linked_list.append(value)
        elif choice == "b":
            linked_list.print_nodes()
        elif choice == "c":
            value = int(input("Enter the value to INDEX of the value to delete: "))
            linked_list.remove(value)
        elif choice == "d":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

main()
