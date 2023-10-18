FROM python:3.12-bookworm

# ENV PYTHONUNBUFFERED 1
# ENV PATH="$PATH:/etc/profile"

RUN apt-get update -y
RUN apt-get -y install binutils libproj-dev gdal-bin
RUN apt -y install libjpeg-dev
RUN apt -y install zlib1g-dev
RUN apt -y install vim curl

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
