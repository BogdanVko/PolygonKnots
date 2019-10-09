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


# Perform Gram-schmidt to create an array of orthogonalized vectors
def gram_schmidt(array_of_vectors1, array_of_vectors2):
    array_of_vectors=numpy.hstack((array_of_vectors1,array_of_vectors2))
    array_of_normal_vectors = scipy.linalg.orth(array_of_vectors)
    return array_of_normal_vectors



def create_quaternions(array_of_nv):
    array_of_quaternions = []
    return array_of_quaternions

def testNormalVectorsWithBounds(lowerBound,vector1,vector2,upperBound,message=""):
    value = numpy.vdot(vector1,vector2)
    assert lowerBound<=value<=upperBound, message

def main(size):   
    # Fill 2 arrays of complex vectors. @param number of vectors to make; @fill the array of vectors
    array_of_complex_vectors1 = generate_random_vectors(size)
    array_of_complex_vectors2 = generate_random_vectors(size)

    # Normal vectors
    normal_vectors = gram_schmidt(array_of_complex_vectors1,array_of_complex_vectors2)

    #Test if vectors are normal by taking their dot-product
    testNormalVectorsWithBounds((-1e-15-1e-15j),normal_vectors[:,0],normal_vectors[:,1],(1e-15+1e-15j), "u*v is too far from 0")
    testNormalVectorsWithBounds((1-1e-15-1e-15j),normal_vectors[:,0],normal_vectors[:,0],(1+1e-15+1e-15j), "u*u is too far from 1")
    testNormalVectorsWithBounds((1-1e-15-1e-15j),normal_vectors[:,1],normal_vectors[:,1],(1+1e-15+1e-15j), "v*v is too far from 1")
    
    
    return normal_vectors

if __name__ == "__main__":
    main(5)
    
