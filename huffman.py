import heapq
import os
import scipy.io


probability = scipy.io.loadmat('freq.mat')
dictionary = huffman_code = {}


class Node:
	def __init__(self, char, freq):
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None

	
	def __lt__(self, other):
		return self.freq < other.freq

	def __eq__(self, other):
		if(other == None):
			return False
		if(not isinstance(other, HeapNode)):
			return False
		return self.freq == other.freq


class Huffman:
	def __init__(self):
		#self.text = text
		self.heap = []
		self.codes = {}
		self.reverse_mapping = {}

	def calculate_frequency_of_characters(self):
		frequency = {}
		for _char in self.text:
			if not _char in frequency:
				frequency[_char] = probability['freq'][ord(_char)-97]
			#frequency[_char] += 1
		#for item in frequency:
			#frequency[item] *= probability['freq'][ord(item)-97]
		return frequency

	def make_heap(self, frequency):
		for item in frequency:
			node = Node(item, frequency[item])
			heapq.heappush(self.heap, node)

	def merge_nodes(self):
		while(len(self.heap)>1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)

			merged_node = Node(None, node1.freq + node2.freq)
			merged_node.left = node1
			merged_node.right = node2

			heapq.heappush(self.heap, merged_node)


	def make_codes_from_left_and_right(self, root, code):
		if(root == None):
			return

		if(root.char != None):
			self.codes[root.char] = code
			self.reverse_mapping[code] = root.char
			return

		self.make_codes_from_left_and_right(root.left, code + "0")
		self.make_codes_from_left_and_right(root.right, code + "1")


	def make_codes(self):
		root = heapq.heappop(self.heap)
		code = ""
		self.make_codes_from_left_and_right(root, code)


	def get_encoded_text(self):
		encoded = ""
		for _char in self.text:
			encoded += self.codes[_char]
			huffman_code[_char] = self.codes[_char]
		return encoded


	def encode_text(self):

			frequency = self.calculate_frequency_of_characters()
			self.make_heap(frequency)
			self.merge_nodes()
			self.make_codes()

			encoded = self.get_encoded_text()
			return encoded


	def decode_text(self, encoded):
		code = ""
		decoded = ""

		for item in encoded:
			code += item
			if(code in self.reverse_mapping):
				_char = self.reverse_mapping[code]
				decoded += _char
				code = ""

		return decoded
	def main(self,name):
		#input_string_for_encode = raw_input("Please enter a string for encoding: ")
		self.text = "abcdefghijklmnopqrstuvwxyz"
		encoded_string = self.encode_text()
		encode_text = ""
		for item in name:
			encode_text +=huffman_code[item] 
		return encode_text
		#print("The encoded string is: " + encode_text + "\n")
		#input_string_for_decode= raw_input("Please enter a string for decoding: ")
		#decoded_string = huffman.decode_text(input_string_for_decode)
		#print("The decoded string is: " + decoded_string + "\n")





