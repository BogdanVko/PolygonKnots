# Install
1) make sure anaconda\miniconda is installed. 
https://docs.conda.io/en/latest/miniconda.html

2) clone this repository

3) install dependencies
$ sudo apt-get update -y && sudo apt-get install -y gcc
$ sudo apt-get install -y libglu1-mesa-dev freeglut3-dev mesa-common-dev

3) install environment
$ conda env create -f environment.yml

# Run
1) activate conda environment
$ conda activate MathProjectKnots

2) run the file
$ python3 l-value_short_cost_distribution.py
