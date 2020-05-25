FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /codecoins
WORKDIR /codecoins
COPY requirements.txt /codecoins/
RUN pip install -r requirements.txt
COPY . /codecoins/
