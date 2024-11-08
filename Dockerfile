FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5556

CMD ["gunicorn", "-b", "0.0.0.0:5556", "-w", "3", "--log-file", "-", "--log-level", "debug", "--access-logfile", "-", "app:app"]