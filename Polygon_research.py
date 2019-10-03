#  Created by Bogdan Vasilchenko on 02/Oct/2019


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


# Fill 2 arrays of complex vectors. @param number of vectors to make; @fill the array of vectors
for i in range(initial_amount_of_complex_vectors):
    # Tuple represents a vector (#, #i)
    vector = (random_number(), random_number())

    array_of_complex_vectors1.append(vector)

for i in range(initial_amount_of_complex_vectors):
    # Tuple represents a vector (#, #i)
    vector = (random_number(), random_number())
    array_of_complex_vectors2.append(vector)


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
