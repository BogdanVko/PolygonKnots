'''
Function to generate plenty of knots and identify them. 
'''
def generate_and_identify_knot(size):
    ID=[]
    empty_knot_id =0    
    while ID ==[]:        
        k = knot_lib.Knot(size)        
        empty_knot_id +=1        
    print("Took "+str(empty_knot_id)+" to generate this one")
    
    return ID