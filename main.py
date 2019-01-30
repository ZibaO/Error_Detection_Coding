import huffman
import convolutional
import viterbi
import random
def noise(input):
    output = ''
    for i in range(0, len(input)):
        r = random.uniform(0, 1)
        if(r < 0.1):
            output += str(1 - int(input[i]))
        else:
            output += (input[i])
    return output
if __name__ == '__main__':
	#input_string_for_encode = raw_input("Please enter your name: ")
	input_string_for_encode = "zibaomidvar"
	huff = huffman.Huffman()
	conv =convolutional.Convolutional()
	viter =viterbi.Viterbi()
	output_of_huffman_encoder = huff.main(input_string_for_encode)
	print("Output of huffman encoder: "+output_of_huffman_encoder)
	output_of_convolutional_encoder = conv.main(output_of_huffman_encoder)
	print("Output of convolutional encoder: "+output_of_convolutional_encoder)
	output_of_noise_function = noise(output_of_convolutional_encoder)
	print("Output of noise function: "+output_of_noise_function)
	output_of_viterbi_decoder = viter.main(output_of_noise_function)
	print("Output of viterbi decoder: "+output_of_viterbi_decoder)
	output_of_huffman_decoder = huff.decode_text(output_of_viterbi_decoder)
	print("Output of huffman decoder: "+output_of_huffman_decoder)
	print("Final output: "+output_of_huffman_decoder)



	  
  
	