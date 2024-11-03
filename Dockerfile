FROM python:3.12-slim-bullseye

RUN apt update && apt install -y build-essential libffi-dev libssl-dev libpq-dev gettext

RUN pip install -U pip
RUN pip install poetry

RUN mkdir -p /app/src
WORKDIR /app/src

# Install Python dependencies
ADD poetry.lock pyproject.toml /app/src/
RUN poetry config virtualenvs.in-project true
RUN poetry install -vv --no-dev
ENV PATH="/app/src/.venv/bin:$PATH"

ADD . /app/src/

# Run translation compile messages
# DEBUG is required because env var such as SECRET_KEY are not set yet
RUN DEBUG=true python manage.py compilemessages
RUN DEBUG=true python manage.py collectstatic --noinput

CMD ["bash", "start.sh"]
