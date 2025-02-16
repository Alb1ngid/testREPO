# Задание №3
import requests
from collections import defaultdict


# Задание №5

class TextAnalysis():

    # Задание №1

    def __init__(self, text, owner):

        # Задание №2

        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        self.response = self.get_answer()

    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
        # Задание №4
        except:
            return "Перевод не удался"


