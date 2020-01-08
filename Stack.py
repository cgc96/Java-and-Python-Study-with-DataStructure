class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if not self.head:
            return True
        return False

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None

        ret_data = self.head.data
        self.head = self.head.next
        return ret_data

    def top(self):
        if self.is_empty():
            return None

        return self.head.data

if __name__ == "__main__":
    s = Stack()

    n = int(input())
    numbers = []
    answer = []

    cur = 0

    for a in range(0, n):
        x = int(input())
        numbers.append(x)

    i = 1

    while not i == n+1:
        if s.is_empty() :
            answer.append('+')
            s.push(i)
            i += 1


        elif s.top() == numbers[cur]:
            answer.append('-')
            s.pop()
            cur += 1
        else :
            answer.append('+')
            s.push(i)
            i += 1

    checker = True
    while not s.is_empty() :
        if s.top() == numbers[cur]:
            cur += 1
            answer.append('-')
            s.pop()
        else:
            checker = False
            break


    if checker == True:
        for i in range(0, len(answer)):
             print( answer[i])
    else :
        print('NO')























