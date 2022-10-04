import random
import os

import sys

from model.Airplane import Airplane
#from Airplane import Airplane

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..' )
sys.path.append( mymodule_dir )


from config import IGV_PERCENT


class TicketSales(object):

    def __init__(self, min_sales_economic: int, max_sales_economic: int, min_sales_premium: int, max_sales_premium: int, code_route: str, airplane: Airplane):

        self.min_sales_economic: int = min_sales_economic
        self.max_sales_economic: int = max_sales_economic
        self.min_sales_premium: int = min_sales_premium
        self.max_sales_premium: int = max_sales_premium
        self.code_route = code_route
        self.airplane = airplane
        self.get_rand_sales_total()

    def __repr__(self) -> str:
        """
        Método especial para representar el objeto de una clase como string.
        """
        return self.code_route

    def get_rand_sales_economic(self) -> int:
        """
        Devuelve un número de ventas de manera aleatoria basada en el rango
        de ventas mínimas y máximas de la tienda.
        """
        return random.randint(self.min_sales_economic, self.max_sales_economic)

    def get_rand_sales_premium(self) -> int:
        """
        Devuelve un número de ventas de manera aleatoria basada en el rango
        de ventas mínimas y máximas de la tienda.
        """
        return random.randint(self.min_sales_premium, self.max_sales_premium)

    def get_rand_sales_total(self) -> None:
        self.sales_economic = self.get_rand_sales_economic()
        self.sales_premium = self.get_rand_sales_premium()
        self.total_sales_travel_ticket = self.sales_economic + self.sales_premium
        self.total_sales_income_economic = self.sales_economic * \
            self.airplane.final_price_economic
        self.total_sales_income_premium = self.sales_premium * \
            self.airplane.final_price_premium
        self.total_sales_amount = self.total_sales_income_economic + \
            self.total_sales_income_premium
        self.total_amount_igv = (
            self.total_sales_income_economic + self.total_sales_income_premium) * IGV_PERCENT/100