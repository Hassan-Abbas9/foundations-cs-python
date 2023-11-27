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


class Graph:
    def __init__(self):
        self.adj_list ={}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


def linked_list_menu():

    while True:
        value = int(input("Enter the initial value for the linked list: "))

        linked_list = LinkedList(value)

        while True:
            print("\na. Add Node")
            print("b. Display Nodes")
            print("c. Delete Node")
            print("d. Return to main menu")

            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == "a":
                value = int(input("Enter the value to add: "))
                linked_list.append(value)
            elif sub_choice == "b":
                linked_list.print_nodes()
            elif sub_choice == "c":
                value = int(input("Enter the value to INDEX of the value to delete: "))
                linked_list.remove(value)
            elif sub_choice == "d":
                break
            else:
                print("Invalid choice. Please enter a valid option.")


def graph_menu():
    graph = Graph()

    while True:
        sub_choice = input("\na. Add vertex\nb. Add edge\nc. Remove vertex\nd. Remove edge\ne. Display vertices with a degree of X or more.\nf. Return to main menu\nEnter your choice: ").lower()

        if sub_choice == "a":
            vertex = input("Enter the vertex to add: ")
            if graph.add_vertex(vertex):
                print(f"Vertex {vertex} added.")
            else:
                print(f"Vertex {vertex} already exists.")

        elif sub_choice == "b":
            v1 = input("Enter the first vertex: ")
            v2 = input("Enter the second vertex: ")
            if graph.add_edge(v1, v2):
                print(f"Edge between {v1} and {v2} added.")
            else:
                print("Vertices do not exist.")

        elif sub_choice == "c":
            vertex = input("Enter the vertex to remove: ")
            if graph.remove_vertex(vertex):
                print(f"Vertex {vertex} removed.")
            else:
                print(f"Vertex {vertex} does not exist.")

        elif sub_choice == "d":
            v1 = input("Enter the first vertex: ")
            v2 = input("Enter the second vertex: ")
            if graph.remove_edge(v1, v2):
                print(f"Edge between {v1} and {v2} removed.")
            else:
                print("Edge does not exist.")


        else:
            print("Invalid choice. Please enter a valid option.")


def main():
    print("1. Singly LinkedList \n2. Check Palindrome \n3. Priority Queue \n4. Evaluate an Infix Expression \n5. Graph \n6. Exit")

    choice = int(input("\nEnter the choice you want : "))

    if choice == 1:
        linked_list_menu()

    elif choice == 5:
        graph_menu()

    else:
        print("Invalid choice. Please enter a valid option.")


main()
