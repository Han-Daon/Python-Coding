>## input()    
-input함수는 무조건 **문자열** 형태로 반환 -> 정수로 변환시 int 필수

```python
x = int(input("첫번째 정수를 입력하세요: "))
y = int(input("두번째 정수를 입력하세요: ")) #정수를 받음

name = input("수식 이름을 정하세요: ") #뮨자열을 받음
```

>## ord('A') / chr(65)
-ord는 문자의 코드값
-chr은 코드에 해당하는 문자

>## list.append()
>

># import randaom
>- 난수 생성하기
```python
import random
time = random.radint(1,24) #1부터 24사이에 랜덤하게 선택
sunny = random.choice([True, False]) #둘중 하나를 랜덤하게 선택
```

># import os
>- 컴퓨터 제어하기
```python
import os
command = input("명령을 입력하세요")

if command == "shutdown"
    print("컴퓨터가 곧 종료됩니다")
    input()
    os.system("shutdown \s \t 1")
```
