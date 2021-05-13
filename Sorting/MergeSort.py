from Lists import Queue


def MergeSort(tab):
    if len(tab) < 2:
        return tab[:]
    else:
        mid = int(len(tab) / 2)
        left = MergeSort(tab[:mid])
        right = MergeSort(tab[mid:])
        return merge(left, right)


def merge(left, right):
    result = []
    q1 = Queue.Queue(len(left))
    q2 = Queue.Queue(len(right))
    for i in range(len(left)):
        q1.enqueue(left[i])
    for i in range(len(right)):
        q2.enqueue(right[i])
    while not q1.isEmpty() and not q2.isEmpty():
        if str(q1.queue[q1.head]) < str(q2.queue[q2.head]):
            result.append(q1.dequeue())
        else:
            result.append(q2.dequeue())
    while not q1.isEmpty():
        result.append(q1.dequeue())
    while not q2.isEmpty():
        result.append(q2.dequeue())
    return result


tab = [9, 5, 4, 3, 2, 1, 6, 7, 8, -1, "h", "a"]
sorted = MergeSort(tab)
print(sorted)
