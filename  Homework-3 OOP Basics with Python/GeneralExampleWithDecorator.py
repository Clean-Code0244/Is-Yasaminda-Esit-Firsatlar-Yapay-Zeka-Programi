# Python OOP - Tüm Konseptlerin Kullanıldığı Genel Örnek (Decorator Kullanımı Dahil)

from abc import ABC, abstractmethod
from functools import wraps

# 6. Decorators (Dekoratörler) - Bir metodu süslemek ve işlevselliğini genişletmek için

def log_method(func):
    """Metodun çağrıldığını ve sonucunu loglayan dekoratör."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} called. Result: {result}")
        return result
    return wrapper

# 1. Abstraction (Soyutlama) - Soyut bir sınıf oluşturuyorum
class BallGame(ABC):
    def __init__(self, name, players, field_type):
        self.name = name  # Public attribute
        self._players = players  # Protected attribute
        self.__field_type = field_type  # Private attribute
    
    @log_method  # Dekoratör ile metodun çağrıldığı loglanıyor
    def game_info(self):
        return f"{self.name} is played with {self._players} players on a {self.__field_type}."
    
    @abstractmethod
    def play(self):
        pass  # Alt sınıflar tarafından uygulanmalıdır
    
    # 3. Encapsulation (Kapsülleme) - Private attribute'a güvenli erişim
    def get_field_type(self):
        return self.__field_type
    
    def set_field_type(self, field_type):
        if field_type in ["court", "field", "beach"]:
            self.__field_type = field_type
        else:
            print("Invalid field type!")

# 2. Inheritance (Kalıtım) - BallGame sınıfından türeyen alt sınıflar
class Basketball(BallGame):
    def __init__(self):
        super().__init__("Basketball", 10, "court")
    
    # 4. Method Overriding (Metot Ezme) - play() metodunu yeniden tanımlıyorum
    @log_method  # Dekoratör ile play() metodunun çağrıldığı loglanıyor
    def play(self):
        return "Players are dribbling and shooting the basketball into the hoop."

class Football(BallGame):
    def __init__(self):
        super().__init__("Football", 22, "field")
    
    @log_method
    def play(self):
        return "Players are passing and shooting the football into the goal."

class Volleyball(BallGame):
    def __init__(self):
        super().__init__("Volleyball", 12, "court")
    
    @log_method
    def play(self):
        return "Players are serving and spiking the volleyball over the net."

# 5. Polymorphism (Çok Biçimlilik) - Aynı metodu farklı sınıflar için çağırma

def start_game(game):
    print(game.game_info())
    print(game.play())
    print("-")


def main():
    games = [Basketball(), Football(), Volleyball()]
    
    for game in games:
        start_game(game)  # Polymorphism kullanımı
    
    # Encapsulation
    basketball = Basketball()
    print("Basketball is played on:", basketball.get_field_type())
    basketball.set_field_type("beach")
    print("Updated field type:", basketball.get_field_type())
    basketball.set_field_type("water")  # Geçersiz veri testi

if __name__ == "__main__":
    main()

