import random


print("hola mi amorshito")


class Avion(object):
    def __init__(self, code_avion: str, asientoEconomico: int, asientoPremium: int):
        """
        constructor de la clase price
        """

        self.code_avion: str = code_avion
        self.asientoEconomico: float = asientoEconomico
        self.asientoPremium: float = asientoPremium


for i in range(4):

  correlative: str = str(i+1).zfill(3)
  print(correlative)

  ticket_number: str = f"{'A'}{correlative}"
  print(ticket_number)





