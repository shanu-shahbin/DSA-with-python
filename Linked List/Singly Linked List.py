class SinglyNode:
    """
    Represents a node in a singly linked list.
    Each node has a 'val' (value) and 'next' pointer.
    """

    def __init__(self, val, next=None):
        """
        Initialize a node with a value and an optional next node.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.val = val  # The value stored in the node
        self.next = next  # Pointer to the next node

    def __str__(self):
        """
        Return the string representation of the node's value.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return str(self.val)


# Create the linked list nodes
Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)

# Link the nodes together
Head.next = A  # 1 -> 2
A.next = B     # 2 -> 3
B.next = C     # 3 -> 4

# Print the head node (start of the list)
print(Head)  # O(1)

# Traverse the linked list - O(n)
curr = Head
while curr:
    print(curr)  # Print the current node
    curr = curr.next  # Move to the next node

# Function to display the entire linked list
def display(head):
    """
    Traverse and display the linked list.
    Time Complexity: O(n), where n is the number of nodes.
    Space Complexity: O(n), since we store the elements in a list.
    """
    curr = head
    elements = []
    while curr:  # Traverse the list until the end
        elements.append(str(curr.val))  # Add the value to the list
        curr = curr.next  # Move to the next node
    print(' -> '.join(elements))  # Print the elements in a linked-list format

# Call display function to show the entire list
display(Head)

# Search function to find a value in the list
def search(head, val):
    """
    Search for a node with the given value in the linked list.
    Time Complexity: O(n), where n is the number of nodes.
    Space Complexity: O(1), since no additional space is used other than variables.
    """
    curr = head
    while curr:
        if val == curr.val:  # If the value is found, return True
            return True
        curr = curr.next  # Move to the next node
    return False  # If not found, return False

# Searching for a value (example: 7)
found = search(Head, 7)
print(f"Value 7 found: {found}")
