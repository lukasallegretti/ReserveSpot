FROM python:3.9

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src

CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000"]