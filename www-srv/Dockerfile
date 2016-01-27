FROM python:2.7

RUN apt-get update && apt-get install -y libicu-dev 
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY src /usr/src/app

CMD [ "python", "run_explora.py" ]

