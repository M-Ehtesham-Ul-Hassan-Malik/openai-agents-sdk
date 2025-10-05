# Python Dataclasses — A Complete Guide

## 📌 Introduction
In Python, writing classes often involves a lot of repetitive boilerplate code — defining `__init__`, `__repr__`, `__eq__`, and sometimes `__hash__` methods just to store and compare data.

To solve this, **`dataclasses`** were introduced in **Python 3.7** via [PEP 557](https://peps.python.org/pep-0557/). They provide a decorator and functions for automatically adding special methods to classes that primarily store data, significantly reducing code duplication.

---

##  Why Dataclasses Were Introduced
Before dataclasses, developers often relied on:
- Manually writing `__init__` and other dunder methods
- Using **namedtuples** (immutable, limited functionality)
- Using **attrs** library (third-party dependency)

Dataclasses were added to:
- Make **data containers** easier to create
- Reduce boilerplate code
- Keep classes **readable** and **maintainable**
- Provide **immutability** (optional) and **type hinting** support

---

## Benefits of Dataclasses

### 1. Less Boilerplate
Instead of manually writing `__init__`, `__repr__`, and `__eq__`, `@dataclass` generates them automatically.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```
Equivalent traditional class:
```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age
```

### 2. Built-in Type Hints

- Dataclasses work seamlessly with Python type hints.

- The type annotations define both the type and the fields for `__init__`.

### 3. Default Values & Factories
You can set default values or use default_factory for mutable types like lists or dicts.

```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    tags: list[str] = field(default_factory=list)
```

### 4. Immutability (frozen classes)
Set `frozen=True` to make instances immutable (like tuples).

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

### 5. Comparison Methods
By default, dataclasses generate `__eq__` (and optionally ordering methods) so objects can be compared without extra code.

### 6. Cleaner, More Readable Code
Code becomes shorter, easier to read, and less error-prone.

## Features at a Glance
| Feature                  | Dataclasses | Regular Class |
| ------------------------ | ----------- | ------------- |
| Auto `__init__`          | ✅           | ❌ (manual)    |
| Auto `__repr__`          | ✅           | ❌ (manual)    |
| Auto `__eq__`            | ✅           | ❌ (manual)    |
| Auto ordering (`__lt__`) | ✅ (opt-in)  | ❌ (manual)    |
| Type hints support       | ✅           | ✅             |
| Immutability             | ✅           | ✅ (manual)    |
| `default_factory`        | ✅           | ❌ (manual)    |

## When to Use Dataclasses

**Use** when:

- Your class is mainly storing data
- You want less boilerplate and better maintainability
- You want built-in comparison and readable output

**Avoid** when:

- Your class is primarily behavior-based (lots of methods, little data)
- You need full control over all dunder methods

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    email: str | None = None
    tags: list[str] = field(default_factory=list)

    def is_adult(self) -> bool:
        return self.age >= 18

# Usage
p = Person("Alice", 25)
print(p)               # Person(name='Alice', age=25, email=None, tags=[])
print(p.is_adult())    # True
```

