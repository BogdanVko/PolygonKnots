from pyknotid.spacecurves import SpaceCurve

'''
Provided function generated lots of stdout, what is not very convenient since we need to generate lots of them. 
Use this function to suppress this irrelevant output.

'''
from contextlib import contextmanager
import sys, os
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout


'''
Function to generate plenty of knots and identify them. 
'''
import snappy
from pyknotid.spacecurves import SpaceCurve
import polygon_generation as polygon
def generate_and_identify_knot(size):
    ID=[]
    empty_knot_id =0
    bad_polygon =0
    while ID ==[]:
        try:
            with suppress_stdout():
                polygon_data = polygon.polygon_edges_and_vertices(size)
                k = SpaceCurve(polygon_data[1])
                PD = k.planar_diagram()
            ID = snappy.Link(PD).exterior().identify()
            empty_knot_id +=1
        except AssertionError:
            bad_polygon+=1
    return ID