class WeatherData:
    def __init__(self):
        self.observers = []
        self.temperature = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()


class Display:
    def update(self, temperature):
        print(f"Temperature updated to: {temperature}°C")
weather_data = WeatherData()
display1 = Display()
display2 = Display()

weather_data.register_observer(display1)
weather_data.register_observer(display2)

weather_data.set_temperature(25)  
