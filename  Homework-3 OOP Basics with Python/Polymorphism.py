# 2. Polymorphism (Çok Biçimlilik) - Topla Oynanan Oyunlar

# Temel sınıf (Ana sınıf)
class BallGame:
    def __init__(self, name, players, field_type):
        self.name = name
        self.players = players
        self.field_type = field_type
    
    def game_info(self):
        return f"{self.name} is played with {self.players} players on a {self.field_type}."
    
    def play(self):
        return "The game is being played."

# Alt sınıflar (Türetilmiş sınıflar), farklı oyun kuralları ile
class Basketball(BallGame):
    def __init__(self):
        super().__init__("Basketball", 10, "court")
    
    def play(self):
        return "Players are dribbling and shooting the basketball into the hoop."

class Football(BallGame):
    def __init__(self):
        super().__init__("Football", 22, "field")
    
    def play(self):
        return "Players are passing and shooting the football into the goal."

class Volleyball(BallGame):
    def __init__(self):
        super().__init__("Volleyball", 12, "court")
    
    def play(self):
        return "Players are serving and spiking the volleyball over the net."

# Polymorphism örneği: Farklı oyunları aynı fonksiyonla yönetme

def start_game(game):
    print(game.game_info())
    print(game.play())
    print("-")

# Ana program (main)
def main():
    games = [Basketball(), Football(), Volleyball()]
    
    for game in games:
        start_game(game)

if __name__ == "__main__":
    main()

