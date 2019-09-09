FROM python:2.7

LABEL maintainer="Joseph Cáceres<josephccaceres@gmail.com>"

COPY . /app
WORKDIR /app

# Install dependences
RUN pip install -U Flask
RUN pip install -U flask_restful
RUN pip install -U redis


ENTRYPOINT ["python"]
CMD ["app.py"]