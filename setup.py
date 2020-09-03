import speech_recognition as sr
import time
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print('\nSetting up ' + bcolors.OKGREEN + 'PhoneBot' + "\n" + bcolors.ENDC)

r = sr.Recognizer()
mic = sr.Microphone()

recording_audio = {"1": "yeah yeah", "2": "yeah that sounds right", "3": "umm im not sure", "4": "hey how is it going umm whatchu up to", "5": "how is it going", "6": "yeah I have", "7": "no I have not", "8": "here let me see", "9": "here", "10": "hey im here", "11": "yeah no problem", "12": "hey how you doing", "13": "did you see the game last night it was crazy", "14": "oh my god I cant believe we lost last night", "15": "umm give me one second to check", "16": "yeah give me one second", "17": "umm I dont know", "18": "bonjour", "19": "what", "20": "I dont understand what youre saying", "21": "not much what about you", "22": "thats good", "23": "okay", "24": "Im good uh how are you", "25": "yeah", "26": "yeah no problem", "27": "yeah sure", "28": "could you repeat that", "29": "alright", "30": "sounds good", "31": "oh okay", "32": "yeah", "33": "no", "34": "no thats crazy", "35": "wow", "36": "im good how about you", "37": "good", "38": "see yah", "39": "no fuck you", "40": "umm", "41": "it was pretty easy", "42": "sorry umm its not working", "43": "oh umm im having some problems with my internet", "44": "uh not sure", "45": "yes", "46": "i dont know yet"}
lb = "---------------------------------------------------------------------------------------------------------------------"

print('Testing the microphone... Say "Hey PhoneBot" to continue')

with mic as source:
	try:
		r.listen(source, 4, 3)
		print("Microphone is working properly." + "\n")
	except:
		print("Microphone is not working try setting a different input in System Preferences." + "\n")
		raise SystemExit

for phrase in recording_audio.items():
	time.sleep(0.75)

	print(lb + "\n" + 'Say ' + bcolors.HEADER + '"' + phrase[1] + '"' + bcolors.ENDC)

	with mic as source:
	    audio = r.listen(source, 3.5, len(phrase[1]) / 4)

	with open("Recordings/New Recording " + phrase[0] + ".flac", "wb") as file:
	    file.write(audio.get_flac_data())
	    print(str(phrase[0]) + " out of " + str(len(recording_audio.items())) + " recordings finished" + bcolors.ENDC)

print("\n\n" + "Hooray! Phone bot is set up and ready for use.")
