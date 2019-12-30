import pickle

import snappy
from pyknotid.spacecurves import SpaceCurve

from polygon_generation import create_polygon_edge_vector,polygon_edge_vector_to_vertices
import math
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
    def get_ID(self):
        if self.knot_ID is None:
            #identify knot using the provided libraries
            with suppress_stdout():                
                k = SpaceCurve(self.vertices)
                PD = k.planar_diagram()
            snappyID =  snappy.Link(PD).exterior().identify()
            #snappy id has its own type, while we are only concerned with the string values
            self.knot_ID =[m.name() for m in snappyID]
        
        return self.knot_ID

    L=None
    def get_L(self):
        if self.L is None:
            self.L = self.compute_d_longest(self)
        return self.L
    def compute_d_longest(self,knot):
        max_distance = 0
        for vertex1_index in range(0,knot.vertices.shape[0]-1):
            for vertex2_index in range(vertex1_index,knot.vertices.shape[0]):
                x1,y1,z1 = knot.vertices[vertex1_index]
                x2,y2,z2 = knot.vertices[vertex2_index]
                distance = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
                if distance>max_distance:
                    max_distance = distance
        return max_distance

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

    def save(self, filename):
        pickle_out = open(filename,"wb")
        pickle.dump(self, pickle_out)
        pickle_out.close()
    
def load_knot(filename):
    pickle_in = open(filename,"rb")
    return pickle.load(pickle_in)