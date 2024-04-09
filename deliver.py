import smtplib
import unicodedata
import re

class Deliver:
    def __init__(self, login, password, to_email) -> None:
        self.login = login
        self.password = password
        self.to_email = to_email


    def create_message(self, info):
        date = f"{info[0].text}".replace("\n", " - ")
        mass = f"Mass:\n{info[1].text}\n\n"
        cal_mariano = f"Calendário Mariano:\n{info[2].text}\n"
        liturgy = f"Liturgia:\n{info[3].text}"
        message = f"subject:{date}\n\n{mass}{cal_mariano}{liturgy}"
        return self.format_msg(message)


    def format_msg(self, message):
        normalized_string = unicodedata.normalize('NFD', message)
        diacritic_free_string = re.sub(r'[\u0300-\u036fªº•*\u2013]', '', normalized_string)
        return diacritic_free_string


    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.login, password=self.password)
            connection.sendmail(from_addr=self.login, to_addrs=self.to_email, msg=message)
