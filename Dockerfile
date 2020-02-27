FROM continuumio/miniconda3
ADD . /src

WORKDIR /src

RUN apt-get update -y && apt-get install -y gcc
RUN apt-get install -y libglu1-mesa-dev freeglut3-dev mesa-common-dev
RUN conda env create -f environment.yml

# Pull the environment name out of the environment.yml
RUN echo $(head -1 /tmp/environment.yml
RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

CMD python3 l-value_short_cost_distribution.py