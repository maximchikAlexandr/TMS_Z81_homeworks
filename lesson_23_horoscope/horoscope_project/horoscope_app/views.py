from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from horoscope_app.services import HoroscopeSource

# Create your views here.
hor_src = HoroscopeSource()


class ZodiacView(TemplateView):
    """Для главной страницы"""
    template_name = "horoscope_app/index.html"

    def get(self, request: WSGIRequest) -> HttpResponse:
        return render(request, self.template_name,
                      {'zodiac_signs': hor_src.get_list_of_zodiac_signs()})


class HoroscopeView(TemplateView):
    """Для вывода гороскопа для определенного знака зодиака"""
    template_name = "horoscope_app/detail_horoscope.html"

    def get(self, request: WSGIRequest, zodiac_sign: str) -> HttpResponse:
        return render(request, self.template_name,
                      {'horoscope': hor_src.get_horoscope(zodiac_sign)})
