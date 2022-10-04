from math import prod
from typing import List, Dict
from model.Airplane import Airplane
from model.TicketSales import TicketSales
from itertools import groupby
from config import CURRENCY_SYMBOL
import utils


def create_list_airplane_sales() -> List[Airplane]: # data de Ventas de aviones
    """
    Funcion que crea y devuelve una lista de objetos Ticket
    """
    data_sales: List[Dict[str, str | int]] = [
        {
            "min_sales_economic": 120,
            "min_sales_premium": 10,
            "max_sales_economic": 130,
            "max_sales_premium": 20,
            "code_route": "LIM-AYA",

        },
        {
            "min_sales_economic": 130,
            "min_sales_premium": 15,
            "max_sales_economic": 144,
            "max_sales_premium": 24,
            "code_route": "LIM-CUS",
        },
        {
            "min_sales_economic": 115,
            "min_sales_premium": 16,
            "max_sales_economic": 138,
            "max_sales_premium": 22,
            "code_route": "LIM-ARE",
        },
        {
            "min_sales_economic": 100,
            "min_sales_premium": 12,
            "max_sales_economic": 120,
            "max_sales_premium": 18,
            "code_route": "LIM-TAR",
        },
        {
            "min_sales_economic": 100,
            "min_sales_premium": 10,
            "max_sales_economic": 115,
            "max_sales_premium": 15,
            "code_route": "AYA-LIM",
        },
        {

            "min_sales_economic": 105,
            "min_sales_premium": 14,
            "max_sales_economic": 120,
            "max_sales_premium": 20,
            "code_route": "CUS-LIM",
        },
        {
            "min_sales_economic": 100,
            "min_sales_premium": 13,
            "max_sales_economic": 110,
            "max_sales_premium": 18,
            "code_route": "ARE-LIM",
        },
        {
            "min_sales_economic": 90,
            "min_sales_premium": 10,
            "max_sales_economic": 105,
            "max_sales_premium": 15,
            "code_route": "TAR-LIM",

        },
    ]
    data_airplane: List[Dict[str, int | float | str]] = [ #data de aviones 
        {
            "price_base": 55.19,
            "economic_seat": 8,
            "premium_seat": 16,
            "code_route": "LIM-AYA",
            "route": "Lima - Ayacucho",
            "code_airplane": "A001"
        },
        {
            "price_base": 136.51,
            "economic_seat": 8,
            "premium_seat": 16,
            "code_route": "LIM-CUS",
            "route": "Lima - Cusco",
            "code_airplane": "A002"

        },
        {
            "price_base": 90.59,
            "economic_seat": 8,
            "premium_seat": 16,
            "code_route": "LIM-ARE",
            "route": "Lima - Arequipa",
            "code_airplane": "A003"
        },
        {
            "price_base": 71.89,
            "economic_seat": 8,
            "premium_seat": 16,
            "code_route": "LIM-TAR",
            "route": "Lima - Tarapoto",
            "code_airplane": "A004"
        },
        {
            "price_base": 40.42,
            "economic_seat": 7,
            "premium_seat": 16,
            "code_route": "AYA-LIM",
            "route": "Ayacucho - Lima",
            "code_airplane": "A001"
        },
        {
            "price_base": 124.32,
            "economic_seat": 7,
            "premium_seat": 16,
            "code_route": "CUS-LIM",
            "route": "Cusco - Lima",
            "code_airplane": "A002"
        },
        {
            "price_base": 86.59,
            "economic_seat": 7,
            "premium_seat": 16,
            "code_route": "ARE-LIM",
            "route": "Arequipa - Lima",
            "code_airplane": "A003"
        },
        {
            "price_base": 68.42,
            "economic_seat": 7,
            "premium_seat": 16,
            "code_route": "TAR-LIM",
            "route": "Tarapoto - Lima",
            "code_airplane": "A004"
        },
    ]
    airplanes: List[Airplane] = []
    tickets_sales: List[TicketSales] = []
    for key, airplane in enumerate(data_airplane):
        obj_airplane = Airplane(
            float(airplane['price_base']),
            int(airplane['economic_seat']),
            int(airplane['premium_seat']),
            str(airplane['code_route']),
            str(airplane['route']),
            str(airplane['code_airplane'])
        )
        airplanes.append(obj_airplane)
        obj_ticket = TicketSales(
            int(data_sales[key]['min_sales_economic']),
            int(data_sales[key]['max_sales_economic']),
            int(data_sales[key]['min_sales_premium']),
            int(data_sales[key]['max_sales_premium']),
            str(data_sales[key]['code_route']),
            obj_airplane
        )
        tickets_sales.append(obj_ticket)
    return tickets_sales


def get_airplane_transport_max(sorted_tickets: List[TicketSales]): # funcion para obtener aviones maximos
    max_flight = {"venta": 0, "code_airplane": " "}
    for code_airplane, elementos in groupby(sorted_tickets, key=lambda x: x.airplane.code_airplane):
        airplane = {"venta": 0,
                    "code_airplane": code_airplane}
        for elemento in elementos:
            airplane["venta"] += elemento.total_sales_travel_ticket
        if airplane["venta"] > max_flight["venta"]:
            max_flight = airplane
    return max_flight


def main():
    """
    Función principal del módulo app.py
    """

    #  Creamos la la lista de ventas por avion
    sales_airplane: List[TicketSales] = create_list_airplane_sales()

    sorted_tickets: List[TicketSales] = sorted(
        sales_airplane, key=lambda x: x.total_sales_travel_ticket)
    sorted_tickets_amount: List[TicketSales] = sorted(
        sales_airplane, key=lambda x: x.total_sales_amount)
    #  Calcular la suma total  de pasajes vendidos
    rep_total_sale: int = sum(
        [ticket.total_sales_travel_ticket for k, ticket in enumerate(sales_airplane)])
    # Calcular el ingreso total de pasajes economicos vendidos
    rep_total_sale_seat_economic: int = sum(
        [ticket.sales_economic for k, ticket in enumerate(sales_airplane)])
    # Calcular el ingreso total de pasajes premium vendidos
    rep_total_sale_seat_premium: int = sum(
        [ticket.sales_premium for k, ticket in enumerate(sales_airplane)])
    # Calcular la suma total de pasajes economicos vendidos
    rep_total_sale_economic: int = round(sum(
        [ticket.total_sales_income_economic for k, ticket in enumerate(sales_airplane)]), 2)
    # Calcular la suma total de pasajes premium vendidos
    rep_total_sale_premium: int = round(sum(
        [ticket.total_sales_income_premium for k, ticket in enumerate(sales_airplane)]), 2)
    # Calculando la suma total de IGV cobrado
    rep_total_igv: float = round(
        sum([ticket.total_amount_igv for k, ticket in enumerate(sales_airplane)]), 2)
    # Calcular el promedio del costo de pasaje economico
    amount_price_avg_economic: float = round(
        rep_total_sale_economic/rep_total_sale_seat_economic, 2)
    # Calcular el promedio del costo de pasaje economico
    amount_price_avg_premium: float = round(
        rep_total_sale_premium/rep_total_sale_seat_premium, 2)
    # ordenar vuelos por codigo de avion
    sorted_airplane: List[TicketSales] = sorted(
        sales_airplane, key=lambda x: x.airplane.code_airplane)
    # Calcular el avion que transporto mas pasajeros
    airplane_max_passengers = get_airplane_transport_max(sorted_airplane)
    print("\n")
    print("*"*100)
    print("INFORME GENERAL")
    print("*"*100)
    # ¿Cuál es el total de pasajes vendidos entre todos los vuelos?
    print("cantidad total vendida de pasajeros: ", rep_total_sale)
    # ¿Cuál es el total de ingresos por la venta de pasajes económicos?
    print("ingreso de ventas de pasajes economicos: ",
          utils.get_currency_format(CURRENCY_SYMBOL, rep_total_sale_economic))
    # ¿Cuál es el total de ingresos por la venta de pasajes premium?
    print("ingreso de ventas de pasajes premium: ",
          utils.get_currency_format(CURRENCY_SYMBOL, rep_total_sale_premium))
    # ¿Cuál es el importe total de IGV cobrado?
    print("total importe igv cobrado: ", utils.get_currency_format(
        CURRENCY_SYMBOL, rep_total_igv))
    # ¿Cuál es el valor promedio de un pasaje económico?
    print("valor promedio pasaje economico: ", utils.get_currency_format(
        CURRENCY_SYMBOL, amount_price_avg_economic))
    # ¿Cuál es el valor promedio de un pasaje premium?
    print("valor promedio pasaje premium: ", utils.get_currency_format(
        CURRENCY_SYMBOL, amount_price_avg_premium))
    # ¿Cuál fue el vuelo con la mayor cantidad de pasajeros?
    print("Vuelo con la mayor cantidad de pasajeros: ",
          sorted_tickets[-1].code_route)
    # ¿Cuál fue el vuelo con la menor cantidad de pasajeros?
    print("Vuelo con la menor cantidad de pasajeros: ",
          sorted_tickets[0].code_route)
    # ¿Cuáles son los tres primeros vuelos que obtuvieron los mayores ingresos por la venta de asientos?
    print("Primeros tres vuelos que obtuvieron mayor ingreso: ", {
          sorted_tickets_amount[-1].code_route,
          sorted_tickets_amount[-2].code_route,
          sorted_tickets_amount[-3].code_route})
    # ¿Cuál fue el avión que transportó la mayor cantidad de pasajeros?
    print("Avion que transporto la mayor cantidad de pasajeros: ",
          airplane_max_passengers["code_airplane"])
    print("*"*100)


if __name__ == "__main__":
    main()