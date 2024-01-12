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

배열구조의 스택
```python
capacity = 10 # 스택 용량
array = [None]*capacity #요소 배열
top = -1 #상단의 인덱스 초기화
```
-----

### 큐의 클래스 구현
```python

```
