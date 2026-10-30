from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name                         # Pull Up Field

    def get_details(self):                       # Pull Up Method — 뼈대는 부모가
        return f"{self.name} ({self.role()}, {self.extra()})"

    @abstractmethod
    def role(self): ...                          # 달라지는 부분만 자식이

    @abstractmethod
    def extra(self): ...


class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def role(self):
        return "Developer"

    def extra(self):
        return f"Language: {self.language}"


class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

    def role(self):
        return "Manager"

    def extra(self):
        return f"Team Size: {self.team_size}"
