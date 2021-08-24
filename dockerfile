FROM python:3.8-slim-buster

WORKDIR /src
COPY requeriments.txt requeriments.txt
RUN pip3 install -r requeriments.txt
EXPOSE 50
COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "50"]