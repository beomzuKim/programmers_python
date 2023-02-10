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
        # prev가 마지막 node 일때
        if prev.next == None: 
            return None
        
        # prev가 마지막 node가 아니므로 curr 정의
        curr = prev.next
        
        # 리스트 맨 끝의 node를 삭제할때
        if curr.next == None: 
            prev.next = None
            self.tail = prev
            
        # 모두 아닌 정상인 경우
        else :
            prev.next = curr.next

        # 데이터 처리 이후 nodeCount 조정 및 return
        self.nodeCount -=1
        return curr.data
            
    def popAt(self, pos):
        # pos가 리스트 범위 밖일때
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        # pos가 범위 안일때 (1 < pos < nodeCount)
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)
            


def solution(x):
    return 0
