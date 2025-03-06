# 4. Abstraction (Soyutlama) - Topla Oynanan Oyunlar

from abc import ABC, abstractmethod

# Soyut (Abstract) sınıf
class BallGame(ABC):
    def __init__(self, name, players, field_type):
        self.name = name
        self.players = players
        self.field_type = field_type
    
    def game_info(self):
        return f"{self.name} is played with {self.players} players on a {self.field_type}."
    
    @abstractmethod
    def play(self):
        pass  # Alt sınıflar tarafından uygulanmalıdır

# Somut sınıflar (Soyut sınıftan türetilmiş)
class Basketball(BallGame):
    def __init__(self):
        super().__init__("Basketball", 10, "court")
    
    def play(self):
        return "Dribbling and shooting the basketball into the hoop."

class Football(BallGame):
    def __init__(self):
        super().__init__("Football", 22, "field")
    
    def play(self):
        return "Passing and shooting the football into the goal."

class Volleyball(BallGame):
    def __init__(self):
        super().__init__("Volleyball", 12, "court")
    
    def play(self):
        return "Serving and spiking the volleyball over the net."

# Ana program (main)
def main():
    games = [Basketball(), Football(), Volleyball()]
    
    for game in games:
        print(game.game_info())
        print(game.play())
        print("-")

if __name__ == "__main__":
    main()

