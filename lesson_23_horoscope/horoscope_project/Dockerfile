FROM python:3.11.2
MAINTAINER Alex Maximchik 'alex@mail.ru'

SHELL ["/bin/bash", "-c"]

# set the environment variables
ENV PYTHONDONTWRITEBYTECODE 1 # no create cash
ENV PYTHONUNBUFFERED 1 # Force the stdout and stderr streams to be unbuffered

RUN pip install --upgrade pip
RUN useradd -rms /bin/bash horoscope && chmod 777 /opt /run

# mkdir + cd
WORKDIR /app

RUN chown -R horoscope:horoscope /app && chmod 755 /app

COPY --chown=horoscope . .

RUN pip install -r requirements.txt