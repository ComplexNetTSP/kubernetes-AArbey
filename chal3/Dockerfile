# syntax=docker/dockerfile:1

FROM python:3.9.13-alpine
WORKDIR /app
COPY . .
RUN pip install flask pymongo
ENV FLASK_APP=chal1.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
EXPOSE 5000