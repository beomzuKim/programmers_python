class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        
        # prev가 마지막 node일때
        if prev.next == None:
            self.tail = prev
            curr = None
        
        #리스트 맨끝의 node를 삭제할때
        if curr.next == None:
            self.tail = curr
            self.nodeCount -= 1
        
        else:
            prev.next = curr.next
            self.nodeCount -= 1
        
        return curr
            
    def popAt(self, pos):
        # pos가 리스트 범위 밖일때
        if pos < 0 or pos > self.nodeCount:
            raise IndexError
        
        # pos가 범위 안일때 (1 < pos < nodeCount)
        if pos > 1 and pos <= self.nodeCount:
            return self.popAfter(pos)
            


def solution(x):
    return 0
