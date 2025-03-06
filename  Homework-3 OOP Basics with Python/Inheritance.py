# 1. Inheritance (Kalıtım) - Topla Oynanan Oyunlar

# Temel sınıf (Ana sınıf)
class BallGame:
    def __init__(self, name, players, field_type):
        self.name = name
        self.players = players
        self.field_type = field_type
    
    def game_info(self):
        return f"{self.name} is played with {self.players} players on a {self.field_type}."

# Alt sınıflar (Türetilmiş sınıflar)
class Basketball(BallGame):
    def __init__(self):
        super().__init__("Basketball", 10, "court")
    
    def game_info(self):
        return f"{self.name} is played with {self.players} players on a {self.field_type}, using a hoop and a basketball."

class Football(BallGame):
    def __init__(self):
        super().__init__("Football", 22, "field")
    
    def game_info(self):
        return f"{self.name} is played with {self.players} players on a {self.field_type}, using a goal and a football."

class Volleyball(BallGame):
    def __init__(self):
        super().__init__("Volleyball", 12, "court")
    
    def game_info(self):
        return f"{self.name} is played with {self.players} players on a {self.field_type}, using a net and a volleyball."

# Ana program (main)
def main():
    basketball = Basketball()
    football = Football()
    volleyball = Volleyball()
    
    print(basketball.game_info())
    print(football.game_info())
    print(volleyball.game_info())

if __name__ == "__main__":
    main()

