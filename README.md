# PhoneBot

Make a chatbot that talks in your voice and responds out loud.<br/><br/>

How to setup
------
Open the Terminal app on your mac then paste the following code:

```
git clone https://github.com/ethandgoodhart/PhoneBot/
cd PhoneBot/
mkdir Recordings
pip3 install SpeechRecognition==3.8.1 PyAudio
python3 setup.py
```
<br/><br/>

Microphone configuration
------
If you want to just be able to talk to PhoneBot without it being able to hear sounds from inside your computer, skip to the How to run section. But if you want to make PhoneBot able to hear sounds coming from inside the computer such as hearing someone talk on a FaceTime, make sure to follow these steps:
1. Install BlackHole audio routing: https://github.com/ethandgoodhart/PhoneBot/raw/master/BlackHole.v0.2.6.pkg
2. Go to System Preferences > Sound and click on Input; Make sure that BlackHole 16ch is selected
3. Open up the Audio MIDI Setup app, and click on the small plus in the bottom left corner
4. Click on Create Multi-Output Device, then make sure that Built-in Output and BlackHole 16ch are both selected
5. Lastly, go back to System Preferences > Sound and click on Output; Select Multi-Output Device and you are ready to go!

How to run
------
In terminal, run the following code but replace NAME with your first name:

```
python3 script.py cautious-mode=false NAME
```
