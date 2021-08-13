# Spaghetti code by Simon Pitra 8/13/2021
# midi-router 1.0
# A simple midi interface that allows the user to pick a midi device
# to listen on, and a second to send midi info to. 
# Originally created as a hacky way to play a volca keys with a 
# digital piano.

import mido
from mido import Message

#main function to handle UI and pass off to route
def main():
	print("Welcome to midi-router!\n")
	selection = input("Press (1) to send a test note.\nPress (2) to route midi.\nPress (3) to exit.\n")

	if(selection == "1"):
		testNotes()
	elif(selection == "2"):
		route()
	elif(selection == "3"):
		quit()		
	else:
		print("Please enter a valid number.")
		main()


#Handles routing of midi notes from a user designated input to a user designated midi output
def route():
	
	midiInPort = ""
	midiOutPort = ""
	midiChannel = ""
	
	inputs = getInputs()
	outputs = getOutputs()
	
	inputLoop = True
	
	#Loop to ensure user enters valid numbers. Newlines for readability on user end. Ditto for outputLoop and channelLoop.
	while inputLoop:
		print("\n")
		print(inputs)
		print("\n")
		#Prompts user to select which midi port to listen on for input
		selection = input(f"Select midi input (1 - {len(inputs)}) ")
		if selection in inputs:
			midiInPort = inputs[selection]
			print(f'You picked {midiInPort}. Setting as Input.')
			inputLoop = False
			
	outputLoop = True
	
	
	while outputLoop:
		print("\n")
		print(outputs)
		print("\n")
		#Prompts user to select which midi port to send recieved notes to.
		selection = input(f"Select midi output (1 - {len(outputs)}) ")
		if selection in outputs:
			midiOutPort = outputs[selection]
			print(f'You picked {midiOutPort}. Setting as output.')
			outputLoop = False
		
	channelLoop = True	
	while channelLoop:
		#Prompts user for which midi channel to send notes on
		midiChannel = input("Select a midi channel (1 - 16)")
		if int(midiChannel) > 0 and int(midiChannel) < 17:
			midiChannel = int(midiChannel)
			midiChannel -= 1
			print(f"You have selected channel {midiChannel + 1}. Setting as midi channel. ")
			channelLoop = False
	#Opens necessary input and output ports with mido
	inport = mido.open_input(midiInPort)
	outport = mido.open_output(midiOutPort)
	
	#Workaround for a clean exit. The for loop listens for input on the input port and sends it to the specified output.
	#try except statement is so the user can exit cleanly. Closes ports once ctrl + c is pressed.
	try:
		while True:
			print("Port is open, try playing something! (press ctrl + c to quit)")
			for msg in inport: #.iter_pending():
				outport.send(msg.copy(channel=midiChannel))
	except KeyboardInterrupt:
		inport.close()
		outport.close()
		quit()
			

				
		
		
	
	
			
	
	
			

		
	
# Uses mido to find valid midi inputs, then assigns them to a dict for 
# easy numerical selection on user end.
def getInputs():
	rawInputs = mido.get_input_names()
	rawKeys = []
	result = {}
	for i in range(len(rawInputs)):
		rawKeys.append(str(i + 1))
		
	for i in range(len(rawInputs)):
		result.update({rawKeys[i]:rawInputs[i]})
		
	return result
# Uses mido to find valid midi outputs, then assigns them to a dict 
# for easy numerical selection on user end.
def getOutputs():
	rawOutputs = mido.get_output_names()
	rawKeys = []
	result = {}
	for i in range(len(rawOutputs)):
		rawKeys.append(str(i + 1))
		
	for i in range(len(rawOutputs)):
		result.update({rawKeys[i]:rawOutputs[i]})
		
	return result
			
	
		
	
# Lazy copy paste of the above output code in the route() function.
# Lets the user pick an output and channel to send a note to.
# Added to allow user to see which outputs correspond to their devices.
def testNotes():
	midiOutPort = ""
	midiChannel = ""
	
	outputs = getOutputs()
	outputLoop = True
	while outputLoop:
		print("\n")
		print(outputs)
		print("\n")
		selection = input(f"Select midi output (1 - {len(outputs)}) ")
		if selection in outputs:
			midiOutPort = outputs[selection]
			print(f'You picked {midiOutPort}. Setting as output.')
			outputLoop = False
		
	channelLoop = True	
	while channelLoop:
		midiChannel = input("Select a midi channel (1 - 16)")
		if int(midiChannel) > 0 and int(midiChannel) < 17:
			midiChannel = int(midiChannel)
			midiChannel -= 1
			print(f"You have selected channel {midiChannel + 1}. Setting as midi channel. ")
			channelLoop = False
			
	outport = mido.open_output(midiOutPort)
	msg = Message('note_on', note=60, channel=midiChannel, time=10)
	outport.send(msg)
	input("Press any key to stop note")
	msg = Message('note_off', note=60)
	outport.send(msg)
	outport.close()
	
	
#Main function call down here.
main()
