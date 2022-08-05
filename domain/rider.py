class Rider:

    general_points = 0
    mountain_points = 0
    sprint_points = 0


    def __init__(self, name, team, value):
        self.name = name
        self.team = team
        self.value = value

    def add_general_points(self, points):
        self.general_points += points

    def add_mountain_points(self, points):
        self.mountain_points += points

    def add_sprint_points(self, points):
        self.sprint_points += points
        
    def add_team(self, team):
        self.team = team

    def add_value(self, value):
        self.value = value