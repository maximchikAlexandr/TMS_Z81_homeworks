from django.urls import path
from horoscope_app.views import ZodiacView, HoroscopeView

urlpatterns = [
    path("", ZodiacView.as_view(), name="zodiac_signs"),
    path("<str:zodiac_sign>", HoroscopeView.as_view(), name="horoscope"),
]
