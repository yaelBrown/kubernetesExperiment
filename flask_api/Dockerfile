FROM python:latest

ADD app.py .

RUN pip install flask flask_cors requests

ENTRYPOINT [ "python" ]

CMD ["app.py"]