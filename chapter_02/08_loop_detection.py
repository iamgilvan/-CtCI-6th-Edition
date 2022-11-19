from chapter_02.linked_list import LinkedList

# is not correct one hundred percent
# # we need to explore other situations

def loop_detection(ll):
    fast = ll.head
    slow = ll.head.next

    while slow is not fast:

        if fast is None or fast.next is None:
            return None

        slow = slow.next
        fast = fast.next.next
    return fast

def test_loop_detection():
    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    tests = [
        (looped_list, loop_start_node),
    ]

    for ll, expected in tests:
        assert loop_detection(ll) == expected

if __name__ == "__main__":
    test_loop_detection()