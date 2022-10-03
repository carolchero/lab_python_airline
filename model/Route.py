print("hola")

class Route(object):
    def __init__(self,code:str , name_route:str):
        """
        constructor de la clase route
        """
        
        self.code: str = code
        self.name: str = name_route