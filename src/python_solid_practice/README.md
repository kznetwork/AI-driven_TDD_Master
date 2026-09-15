# Python으로 배우는 SOLID 원칙

## 단일 책임 원칙(SRP)

단일 책임 원칙(Single Responsibility Principle)은 **클래스가 변경되어야 하는 이유를 하나만 가져야 한다**는 원칙입니다.

## 적용 전

[`before_srp.py`](./before_srp.py)의 `Guitar`는 두 책임을 함께 가집니다.

- 개별 기타의 일련번호와 가격을 관리합니다.
- 기타의 사양을 관리하고 원하는 사양과 일치하는지 비교합니다.

따라서 사양 항목이나 비교 규칙이 바뀌면 개별 상품을 나타내는 `Guitar`도 수정해야 합니다.

## 적용 후

[`after_srp.py`](./after_srp.py)는 책임을 다음과 같이 분리합니다.

- `Guitar`: 개별 기타의 일련번호, 가격, 사양 참조를 관리합니다.
- `GuitarSpec`: 기타의 사양과 사양 비교 규칙을 관리합니다.

이제 사양 항목이나 비교 규칙이 바뀌어도 주로 `GuitarSpec`만 수정하면 됩니다. `GuitarSpec`은 검색 조건으로도 재사용할 수 있습니다.

## 실행 방법

Python 3가 설치된 터미널에서 프로젝트 디렉터리로 이동한 뒤 실행합니다.

```powershell
python before_srp.py
python after_srp.py
```

두 파일 모두 다음 결과를 출력합니다.

```text
V95693: Stratocaster
Price: $1499.95
Matches preferred guitar: True
```

## 개방-폐쇄 원칙(OCP)

개방-폐쇄 원칙(Open-Closed Principle)은 **소프트웨어 요소가 확장에는 열려 있고, 기존 코드의 수정에는 닫혀 있어야 한다**는 원칙입니다.

[`ocp.py`](./ocp.py)에서는 추상 클래스 `Shape`가 모든 도형이 따라야 하는 `calculate_area()` 인터페이스를 정의합니다. `Rectangle`, `Circle`, `Triangle`은 각자의 면적 계산 방법을 구현합니다.

OCP가 적용된 핵심은 `total_area()`입니다. 이 함수는 구체적인 도형 종류를 검사하지 않고 `Shape`의 `calculate_area()`만 호출합니다. 따라서 새 도형을 추가할 때는 다음 두 단계만 필요합니다.

1. `Shape`를 상속하는 새 클래스를 만듭니다.
2. 새 클래스에 `calculate_area()`를 구현합니다.

기존 `Shape`, 도형 클래스, `total_area()`는 수정할 필요가 없습니다. 즉, 새 클래스 추가를 통한 **확장에는 열려 있고**, 이미 검증한 면적 합산 코드의 **수정에는 닫혀 있습니다**.

### 실행 방법

```powershell
python ocp.py
```

예상 결과:

```text
Rectangle: 20.00
Circle: 28.27
Triangle: 12.00
Total: 60.27
```

## 리스코프 치환 원칙(LSP)

리스코프 치환 원칙(Liskov Substitution Principle)은 **하위 타입이 부모 타입의 약속을 깨지 않으면서 부모 타입을 대신할 수 있어야 한다**는 원칙입니다.

### 적용 전: LSP 위반

[`before_lsp.py`](./before_lsp.py)의 `Bird`는 모든 새가 날 수 있다고 가정하고 `fly()`를 정의합니다. 날지 못하는 `Ostrich`는 이 계약을 지킬 수 없어 `fly()`에서 예외를 발생시킵니다.

`make_bird_fly()`에 `Bird`의 하위 타입인 `Ostrich`를 전달하면 정상적으로 비행하지 못하므로, 부모 타입을 하위 타입으로 안전하게 치환할 수 없습니다.

```powershell
python before_lsp.py
```

```text
The sparrow is flying.
LSP violation: Ostriches cannot fly.
```

### 적용 후: 역할 분리

[`after_lsp.py`](./after_lsp.py)는 모든 새의 공통 동작인 `eat()`만 `Bird`에 둡니다. 비행 능력은 `Flyable` 인터페이스로 분리하고, 날 수 있는 `Sparrow`만 이를 구현합니다.

- `Sparrow`와 `Ostrich`는 모두 `Bird` 대신 사용해 `eat()`을 수행할 수 있습니다.
- `make_fly()`에는 `Flyable`을 구현한 객체만 전달합니다.
- `Ostrich`는 지킬 수 없는 `fly()` 계약을 상속하거나 예외로 무효화하지 않습니다.

```powershell
python after_lsp.py
```

```text
The sparrow is eating.
The ostrich is eating.
The sparrow is flying.
```

## 인터페이스 분리 원칙(ISP)

인터페이스 분리 원칙(Interface Segregation Principle)은 **클라이언트가 사용하지 않는 메서드에 의존하도록 강요받아서는 안 된다**는 원칙입니다.

### 적용 전: ISP 위반

[`before_isp.py`](./before_isp.py)의 `Bird` 인터페이스는 `sing()`, `eat()`, `fly()`를 모두 강제합니다. 날지 못하는 `Penguin`도 불필요한 `fly()`를 구현해야 하며, 호출하면 예외가 발생합니다.

```powershell
python before_isp.py
```

```text
The penguin is singing.
The penguin is eating.
ISP violation: Penguins cannot fly.
```

### 적용 후: 인터페이스 분리

[`after_isp.py`](./after_isp.py)는 인터페이스를 역할별로 나눕니다.

- `Bird`: 모든 새에게 필요한 `sing()`, `eat()`을 정의합니다.
- `FlyableBird`: 날 수 있는 새에게만 필요한 `fly()`를 정의합니다.
- `Penguin`: `Bird`만 구현합니다.
- `Eagle`: `Bird`와 `FlyableBird`를 모두 구현합니다.

이제 각 클래스는 실제로 필요한 메서드에만 의존하며, `Penguin`에 의미 없는 `fly()` 구현이나 예외 처리가 필요하지 않습니다.

```powershell
python after_isp.py
```

```text
The penguin is singing.
The penguin is eating.
The eagle is singing.
The eagle is eating.
The eagle is flying.
```

## 의존 역전 원칙(DIP)

의존 역전 원칙(Dependency Inversion Principle)은 **고수준 모듈과 저수준 모듈이 구체 구현이 아니라 추상화에 의존해야 한다**는 원칙입니다.

### 적용 전: DIP 위반

[`before_dip.py`](./before_dip.py)의 고수준 모듈 `Notification`은 내부에서 저수준 모듈 `EmailService`를 직접 생성합니다. SMS 같은 다른 전송 방식을 사용하려면 `Notification`의 코드를 수정해야 합니다.

```powershell
python before_dip.py
```

```text
Email sent: Your order has shipped.
```

### 적용 후: 추상화와 생성자 주입

[`after_dip.py`](./after_dip.py)는 다음과 같이 의존 방향을 바꿉니다.

- `MessageService`: `send()` 계약을 정의하는 추상 인터페이스입니다.
- `EmailService`, `SMSService`: `MessageService`를 구현합니다.
- `Notification`: 구체 서비스를 생성하지 않고 생성자로 `MessageService`를 주입받습니다.

`Notification`은 구체적인 전송 방식을 알 필요가 없습니다. `MessageService`를 구현한 새로운 서비스를 만들어 생성자에 전달하면 `Notification`을 수정하지 않고 동작을 교체할 수 있습니다.

```powershell
python after_dip.py
```

```text
Email sent: Your order has shipped.
SMS sent: Your verification code is 1234.
```
