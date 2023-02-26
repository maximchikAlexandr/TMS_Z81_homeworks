from django.urls import path
from horoscope_app.views import ZodiacsSignsView, HoroscopeView

urlpatterns = [
    path("", ZodiacsSignsView.as_view(), name="zodiac_signs"),
    path("<str:zodiac_sign>", HoroscopeView.as_view(), name="horoscope"),
]
