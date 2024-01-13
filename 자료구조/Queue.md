Queue = FIFO
============
- enqueue(e) => append(e)
- dequeue() => pop()
- isEmpty() => len(L) ==0
- isFull() => false
- peek() => L(len(L)-1)
- size() => len(L)
- rear : 맨 마지막 요소의 위치    
- front : 첫번째 요소 바로 이전의 위치
     
### 원형 큐

- 전단 회전 : front <- (front + 1)%capacity
- 후단 회전 : rear <- (rear + 1)%capacity
------

### 큐의 클래스 구현
```python
class ArrayQueue :
    def __init__(self, capacity = 10) :
        self.capacity = capacity 
        self.array = [None]*capacity
        self.front = 0 #전단 인덱스 초기화
        self.rear = 0 #후단 인덱스 초기화
```
### 큐의 연산
```python        
    def enqueue (self, item) :
        if not self.isFull() :
            self.rear = (self.rear +1 )% self.capacity
            self.array[self.rear] = item
        else : pass # 오버플로우
        
    def dequeue(self) : 
        if not self.isEmpty() :
            self.front = (self.front+1)% self.capacity
            return self.array[self.front]
        else : pass
     
    def peek(self) :
        if not self.isEmpty() :
            return self.array[(self.front +1)]%self.capacity
        else : pass #언더플로우
        
    def size(self) :
        return (self.rear - self.front + self.capacity) %self.capacity
```

```python
    
    def display(self.msg) : # msg = 큐의 이름이나 메세지를 출력하기 위한 매개변수
        print(msg, end ='= [')
        for i in range(self.front+1, self.front+1+self.size()) :
            print(self.array[i%self.capacity], end=" ")
        print("]")                     
```
