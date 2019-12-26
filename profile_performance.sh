python3 -m cProfile -o identify.prof performance_profiling.py 

sudo docker cp <container_name>:/src/identify.prof .
