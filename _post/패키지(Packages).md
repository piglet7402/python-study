# 패키지(Packages)

Created: Oct 26, 2020 9:40 AM
Updated: Oct 26, 2020 10:28 AM

# 패키지(Packages)

- 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해 줌
- 공동 작업이나 유지 보수 등 여러 면에서 유리
- 다른 모듈과 이름이 겹치더라도 더 안전하게 사용할 수 있음

### 패키지 안의 함수를 실행하는 방법 3가지

- **[예시 - 패키지 기본 구성 요소 준비하기]**

    ![%E1%84%91%E1%85%A2%E1%84%8F%E1%85%B5%E1%84%8C%E1%85%B5(Packages)%209a5e7bc92ddc4d3aabf434b7fa353ba2/Untitled.png](%E1%84%91%E1%85%A2%E1%84%8F%E1%85%B5%E1%84%8C%E1%85%B5(Packages)%209a5e7bc92ddc4d3aabf434b7fa353ba2/Untitled.png)

    ```python
    # echo.py

    def echo_test():
        print ("echo")
    ```

    ```python
    # render.py

    def render_test():
        print ("render")
    ```

- 모듈을 import하여 실행하는 방법
- import할 때 가장 마지막 항목은 반드시 모듈 또는 패키지여야만 함
- import할 때 가장 마지막 항목에 함수를 사용하는 것 불가능

```python
# test.py

import game.sound.echo
game.sound.echo.echo_test()
```

- 모듈이 있는 디렉터리까지를 from ... import하여 실행하는 방법

```python
# test.py

from game.sound import echo
echo.echo_test()
```

- 모듈의 함수를 직접 import하여 실행

```python
# test.py

from game.sound.echo import echo_test
echo_test()
```

## __**init**__**.py** 의 용도

- 해당 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할
- 파일이 없다면 패키지로 인식되지 않음

### 특정 디렉터리의 모듈을 *를 사용하여 import할 때

- 해당 디렉터리의 __init__.py 파일에 all 변수를 설정하고 import할 수 있는 모듈을 정의해 주어야 함 ← 정의 안하면 이름 오류(NameError)가 발생
- __all__과 상관없이 무조건 import되는 경우는 from a.b.c import * 에서 from의 마지막 항목인 c가 모듈인 경우

```python
# doit/game/sound/__init__.py

__all__ = ['echo']
# 디렉터리에서 * 기호를 사용하여 import할 경우 __all__에 정의된 모듈만 import된다
```

```python
# test.py

from game.sound import *
echo.echo_test()
```

### graphic 디렉터리의 render.py 모듈이 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면

```python
# render.py

from game.sound.echo import echo_test
def render_test():
    print ("render")
    echo_test()
```

또는

```python
# render.py

from ..sound.echo import echo_test

def render_test():
    print ("render")
    echo_test()
```

```python
# test.py

from game.graphic.render import render_test
render_test()
```