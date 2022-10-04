class Airplane(object):
    def __init__(self, price_base: float, economic_seat: int, premium_seat: int, code_route: str, route: str, code_airplane: str):
        self.price_base: float = price_base
        self.economic_seat: int = economic_seat
        self.premium_seat: int = premium_seat
        self.code_route: str = code_route
        self.route: str = route
        self.code_airplane = code_airplane
        self.final_price_economic: float = self.price_base + self.economic_seat
        self.final_price_premium: float = self.price_base + self.premium_seat
        # self.airplane: Airplane = airplane

