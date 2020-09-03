# PhoneBot

Make a chatbot that talks in your voice and responds out loud.<br/><br/>

How to setup
------
To setup PhoneBot visually follow these steps:
1. Download, and unzip the project folder from here: https://github.com/ethandgoodhart/PhoneBot/archive/master.zip
2. Click on the black **Setup** file and enter your password if necessary, this will install the required dependencies for PhoneBot
3. Click on the black **RecordSamplesFile** file and record your samples
4. Now, whenever you want to run PhoneBot, just click on the black PhoneBot file

To setup PhoneBot via Terminal, follow these steps:
1. Run the following code in Terminal:

```
which python3 >/dev/null 2>&1; if [ $? -eq 1 ]; then /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" && brew install python3; fi
```
2. After that finishes, run this and record your samples:
```
git clone https://github.com/ethandgoodhart/PhoneBot/
cd PhoneBot/
mkdir Recordings
brew install portaudio
pip3 install SpeechRecognition==3.8.1 PyAudio
python3 setup.py
```
3. Whenever you want to run the program now, just run
```
python3 script.py cautious-mode=false YOURFIRSTNAMEHERE
```
<br/>

Microphone configuration
------
If you want to just be able to talk to PhoneBot without it being able to hear sounds from inside your computer, skip to the **How to run section**. But if you want to make PhoneBot able to hear sounds coming from inside the computer such as hearing someone talk on a FaceTime, make sure to follow these steps:
1. Install **BlackHole audio routing**: https://github.com/ethandgoodhart/PhoneBot/raw/master/BlackHole.v0.2.6.pkg
2. Go to *System Preferences > Sound* and click on *Input*; Make sure that **BlackHole 16ch** is selected
3. Open up the **Audio MIDI Setup app**, and click on the small plus in the bottom left corner
4. Click on Create **Multi-Output Device**, then make sure that **Built-in Output** and **BlackHole 16ch** are both selected
5. Lastly, go back to *System Preferences > Sound* and click on *Output*; Select **Multi-Output Device** and you are ready to go!<br/><br/>
