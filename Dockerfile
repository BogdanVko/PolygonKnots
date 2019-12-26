FROM continuumio/miniconda
ADD . /src

WORKDIR /src

RUN apt-get update -y && apt-get install -y gcc
RUN conda env create -f env_linux.yml
RUN apt-get install -y libglu1-mesa-dev freeglut3-dev mesa-common-dev