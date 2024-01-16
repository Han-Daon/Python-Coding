List
============
- insert(pos, e)
- delete(pos)
- getEntry(pos) #pos위치에 있는 요소를 삭제하지 않고 반환
- isEmpty()
- isFull()
- size()    
    
- 노드 : 하나의 데이터와 하나 이상의 링크를 가짐
- 링크 : 다르노드를 가리키는 변수
------

### 단순연결 리스트 : LinkedList
#### 노트 클래스 구현
```python
class Node : 
    def __init__(self, elem, link = None):
        self.data = elem #데이ㅓ 생성및초기화
        self.link = link #링크 생성 및 초기화
    
#새로운 노드를 뒤에 추가하는 append 연산        

    def append (self, node) :
        if node if not None :
            node.link = self.link
            self.link = node    

# 다음 노드를 연결 구조에서 꺼내는 Node 클래스의 popNext연산 
  
    def popNext (self):
        next = self.link
        if next is not None :
            self.link = next.link
        return next #다음 노드로 반환
```
### 리스트 클래스 구현
```python

class LinkedList:
    def __init__(self):
        self.head = None
                        
#연산 포화 공백 상태 검사
    def isEmpty(self):
        return self.head == None
    
    def isFull (self):
        return False
    
    def getNode(self, pos) :
        if pos < 0 : return None #잘못된 위치 none 반환
        ptr = self.head # 시작 위치
        for i in range(pos): #머리노드에서부터 링크를 따라 pos번 이동하면 pos 위치의 노드에 도착, 위치는 0부터 시작
            if ptr == None :
                return None
            ptr = ptr.link 
        return ptr
    
    def getEntry(self, pos) :
        node = self.getNode(pos) #pos번째 노드 구함 
        if node == None : #해당 노드가 없는 경우
            return None
        else: #있는 경우 데이터 필드 반환
            return node.data 
            
#LinkedList 연산: 삽입 연산 insert(pos, e)

    def insert(self, pos, e) :
        node = Node(e, None)
        before ==self.getNode(pos-1) #삽입할 위치 이전 노드 탐색
        if before == None:
            node.link = self.head
            self.head = node
        else : #아닌경우 before뒤에 추가
            before.append(node)

#삭제 연산 delete(pos)
    
    def delete(self, pos) :
        before = self.getNode([pos-1])
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.link
            return before
        else:
            return before.popNext()     
```

### 이중리스트 노드 구현
```python
class DNode:
    def __init__(self, elem, prev= None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next
        
#더블 노드의 append 연산
    def append(self, node): #self 다음에 노드를 넣는 연산
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None :
                node.next.prev = node
            self.next = node
            
            
#DNode의 popNext 연산

    def popNext(self):
        node = self.next #삭제할 노드
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self #그 노드의 이전 노드는 self
            return node
```

### 이중리스트 데이터 구현
```python
class DbLinkedList:
    def __init__(self):
        self.head = None
        
    #화면 출력
    def display (self, msg = "DblinkedList:"):
        print(msg, end = "")
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='<=>') #이중 연결은 <=> 로 표시
            ptr = ptr.next # 다음 노드로 이동
        print("None")
        
    # insert(pos, e)
    
    def insert(self, pos, e):
        node = DNode(e) # 삽입할 이중 연결 구조의 노드 생성
        before = self.getNode(pos -1) #삽입할 위치 이전 노드 탐색
        if before == None : # 머리 노드로 삽입하는 경우
            node.next = self.head
            if node.next is not None :
                node.next.prev = node
            self.head = node
        else :
            before.append(node)
            
    #delete(pos) 연산
    
    def delete(self, pos) :
        before = self.getNode(pos -1)
        if before == None : #머리 노드 삭제의 경우
            before =  self.head
            if self.head is not None :
                self.head = self.head.next
            if self.head is not None :
                self.head.prev = None
            return before
        else :
            before.popNext()
```
