class Convolutional:
	def create_state_machine(self,input_string):

		state_machine = {}
		state_00 = {}
# output next_state
		state_00['0'] = ("00","00")
		state_00['1'] = ("11","10")
		state_machine["00"] = state_00
		state_01 = {}
		state_01['0'] = ("10","00")
		state_01['1'] = ("01","10")
		state_machine["01"] = state_01
		state_10 = {}
		state_10['0'] = ("11","01")
		state_10['1'] = ("00","11")
		state_machine["10"] = state_10
		state_11 = {}
		state_11['0'] = ("01","01")
		state_11['1'] = ("10","11")
		state_machine["11"] = state_11

		current_state = "00"
		output_string = ""
		for i in range(len(input_string)):
	
			output_string += state_machine[current_state][input_string[i]][0]
	
			current_state = state_machine[current_state][input_string[i]][1]

		return output_string
	def main(self,input_string):
		output_string = self.create_state_machine(input_string)
		return output_string



	
