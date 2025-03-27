FROM python:3.9-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5002 5005

COPY . .
ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=development
CMD ["flask", "run", "--host", "0.0.0.0"]