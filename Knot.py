import pickle

import snappy
from pyknotid.spacecurves import SpaceCurve

from polygon_generation import create_polygon_edge_vector,polygon_edge_vector_to_vertices

'''
Provided function to identify knots generated lots of stdout, what is not very convenient since we need to generate lots of them. 
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

class Knot:
    edges = []
    vertices = []
    initial_random_vectors = []
    num_sticks = None
    knot_ID = None

    def __init__(self, num_sticks):        
        self.num_sticks = num_sticks
        #keep regerating polygon untill in looks fine by its edge computation accuracy
        bad_polygons =0
        succeffully_generated_polygon = False
        while not succeffully_generated_polygon:
            try:
                self.edges,self.initial_random_vectors = create_polygon_edge_vector(num_sticks)        
                self.vertices = polygon_edge_vector_to_vertices(self.edges)
                succeffully_generated_polygon = True
            except AssertionError:
                bad_polygons+=1
                if(bad_polygons>=10):
                    print("WARNING: "+str(bad_polygon)+" polygons in a row were bad. Consider changing margin of error")

        #identify knot using the provided libraries
        with suppress_stdout():                
            k = SpaceCurve(self.vertices)
            PD = k.planar_diagram()
        snappyID =  snappy.Link(PD).exterior().identify()
        #snappy id has its own type, while we are only concerned with the string values
        self.knot_ID =[m.name() for m in snappyID]

    def save(self, filename):
        pickle_out = open(filename,"wb")
        pickle.dump(self, pickle_out)
        pickle_out.close()
    
def load_knot(filename):
    pickle_in = open(filename,"rb")
    return pickle.load(pickle_in)