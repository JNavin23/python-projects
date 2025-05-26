class Car:
    def __init__(self, model_year: int, transmission: str, color: str):
        self.model_year = model_year
        self.transmission = transmission
        self.color = color

    def __repr__(self):
        return f"Car({self.model_year}, {self.transmission}, {self.color})"


class Audi(Car):
    _speed = "100 KMPH"

    def __init__(self, model_year: int, transmission: str, color: str):
        super().__init__(model_year, transmission, color)

    @property
    def speed(self):
        return self._speed

    def get_full_description(self):
        return (
            "=== Available Car Details ===\n"
            f"Make        : Audi\n"
            f"Model Year  : {self.model_year}\n"
            f"Transmission: {self.transmission}\n"
            f"Color       : {self.color}\n"
            f"Top Speed   : {self.speed}"
        )

    def __str__(self):
        return f"Audi {self.model_year} - {self.color} ({self.transmission})"


if __name__ == "__main__":
    car1 = Audi(2025, 'Automatic', 'Red')
    print(car1.get_full_description())
