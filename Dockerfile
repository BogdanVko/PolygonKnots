FROM continuumio/miniconda3
ADD . /src

WORKDIR /src

RUN apt-get update -y && apt-get install -y gcc
RUN apt-get install -y libglu1-mesa-dev freeglut3-dev mesa-common-dev
RUN conda env create -f environment.yml && conda activate MathProjectKnots