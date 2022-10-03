print("hola amor")


class Price(object):
    def __init__(self,code_Route: str, base_price: float, asientoEconomico: int, asientoPremium: int):
        """
        constructor de la clase price
        """
        
        self.code_Route: str = code_Route
        self.base_price: float = base_price
        self.asientoEconomico: int = asientoEconomico
        self.asientoPremium:int = asientoPremium