from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Btn:
    journal = '\U0001F3EA' + ' Журнал'
    reports = '\U0001F3F7' + ' Отчеты'
    pay_card = '\U0001F4B3' + ' Оплатить'