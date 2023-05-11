FROM python:3.8-slim-buster

WORKDIR /client

COPY client/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-m" , "jurigged", "-v", "client.py"]