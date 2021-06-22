FROM python:3.9.0-slim

RUN pip install requirements.txt

EXPOSE 80

COPY ./api /api

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]