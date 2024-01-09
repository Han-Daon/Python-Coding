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

