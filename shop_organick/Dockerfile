# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.10.1-slim-buster

# Add user that will be used in the container.
RUN useradd wagtail

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

# Install the application server.
RUN pip install "gunicorn==20.0.4"
RUN pip install "wagtail==2.15.1"
RUN pip install "psycopg2>=2.8"


# Use /app folder as a directory where the source code is stored.
WORKDIR /code

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
# CMD set -xe; sleep 10; python manage.py migrate --noinput; gunicorn shop_organick.wsgi:application
CMD set -xe; sleep 10; python manage.py migrate --noinput; python manage.py runserver 0.0.0.0:8000
