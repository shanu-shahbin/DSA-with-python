class DoublyNode:
    """
    Represents a node in a doubly linked list.
    Each node has a 'val' (value), 'next' (pointer to next node), and 'prev' (pointer to previous node).
    """

    def __init__(self, val, next=None, prev=None):
        """
        Initialize a node with a value, next pointer, and previous pointer.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.val = val  # Value of the node
        self.next = next  # Pointer to the next node
        self.prev = prev  # Pointer to the previous node

    def __str__(self):
        """
        Return the string representation of the node's value.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return str(self.val)


# Initialize the doubly linked list with a single node
head = tail = DoublyNode(1)
print(head)  # O(1)


# Display the linked list from head to tail - O(n)
def display(head):
    """
    Traverse and display the doubly linked list from head to tail.
    Time Complexity: O(n), where n is the number of nodes.
    Space Complexity: O(n), since elements are stored in a list temporarily.
    """
    curr = head
    elements = []
    while curr:  # Traverse until the end
        elements.append(str(curr.val))  # Add the value to the list
        curr = curr.next  # Move to the next node
    print(' <-> '.join(elements))  # Print the nodes in 'node <-> node' format


display(head)  # Initially display the single node


# Insert a node at the beginning of the list - O(1)
def insert_at_beginning(head, tail, val):
    """
    Insert a new node at the beginning of the list.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    new_node = DoublyNode(val, next=head)  # Create a new node pointing to the old head
    head.prev = new_node  # Set the old head's previous pointer to the new node
    return new_node, tail  # Return the new head, tail remains the same


# Insert a node at the end of the list - O(1)
def insert_at_end(head, tail, val):
    """
    Insert a new node at the end of the list.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    new_node = DoublyNode(val, prev=tail)  # Create a new node pointing to the old tail
    tail.next = new_node  # Set the old tail's next pointer to the new node
    return head, new_node  # Return the head, the new node becomes the tail


# Perform insertions and display the list after each insertion
head, tail = insert_at_beginning(head, tail, 3)  # Insert at the beginning
display(head)

head, tail = insert_at_end(head, tail, 7)  # Insert at the end
display(head)


# Traverse the list in both directions (forward and backward) - O(n)
def traverse_both_ways(head, tail):
    """
    Traverse the doubly linked list in both forward and backward directions.
    Time Complexity: O(n), where n is the number of nodes.
    Space Complexity: O(n) for storing elements during traversal.
    """
    # Traverse forward (from head to tail)
    print("Forward traversal:")
    curr = head
    while curr:
        print(curr, end=' ')
        curr = curr.next
    print()

    # Traverse backward (from tail to head)
    print("Backward traversal:")
    curr = tail
    while curr:
        print(curr, end=' ')
        curr = curr.prev
    print()


# Call the traverse function
traverse_both_ways(head, tail)


# Search for a value in the list - O(n)
def search(head, val):
    """
    Search for a node with the given value in the list.
    Time Complexity: O(n), where n is the number of nodes.
    Space Complexity: O(1), as no extra space is used other than variables.
    """
    curr = head
    while curr:
        if curr.val == val:  # If value is found
            return True
        curr = curr.next  # Move to the next node
    return False  # If the value is not found, return False


# Searching for values in the list
found = search(head, 7)  # Searching for 7 (should return True)
print(f"Value 7 found: {found}")

found = search(head, 5)  # Searching for 5 (should return False)
print(f"Value 5 found: {found}")
