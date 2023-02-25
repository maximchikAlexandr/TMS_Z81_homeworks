from datetime import datetime
from typing import Dict

import requests
import xmltodict


class HoroscopeSource:
    __HOROSCOPE_SOURCE_URL = "https://ignio.com/r/export/utf/xml/daily/com.xml"

    def __init__(self) -> None:
        self.__get_horoscope_from_internet()

    def get_horoscope(self, zodiac_name: str) -> Dict[str, str]:
        """Проверяем актуальность гороскопов и возвращаем гороскоп
        по знаку зодиака"""
        if not self.__is_actual_horoscope():
            self.__get_horoscope_from_internet()
        return self.__create_horoscope_dict(zodiac_name)

    def __is_actual_horoscope(self) -> bool:
        today = self.__horoscopes["horo"]["date"]["@today"]
        today = datetime.strptime(today, "%d.%m.%Y").date()
        return today == datetime.now().date()

    def __get_horoscope_from_internet(self) -> None:
        xml_str = requests.get(self.__HOROSCOPE_SOURCE_URL, timeout=5).text
        self.__horoscopes = xmltodict.parse(xml_str)

    def __create_horoscope_dict(self, zodiac_name: str) -> Dict[str, str]:
        horoscope = {}
        for day, hrscp in self.__horoscopes["horo"][zodiac_name].items():
            horoscope[self.__horoscopes["horo"]["date"][f"@{day}"]] = hrscp
        return horoscope
