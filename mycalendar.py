import datetime as dt

class Calendar:
    def __init__(self) -> None:
        self.date = self.format_date()

    def get_date(self) -> list:
        now = dt.datetime.now()
        return [now.day, now.month] 
        

    def format_date(self):
        raw_dt = self.get_date()
        formated_dt = f"{raw_dt[0]} de "
        match raw_dt[1]:
            case 1:
                formated_dt += "Janeiro"
            case 2:
                formated_dt += "Feveiro"
            case 3:
                formated_dt += "Março"
            case 4:
                formated_dt += "Abril"
            case 5:
                formated_dt += "Maio"
            case 6:
                formated_dt += "Junho"
            case 7:
                formated_dt += "Julho"
            case 8:
                formated_dt += "Agosto"
            case 9:
                formated_dt += "Setembro"
            case 10:
                formated_dt += "Outubro"
            case 11:
                formated_dt += "Novembro"
            case 12:
                formated_dt += "Dezembro"
        return formated_dt
