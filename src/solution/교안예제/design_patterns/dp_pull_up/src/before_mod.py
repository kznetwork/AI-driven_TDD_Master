class Developer:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def get_details(self):
        return f"{self.name} (Developer, Language: {self.language})"


class Manager:
    def __init__(self, name, team_size):
        self.name = name
        self.team_size = team_size

    def get_details(self):
        return f"{self.name} (Manager, Team Size: {self.team_size})"
