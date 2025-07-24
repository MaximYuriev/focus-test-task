FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction

COPY . .

CMD uvicorn --factory src.main:create_app --host 0.0.0.0 --port 8000