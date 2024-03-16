class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseList(head):
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev

def insertionSortList(head):
    if not head or not head.next:
        return head
    
    sortedList = head
    head = head.next
    sortedList.next = None
    
    while head:
        current = head
        head = head.next
        if current.value < sortedList.value:
            current.next = sortedList
            sortedList = current
        else:
            search = sortedList
            while search.next and search.next.value < current.value:
                search = search.next
            current.next = search.next
            search.next = current
    
    return sortedList

def getMiddle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def sortedMerge(a, b):
    dummy = ListNode(0)
    tail = dummy

    while a and b:
        if a.value <= b.value:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    if a:
        tail.next = a
    elif b:
        tail.next = b

    return dummy.next

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next

def appendToList(head, value):
    if not head:
        return ListNode(value)
    else:
        current = head
        while current.next:
            current = current.next
        current.next = ListNode(value)
        return head

head = None
for value in [4, 2, 1, 3]:
    head = appendToList(head, value)

def printList(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

print("Початковий список:")
printList(head)

sortedHead = insertionSortList(head)
print("Відсортований список:")
printList(sortedHead)

reversedHead = reverseList(sortedHead)
print("Реверсований список:")
printList(reversedHead)

secondListHead = None
for value in [5, 6, 7]:
    secondListHead = appendToList(secondListHead, value)

mergedHead = mergeTwoLists(reversedHead, secondListHead)
print("Об'єднаний відсортований список:")
printList(mergedHead)


