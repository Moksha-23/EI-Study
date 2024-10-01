class RouteStrategy:
    def calculate_route(self):
        pass


class FastestRoute(RouteStrategy):
    def calculate_route(self):
        return "Calculating fastest route..."


class ShortestRoute(RouteStrategy):
    def calculate_route(self):
        return "Calculating shortest route..."


class Navigator:
    def __init__(self, strategy: RouteStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: RouteStrategy):
        self.strategy = strategy

    def navigate(self):
        return self.strategy.calculate_route()

navigator = Navigator(FastestRoute())
print(navigator.navigate()) 

navigator.set_strategy(ShortestRoute())
print(navigator.navigate()) 
