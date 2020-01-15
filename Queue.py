#파이썬으로 만든 Queue class
import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:


    def __init__(self):
        self.head = None
        self.tail = None
        self.QueueSize = 0

    def front(self):
        if self.head == None:
            return -1
        else:
            return self.head.data

    def back(self):
        if self.tail == None:
            return -1
        else:
            return self.tail.data

    def is_empty(self):
        if self.head == None:
            return 1
        return 0

    def Enqueue(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.QueueSize += 1

    def Dequeue(self):
        if self.is_empty():
            return -1

        self.QueueSize -= 1
        ret_data = self.head.data
        self.head = self.head.next

        if self.head == None:
            self.tail = None
        return ret_data

    def Size(self):
        return self.QueueSize

#10845번 문제 : 큐

if __name__ == "__main__":
    Q = Queue()

    n = int(sys.stdin.readline())

    while n:
        n -= 1
        x = sys.stdin.readline().split()

        if x[0] == "back":
            print(Q.back())
        elif x[0] == "pop":
            print(Q.Dequeue())
        elif x[0] == 'size':
            print(Q.Size())
        elif x[0] == 'empty':
            print(Q.is_empty())
        elif x[0] == 'front':
            print(Q.front())
        else:
            num = int(x[1])
            Q.Enqueue(Node(num))

