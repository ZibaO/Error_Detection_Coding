
class Viterbi:
    #def __init__(self,received, start_metric,start_path_metric):
       # self.received =received
       # self.start_metric = start_metric
       # self.start_path_metric = start_path_metric
        
 
    def num_of_different_bit(self,num1,num2):
        count=0;
        for i in range(0,len(num1),1):
            if num1[i]!=num2[i]:
                count=count+1
        return count
 
    def viterbi(self):
    
        V = [{}]
        for state in self.state_machine:
            V[0][state] = {"PM": self.start_path_metric[state]}

        for t in range(1, len(self.received)+1):
            V.append({})
            for state in self.state_machine:
                prev_state = self.state_machine[state]['upper_branch']['prev']
                upper_branch_PM = V[(t-1)][prev_state]["PM"] + self.num_of_different_bit(self.state_machine[state]['upper_branch']['out'], self.received[t - 1])
                prev_state = self.state_machine[state]['lower_branch']['prev']
                lower_branch_PM = V[(t - 1)][prev_state]["PM"] + self.num_of_different_bit(self.state_machine[state]['lower_branch']['out'], self.received[t - 1])
                if upper_branch_PM < lower_branch_PM:
                    V[t][state] = {"PM": upper_branch_PM, "branch": 'upper_branch'}
                
                else:
                    V[t][state] = {"PM" : lower_branch_PM,"branch":'lower_branch'}
        #for state in self.state_machine:
            #for t in range(0,len(V)):
               # print V[t][state]["PM"],
           # print ""
       # print ""
        smaller = min(V[len(self.received)][state]["PM"] for state in self.state_machine)
        answer = ""
        for state in self.state_machine:
            if V[len(self.received)][state]["PM"] == smaller:
                source_state = state
                for t in range(len(self.received),0,-1):
                    branch = V[t][source_state]["branch"]
                    answer += str(self.state_machine[source_state][branch]['input'])
                    source_state = self.state_machine[source_state][branch]['prev']
        return answer[::-1]

    def main(self,input_string_for_decode):
        self.start_path_metric = {'state_00':0,'state_01':float("inf"), 'state_10':float("inf"),'state_11':float("inf")}
        self.state_machine = {
            'state_00': {'upper_branch': {'out':"00",'prev': 'state_00','input':0},
                'lower_branch': {'out':"10",'prev': 'state_01','input':0}},
            'state_01': {'upper_branch': {'out': "11", 'prev': 'state_10', 'input': 0},
                'lower_branch': {'out': "01", 'prev': 'state_11', 'input': 0}},
            'state_10': {'upper_branch': {'out': "11", 'prev': 'state_00', 'input': 1},
                'lower_branch': {'out': "01", 'prev': 'state_01', 'input': 1}},
            'state_11': {'upper_branch': {'out': "00", 'prev': 'state_10', 'input': 1},
                'lower_branch': {'out': "10", 'prev': 'state_11', 'input': 1}},
 
        }
        #input_string_for_decode = raw_input("Please enter a string for decoding: ")
        self.received = []
        for i in range(0,len(input_string_for_decode),2):
            self.received.append(input_string_for_decode[i:i+2])
        return self.viterbi()


   
        
   

    

