#  Created by Bogdan Vasilchenko on 02/Oct/2019

import numpy
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

initial_amount_of_complex_vectors = 100  # STUB
array_of_complex_vectors1 = []
array_of_complex_vectors2 = []
normal_vectors = []


# Get a random float from a Gaussian Distribution. @return float
def random_number():
    number = 1  # STUB for now. Should be a random number from Gaussian Distribution
    return number

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
    return array_of_complex_vectors

# Fill 2 arrays of complex vectors. @param number of vectors to make; @fill the array of vectors
array_of_complex_vectors1 = generate_random_vectors(initial_amount_of_complex_vectors)
array_of_complex_vectors2 = generate_random_vectors(initial_amount_of_complex_vectors)

# Perform Gram-schmidt to create an array of
def gram_schmidt(array_of_vectors1, array_of_vectors2):
    array_of_normal_vectors = []  # Puts in 2 tuples per []. 2 tuples/vectors are normal to each other
    return array_of_normal_vectors


# Normal vectors
normal_vectors = gram_schmidt(array_of_complex_vectors1, array_of_complex_vectors2)


def create_quaternions(array_of_nv):
    array_of_quaternions = []
    return array_of_quaternions


def main():
    quaternions = create_quaternions(normal_vectors)

    # Add testing for normal vectors
    print(quaternions)


if __name__ == "__main__":
    main()
