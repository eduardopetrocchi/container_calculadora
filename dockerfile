FROM ubuntu

RUN apt update && apt install -y python3 && apt clean

COPY calculadora.py /opt/calculadora.py

CMD python3 /opt/calculadora.py


