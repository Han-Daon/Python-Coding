Stack = LIFO
============
- push(e)
- pop()
- isEmpty()
- isFull()
- peek()
- size()

------

배열구조의 스택
```python
capacity = 10 # 스택 용량
array = [None]*capacity #요소 배열
top = -1 #상단의 인덱스 초기화
```
-----

### 스택의 연산
```python
def isEmpty() :
    if top == -1 :
    return Ture
    else:
    return False

def is Full :
    return top == capacity

def push(e):
    if not isFull():
        top +=1
        array[top] = e
    else :
         print("Stack overflow")
         exit()

def pop() :
    if not isEmpty():
        top = -1
        return array[top+1]

    else :
        print("Stack underflow")
        exit()

def peek() :
    if not isEmpty():
        return array[top]
    else :
        pass
```

-----

### 스텍을 객체지향으로 구현하자(더 좋음)
```python
class ArrayStack : # 클래스의 이름
    def __init__(self, capacity) :
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self) : return self.top == -1
    def isFull(self) : return self.top == self.capacity-1

    def push(self, item) :
        if not self.isFull() :
            self.top +=1
            self.array[self.top] = item
        else : pass

    def pop(self) :
        if not self.isEmpty() :
            self.top -=1
            return self.array[self.top +1]
        else : pass

    def peek(self) :
        if not self.isEmpty():
            return self.arrat[self.top]
        else : pass

```
