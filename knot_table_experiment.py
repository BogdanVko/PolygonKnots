import Knot as knot_lib
import sys

'''
Function to generate plenty of knots and identify them. 
'''
def generate_random_interesting_knot(size):
    ID=[]
    empty_knots_num =0    
    k=None
    while ID ==[]:        
        k = knot_lib.Knot(size)        
        empty_knots_num +=1       
        ID = k.get_ID()
        if empty_knots_num%10000 ==0:
            print("Empty: "+str(empty_knots_num))
    print("Took "+str(empty_knots_num)+" to generate this one: "+str(k.get_ID()))
    
    return k

'''
Open a table with a recorded number of sticks for each class. If this table does not exist, download it from that Github repository
'''    
def retrieve_table():
    filename = "stick_number_upper_bounds.csv"
    import os
    if not os.path.isfile('./'+filename):
        import wget
        url = "https://raw.githubusercontent.com/thomaseddy/stick-knot-gen/master/data/stick_number_upper_bounds.csv"
        filename = wget.download(url)

    import pandas as pd
    csv_data = pd.read_csv(filename, header=0)
    knot_table = dict(zip(list(csv_data["knot"]), list(csv_data[" stick_number_ub"])))
    return knot_table

def table_lookup(k,knot_table):
    for knot_type in k.get_ID():
        filename = knot_type+"-in-"+str(k.num_sticks)+".knot"
        if knot_type not in knot_table:
            print("New knot type: "+knot_type)
            k.save(filename)
            knot_table[knot_type] = k.num_sticks
        if knot_table[knot_type]> k.num_sticks:
            print("Found better knot: "+knot_type+" in "+str(k.num_sticks) +" sticks!")
            k.save(filename)
            knot_table[knot_type] = k.num_sticks

def main(num_sticks, num_knots=None):
    knot_table = retrieve_table()
    knot_counter = 0
    while num_knots is None or num_knots > knot_counter:
        k = generate_random_interesting_knot(num_sticks)
        table_lookup(k, knot_table)
        knot_counter += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise RuntimeError("Expecting argument with a number of sticks")
    if len(sys.argv) < 3:
        num_knots = None
    else:
        num_knots = int(sys.argv[2])
    main(int(sys.argv[1]), num_knots)
