FROM python:2.7

LABEL maintainer="Joseph Cáceres<josephccaceres@gmail.com>"

COPY . /app
WORKDIR /app

# Install flask
RUN pip install -U Flask
RUN pip install -U flask_restful


ENTRYPOINT ["python"]
CMD ["app.py"]