from Knot import Knot
import random

id_cost = 0.8
gen_cost = 0.17
lval_cost = 0.03

def main(number_of_non_empty_knots ,stick_number):

    while True:
        cost_file = open("avg_costs.csv", "a")
        num_empty=0

        lval_threshold = random.uniform(0.3,0.9)
        print("Selected threshold: "+str(lval_threshold))
        outcome1,outcome2,outcome3,outcome4 = 0,0,0,0

        cost_sum = 0

        while outcome1 < number_of_non_empty_knots:
            cost = 0
            k=Knot(stick_number)        
            cost += gen_cost
            
            L=k.get_L()
            cost += lval_cost
            
            discarded = True
            if L<=lval_threshold:
                cost+=id_cost
                discarded = False
                
            if k.get_ID() != []:
                if discarded:
                    #discarded non-empty one
                    outcome4+=1
                    if outcome4>number_of_non_empty_knots*100:
                        continue
                else:            
                    #found non-empty one
                    outcome1+=1
                    print("Found non-empty ones: "+str(outcome1)+ " out of "+str(number_of_non_empty_knots))
            else:
                num_empty+=1
                if discarded:
                    #discarded empty one
                    outcome3+=1
                else:
                    #identified empty one
                    outcome2+=1
            cost_sum += cost
            
        average_cost = cost_sum / (number_of_non_empty_knots+num_empty)
        cost_file.write(str(lval_threshold)+','+str(average_cost)+','+str(number_of_non_empty_knots)+','+str(num_empty)+','
                        +str(outcome1)+','+str(outcome2)+','+str(outcome3)+','+str(outcome4)+'\n')
        cost_file.flush()
        cost_file.close()

if __name__=="__main__":

    number_of_non_empty_knots = 1
    stick_number = 10
    main(number_of_non_empty_knots ,stick_number)
    