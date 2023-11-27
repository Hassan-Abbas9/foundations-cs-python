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

    def append(self, value): # 0(1) because we add directly to the end of the LinkedList
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_nodes(self): # 0(n) : n being the looping through the LinkedList until the end of it
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get(self, index): # 0(n) : n being the looping through the Linkedlist until the end of it
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def remove(self, index): # 0(n) : n being the looping through the Linkedlist until the end of it
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

    def add_vertex(self, vertex): # 0(1)
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2): # 0(1)
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2): # 0(n) : n being the looping through the list of edges
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex): # 0(n2) : n being the looping through all the list of vertices & Edges
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


class Stack:       # copied and understood the code from
    # https://www.sanfoundry.com/python-program-check-string-palindrome-using-stack/
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data): # 0(1)
        self.items.append(data)

    def pop(self): # 0(1)
        return self.items.pop()


class Student:
    def __init__(self, name, midterm_grade, final_grade, good_attitude):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude

    def priority_for_interview(self, other_student): # 0(1)
        if self.good_attitude != other_student.good_attitude:
            return self.good_attitude > other_student.good_attitude
        elif self.final_grade != other_student.final_grade:
            return self.final_grade > other_student.final_grade
        else:
            return self.midterm_grade > other_student.midterm_grade


class PriorityQueue:
    def __init__(self):
        self.students = []

    def add_student(self, student): # 0(1)
        self.students.append(student)

    def interview_student(self): # 0(n) : n being the iterating through the list of students to find the highest priority.
        if self.students:
            highest_priority_student = self.students[0]
            for student in self.students[1:]:
                if student.priority_for_interview(highest_priority_student):
                    highest_priority_student = student

            self.students.remove(highest_priority_student)
            print(f"Interviewing {highest_priority_student.name}")
        else:
            print("No students to interview")


def student_priority_list():

    priority_queue = PriorityQueue()

    while True:
        print("\nHR Office Menu:")
        print("a. Add a student")
        print("b. Interview a student")
        print("c. Return to main menu")

        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            name = input("Enter student name: ")
            midterm_grade = int(input("Enter midterm grade (0-100): "))
            final_grade = int(input("Enter final grade (0-100): "))
            good_attitude = input("Does the student have a good attitude? (True/False): ").lower() == 'true'
            student = Student(name, midterm_grade, final_grade, good_attitude)
            priority_queue.add_student(student)
            print(f"{name} added to the priority queue.")

        elif choice == 'b':
            priority_queue.interview_student()

        elif choice == 'c':
            print("\nYou return to the Main Menu")
            main()

        else:
            print("Invalid choice. Please choose again.")


def stack_function_menu():
    while True:
        s = Stack()
        text = input('Please enter the string: ')

        for character in text:
            s.push(character)

        reversed_text = ''
        while not s.is_empty():
            reversed_text = reversed_text + s.pop()

        if text == reversed_text:
            print('The string is a palindrome.')
            print('\nYou return to the Main menu')
            main()
        else:
            print('The string is not a palindrome.')
            print('\nYou return to the Main menu')
            main()


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
        sub_choice = input("\na. Add vertex\nb. Add edge\nc. Remove vertex\nd. Remove edge\ne. Display vertices with a degree of X or more.\nf. Return to main menu \nEnter your choice: ").lower()

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

        elif sub_choice == "f":
            print("\nYou return to the Main Menu")
            main()

        else:
            print("Invalid choice. Please enter a valid option.")


def main():
    print("1. Singly LinkedList \n2. Check Palindrome \n3. Priority Queue \n4. Evaluate an Infix Expression \n5. Graph \n6. Exit")

    choice = int(input("\nEnter the choice you want : "))

    if choice == 1:
        linked_list_menu()

    elif choice == 2:
        stack_function_menu()

    elif choice == 3:
        student_priority_list()

    elif choice == 5:
        graph_menu()

    elif choice == 6:
        print("\nyou exited the program.")
        return

    else:
        print("Invalid choice. Please enter a valid option.")


if __name__ == '__main__':
    main()
