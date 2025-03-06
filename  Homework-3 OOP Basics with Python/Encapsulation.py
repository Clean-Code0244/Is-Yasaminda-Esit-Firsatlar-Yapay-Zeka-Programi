# 3. Encapsulation (Kapsülleme) - Topla Oynanan Oyunlar

class BallGame:
    def __init__(self, name, players, field_type):
        self.name = name  # Public attribute
        self._players = players  # Protected attribute
        self.__field_type = field_type  # Private attribute
    
    # Public method
    def game_info(self):
        return f"{self.name} is played with {self._players} players on a {self.__field_type}."
    
    # Getter method for private attribute
    def get_field_type(self):
        return self.__field_type
    
    # Setter method for private attribute
    def set_field_type(self, field_type):
        if field_type in ["court", "field", "beach"]:
            self.__field_type = field_type
        else:
            print("Invalid field type!")

class Basketball(BallGame):
    def __init__(self):
        super().__init__("Basketball", 10, "court")

class Football(BallGame):
    def __init__(self):
        super().__init__("Football", 22, "field")

class Volleyball(BallGame):
    def __init__(self):
        super().__init__("Volleyball", 12, "court")

# Ana program (main)
def main():
    basketball = Basketball()
    football = Football()
    volleyball = Volleyball()
    
    print(basketball.game_info())
    print(football.game_info())
    print(volleyball.game_info())
    
    # Kapsülleme örneği: Private attribute erişimi
    print("Basketball is played on:", basketball.get_field_type())
    basketball.set_field_type("beach")
    print("Updated field type:", basketball.get_field_type())
    
    # Geçersiz alan güncellemesi
    basketball.set_field_type("water")
    print("Final field type:", basketball.get_field_type())

if __name__ == "__main__":
    main()

