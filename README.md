# PhoneBot

Make a chatbot that talks in your voice and responds out loud.<br/><br/>

How to setup
------
1. Install BlackHole audio routing: https://github.com/ethandgoodhart/PhoneBot/raw/master/BlackHole.v0.2.6.pkg
2. Open the Terminal app on your mac then paste the following code:

```
git clone https://github.com/ethandgoodhart/PhoneBot/
cd PhoneBot/
mkdir Recordings
pip3 install SpeechRecognition==3.8.1 PyAudio
python3 setup.py
```
<br/>

How to run
------
In terminal, run the following code but replace NAME with your first name:

```
python3 script.py cautious-mode=false NAME
```
