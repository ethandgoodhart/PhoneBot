import speech_recognition as sr
import random
import sys
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

name = ""

if len(sys.argv) < 3:
    name = input("What is your first name: ")

cautious_mode = False

if len(sys.argv) > 1:
    cautious_mode = (sys.argv[1].split("cautious-mode=")[1].replace("t", "T").replace("f", "F") == 'True')

recording_audio = {"1": "yeah yeah", "2": "yeah that sounds right", "3": "umm im not sure", "4": "hey how is it going umm whatchu up to", "5": "how is it going", "6": "yeah I have", "7": "no I have not", "8": "here let me see", "9": "here", "10": "hey im here", "11": "yeah no problem", "12": "hey how you doing", "13": "did you see the game last night it was crazy", "14": "oh my god I cant believe we lost last night", "15": "umm give me one second to check", "16": "yeah give me one second", "17": "umm I dont know", "18": "bonjour", "19": "what", "20": "I dont understand what youre saying", "21": "not much what about you", "22": "thats good", "23": "okay", "24": "Im good uh how are you", "25": "yeah", "26": "yeah no problem", "27": "yeah sure", "28": "could you repeat that", "29": "alright", "30": "sounds good", "31": "oh okay", "32": "yeah", "33": "no", "34": "no thats crazy", "35": "wow", "36": "im good how about you", "37": "good", "38": "see yah", "39": "no fuck you", "40": "umm", "41": "it was pretty easy", "42": "sorry umm its not working", "43": "oh umm im having some problems with my internet", "44": "uh not sure", "45": "yes", "46": "i dont know yet"}
intents = {"why": "3 or 17", "did you": "1 or 25 or 32 or 45", "that right": "2", "sound correct": "2", "sounds correct": "2", "do you know": "3 or 8 or 17", "know how": "3 or 8", "hey": "4 or 12", "sup": "4", "whats up": "21", "hello": "5 or 4 or 12", "hi": "5 or 4 or 12", "you have": "6 or 15", "have you": "6 or 7 or 15", "you check": "8 or 15 or 16", "do you know if": "3 or 8 or 15 or 17",  name + " here": "9 or 10", "is " + name: "9", "are you here": "9 or 10", "is there any way": "11", "you could": "11", "could you": "11", "can you see if": "15 or 16", "bonjour": "18", "anything going on": "21", "finished": "22", "so happy": "22", "finally": "22", "Ethan": "9 or 10", "thanks": "25 or 26", "thank you": "25 or 26", "really appreciate": "25 or 26", "cool": "23 or 25 or 32", "so nice": "25 or 26 or 32", "want to": "27", "you done": "25", "homework": "25 or 32", "did you see": "25 or 33", "can you believe": "33 or 34 or 35", "you believe": "33 or 34 or 35", "easy": "38 or 25 or 32 or 33", "know what time": "25 or 33", "can you": "27", "understand": "25", "hows day": "36 or 37", "when is": "17 or 44", "what do": "17 or 44 or 15", "how many": "17 or 44 or 15", "due": "17 or 44 or 15", "hard": "38 or 25 or 32 or 33 or 45", "do you": "33", "bye": "38", "see you later": "38", "see yah": "38", "see ah": "38", "what do you": "17 or 44", "what are your": "17", "what is": "3 or 17", "f*** you": "39", "whats": "3 or 17", "whats": "3 or 17", "is that": "1 or 25 or 27 or 32 or 45", "okay": "25 or 32", "how easy": "41", "how hard": "41", "you like": "1 or 25 or 33", "its crazy": "25 or 35", "could you": "42 or 43", "would you want": "27", "did finish": "25 or 33 or 45", "has everyone": "25 or 33 or 45", "have you": "25 or 33 or 45 or 7", "are you": "25 or 33 or 45", "will you": "25 or 33 or 45", "how you doing": "24", "how are you": "24", "it was crazy": "31 or 35", "it was insane": "31 or 35", "is it": "17 or 3", "are we": "17 or 3", "goodbye": "38", "do you know when": "46", "who are you going to": "46"}
lb = "---------------------------------------------------------------------------------------------------------------------"

print(lb + bcolors.OKGREEN + """
  _____  _                        ____        _   
 |  __ \\| |                      |  _ \\      | |  
 | |__) | |__   ___  _ __   ___  | |_) | ___ | |_ 
 |  ___/| '_ \\ / _ \\| '_ \\ / _ \\ |  _ < / _ \\| __|
 | |    | | | | (_) | | | |  __/ | |_) | (_) | |_ 
 |_|    |_| |_|\\___/|_| |_|\\___| |____/ \\___/ \\__|
                                                  
""" + bcolors.ENDC)
print(bcolors.HEADER + "Cautious Mode = " + str(cautious_mode) + bcolors.ENDC + "\n" + lb)

def process_command(c):
    found = False
    print('Input: ' + c)

    for key, value in list(reversed(sorted(intents.items(), key=len))):
        arr1 = c.replace("\'", "").split(" ")
        arr2 = key.replace("\'", "").lower().split(" ")

        if all(elem in arr1 for elem in arr2):
            found = True

            if "or" in value:
                ops = value.split(" or ")
                sel = ops[random.randint(0, len(ops) - 1)]
                print("Response: " + recording_audio[sel] + "\n" + lb)
                respond("Recordings/New\\ Recording\\ " + sel + ".flac")
                break
            else:
                print("Response: " + recording_audio[value] + "\n" + lb)
                respond("Recordings/New\\ Recording\\ " + value + ".flac")
                break

    if (not found) and (cautious_mode):
        if "*" in c.replace("\'", ""):
            value = "23 or 35"
            ops = value.split(" or ")
            sel = ops[random.randint(0, len(ops) - 1)]
            print("Response: " + recording_audio[sel] + "\n" + lb)
            respond("Recordings/New\\ Recording\\ " + sel + ".flac")
        else:
            print("Being Cautious So No Response\n" + lb)
    elif (not found) and (not cautious_mode):
        if "*" in c.replace("\'", ""):
            value = "23 or 35"
            ops = value.split(" or ")
            sel = ops[random.randint(0, len(ops) - 1)]
            print("Response: " + recording_audio[sel] + "\n" + lb)
            respond("Recordings/New\\ Recording\\ " + sel + ".flac")
        else:
            resz = ["19", "19", "20", "23", "23", "23", "23", "28", "29", "29", "30", "30", "31", "31", "25", "40"]
            res = resz[random.randint(0, len(resz) - 1)]
            print("Response Not Found: " + recording_audio[res] + "\n" + lb)
            respond("Recordings/New\\ Recording\\ " + res + ".flac")

def respond(file_name):
    os.system("afplay " + file_name)


r = sr.Recognizer()
m = sr.Microphone()
r.energy_threshold = 15

with m as source:
    r.adjust_for_ambient_noise(source)

while True:
    with m as source:
        audio = r.listen(source)

    try:
        process_command(str(r.recognize_google(audio)).lower())
    except sr.UnknownValueError:
        continue
    except sr.RequestError as e:
        continue
