#  Created by Bogdan Vasilchenko on 02/Oct/2019

import numpy
import scipy.linalg
"""  Generating Quaternion Vectors.

        Step One -> Get 2 arrays of Complex Vectors [(Real,Imaginary),
                                                     (Real,Imaginary),
                                                           ...        ]
        Step Two -> Gram-Schmidt -> New Array of complex vectors. [ [ (..,..i), (..,..i) ],
                                                                         [ (), () ],
                                                                           ...           ]

        Step Three -> Transform the array of complex vectors into an array of Quaternion vectors.

        [R, fi, fj, fk] <--- Result

"""
def generate_random_vectors(size):
    """
    :param size: length of the complex vector arrays (ex.: size = 5 => there will be 5 random complex vectors)
    :return: returns a tuple of 2 arrays of complex vectors, each array has a provided length and 2 values for each vector: real and imaginary parts
    mean, standard deviation, and number of values per vector are hardcoded to be specific for this project
    """
    shape_to_generate=(size,2)
    mean =0
    stdDiv = 0.1
    array_of_complex_vectors = numpy.random.normal(mean, stdDiv, shape_to_generate)
    array_of_complex_vectors = array_of_complex_vectors[:,0]+array_of_complex_vectors[:,1]*1j
    return array_of_complex_vectors.reshape(-1,1)

 
def gram_schmidt(array_of_vectors1, array_of_vectors2):
    '''Perform Gram-schmidt to create an array of orthogonalized vectors
    To do that easily, inputs should be arrays of complex numbers.
    '''
    array_of_vectors=numpy.hstack((array_of_vectors1,array_of_vectors2))
    array_of_normal_vectors = scipy.linalg.orth(array_of_vectors)
    return array_of_normal_vectors



def create_quaternions(array_of_nv):
    array_of_quaternions = []
    return array_of_quaternions

def testNormalVectorsWithBounds(lowerBound,vector1,vector2,upperBound,message=""):
    value = numpy.vdot(vector1,vector2)
    assert lowerBound<=value<=upperBound, message

def test_normal_vectors(normal_vectors_of_complex):
    #Test if vectors are normal by taking their dot-product
    testNormalVectorsWithBounds((-1e-15-1e-15j),normal_vectors_of_complex[:,0],normal_vectors_of_complex[:,1],(1e-15+1e-15j), "u*v is too far from 0")
    testNormalVectorsWithBounds((1-1e-15-1e-15j),normal_vectors_of_complex[:,0],normal_vectors_of_complex[:,0],(1+1e-15+1e-15j), "u*u is too far from 1")
    testNormalVectorsWithBounds((1-1e-15-1e-15j),normal_vectors_of_complex[:,1],normal_vectors_of_complex[:,1],(1+1e-15+1e-15j), "v*v is too far from 1")

def two_complex_to_quaternion(array_of_two_complex):
    array_of_4_floats = numpy.hstack((
        array_of_two_complex[:,0].real.reshape(-1,1), array_of_two_complex[:,0].imag.reshape(-1,1),
        array_of_two_complex[:,1].real.reshape(-1,1), array_of_two_complex[:,1].imag.reshape(-1,1)
        ))
    return array_of_4_floats

def create_single_polygon_edge_from_quaternion(quaternion):
    '''
    Build a 3d edge vector from 4*[float] quaternion representation by using a formula discussed at one of the first meetings
    '''
    a,b,c,d = quaternion
    
    x = a**2+b**2-c**2-d**2
    y = 2*b*c - 2*a*d
    z = 2*a*c + 2*b*d
    
    return numpy.array([x,y,z])
    
def create_polygon_edges_from_quaternion_vector(quaternion_vector):
    '''
    Convert each quaternion in a quat vector to an edge and return a vector of polygon edges
    '''
    #use numpy buit-in function since it is likely to be well-optimized
    return numpy.apply_along_axis(create_single_polygon_edge_from_quaternion,1,quaternion_vector)
    
def testPolygonEnclosionWithBounds(polygon_edges,lowerBound,upperBound,message=""):
    '''Since polygon is supposed to be enclosed - sum of all of its vectors shall be equal to zero. 
    Unfornately, due to precision of computations, it is not always so. That's why discard polygons that are further from being enclosed.    
    '''
    close_to_zero = numpy.sum(polygon_edges, axis=0)
    assert lowerBound<=numpy.sum(close_to_zero, axis=0)<=upperBound, message

def create_polygon_edge_vector(size):   
    # Fill 2 arrays of complex vectors. @param number of vectors to make; @fill the array of vectors
    array_of_complex_vectors1 = generate_random_vectors(size)
    array_of_complex_vectors2 = generate_random_vectors(size)

    # Normal vectors of complex numbers
    normal_vectors = gram_schmidt(array_of_complex_vectors1,array_of_complex_vectors2)

    #Create quaternion from normal complex vectors
    quaternion = two_complex_to_quaternion(normal_vectors)

    #Finally, convert quaternion to edge vector
    polygon_edges = create_polygon_edges_from_quaternion_vector(quaternion)

    #Test if polygon has enclosed shape (or if it close enough). To have faster execution over precision - use wider bounds of acceptance
    testPolygonEnclosionWithBounds(polygon_edges,-1e-15,1e-15,"Polygon is too far from enclosed - try again and get lucky or use wider bounds")

    return polygon_edges

def polygon_edge_vector_to_vertices(polygon_edges):
    return numpy.cumsum(polygon_edges,axis=0)

def polygon_edges_and_vertices(size):
    edge_vector = create_polygon_edge_vector(size)
    vertex_vector = polygon_edge_vector_to_vertices(edge_vector)
    return edge_vector,vertex_vector
    
