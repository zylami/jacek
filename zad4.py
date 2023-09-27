class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while head and head.next:
        # Zapisujemy wskaźniki na pary węzłów
        first_node = head
        second_node = head.next

        # Zamieniamy miejscami pary
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        # Przesuwamy wskaźniki do następnej pary
        prev = first_node
        head = first_node.next
    
    return dummy.next

# Funkcja do konwertowania listy na obiekt ListNode
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for item in lst[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Funkcja do konwertowania obiektu ListNode na listę
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Przykład użycia
if __name__ == "__main__":
    input_list = [1, 2, 3, 4]
    input_head = list_to_linked_list(input_list)

    print("Input:")
    input_list = linked_list_to_list(input_head)
    print(input_list)

    # Wywołanie funkcji swap_pairs
    output_head = swap_pairs(input_head)

    print("Output:")
    output_list = linked_list_to_list(output_head)
    print(output_list)

