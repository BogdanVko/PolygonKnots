import numpy
import math 

from Knot import Knot
from polygon_generation import two_complex_to_quaternion

def compute_L(knot):
    quat_arr = two_complex_to_quaternion(numpy.hstack(knot.initial_random_vectors))
    n = quat_arr.shape[0]
    
    
    acc_j=0
    for j in range(0,n):
        acc_i=0
        for i in range(0,n):            
            #(a^2+b^2+c^2+d^2)^2
            acc_k_0 = 0
            for k in range(i,j+1):
                acc_k_0 += quat_arr[k,0]**2+quat_arr[k,1]**2+quat_arr[k,2]**2+quat_arr[k,3]**2
            acc_k_0 = acc_k_0**2
            
            #(2(b*c-a*d))^2
            acc_k_1 = 0
            for k in range(i,j+1):
                acc_k_1 += quat_arr[k,1]*quat_arr[k,2]-quat_arr[k,0]*quat_arr[k,3]
            acc_k_1 = (2*acc_k_1)**2
            
            #(2(a*c+b*d))^2
            acc_k_2 = 0
            for k in range(i,j+1):
                acc_k_2 += quat_arr[k,0]*quat_arr[k,2]+quat_arr[k,1]*quat_arr[k,3]
            acc_k_2 = (2*acc_k_2)**2
            
            left_k = math.sqrt(acc_k_0+acc_k_1+acc_k_2)
            
            #right side of minus
            right_k = compute_right_k(quat_arr,n)
            
            acc_i+=left_k-right_k
        acc_j+=acc_i
        
    d_longest = compute_d_longest(knot)#numpy.max(quat_arr[:,3])
    return math.sqrt(acc_j**2)/d_longest

def compute_right_k(quat_arr,n):
    acc_m=0
    for m in range(0,n):
        acc_p=0
        for p in range(0,n):            
            #(a^2+b^2+c^2+d^2)^2
            acc_k_0 = 0
            for k in range(m,p+1):
                acc_k_0 += quat_arr[k,0]**2+quat_arr[k,1]**2+quat_arr[k,2]**2+quat_arr[k,3]**2
            acc_k_0 = acc_k_0**2
            
            #(2(b*c-a*d))^2
            acc_k_1 = 0
            for k in range(m,p+1):
                acc_k_1 += quat_arr[k,1]*quat_arr[k,2]-quat_arr[k,0]*quat_arr[k,3]
            acc_k_1 = (2*acc_k_1)**2
            
            #(2(a*c+b*d))^2
            acc_k_2 = 0
            for k in range(m,p+1):
                acc_k_2 += quat_arr[k,0]*quat_arr[k,2]+quat_arr[k,1]*quat_arr[k,3]
            acc_k_2 = (2*acc_k_2)**2
            
        acc_p+=math.sqrt(acc_k_0+acc_k_1+acc_k_2)
    acc_m+=acc_p
    return acc_m/(n*(n-1))

def compute_d_longest(knot):
    max_distance = 0
    for row_index in range(-1,knot.vertices.shape[0]-1):
        x1,y1,z1 = knot.vertices[row_index]
        x2,y2,z2 = knot.vertices[row_index+1]
        distance = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
        if distance>max_distance:
            max_distance = distance
    return max_distance

if __name__=="__main__":
    number_of_knots = 100
    stick_number = 10

    empty = open("empty.lval", "w")
    num_empty=0
    non_empty = open("non_empty.lval", "w")    

    for _ in range(0,number_of_knots):
        k=Knot(stick_number)    
        L=compute_L(k)
        if k.knot_ID == []:
            empty.write(L)       
            num_empty+=1     
        else:
            non_empty.write(L)
    print("Generated "+str(number_of_knots)+" knots: "+str(num_empty)+" of them were empty")

    empty.close()
    non_empty.close()