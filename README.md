# midi-router
A short python script that allows a user to route midi input from one device to midi output on another.

I created this script as a workaround to plug my digital piano (USB midi out) into my volca keys (analogue midi in). 
I am a programming novice, don't judge too harshly. 

-Requirements-

Mido https://mido.readthedocs.io/en/latest/ 

Python-rtmidi https://spotlightkid.github.io/python-rtmidi/installation.html

-Usage-

Run with the command (debian based distros):
python3 midi-router.py

The program presents you with three options upon startup. 
1. Test notes
2. Route midi
3. Exit

Test notes allows you to send a note to a specified output on a specified midi channel. 
This was implemented to allow the user to figure out which output corresponds to each device should 
the output names not make it obvious (as in my case).

Route midi allows you to select a midi device to listen to as an input and send note information to an output. 
The user has control over where the output is sent, and on what midi channel.

Exit simply exits the program.

Thank you for reading! I hope you find this useful!
Feel free to fork, modify, or do whatever with this code.

Donations accepted, never expected.
ALGO wallet
7S2E7FAGF34YRZX7WCJUR52W6QWT6VB6UVBUXQF6AR5KBFFBCVLRWBJ7LI








