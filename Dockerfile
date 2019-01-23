FROM python:3.4

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY cmd.sh /

CMD ["/cmd.sh"]
