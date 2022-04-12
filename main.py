import speech_recognition as sr
# recognize_google() : Google Web Speech API
# recognize_google_cloud() : Google Cloud Speech API
# recognize_bing() : Microsoft Bing Speech API
# recognize_houndify() : SoundHound Houndify API
# recognize_ibm() : IBM Speech to Text API
# recognize_wit() : Wit.ai API
# recognize_sphinx() : CMU Sphinx (오프라인에서 동작 가능)

# r = sr.Recognizer() # Recognizer 객체 생성
# wav_file = sr.AudioFile('./thanks.wav') # Wav파일 읽어오고
#
# print(">>> STT ...")
# with wav_file as source: # 파일 알아서 닫혀주기
#     audio = r.record(source)
#     #print(r.recognize_google(audio_data=audio, language='ko-KR')) # en-EN
#     print(r.recognize_google(audio_data=audio, language='en-EN'))  # en-EN
# ================================

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# 구글 웹 음성 API로 인식하기 (하루에 제한 50회)
try:
    print("Google Speech Recognition thinks you said : " + r.recognize_google(audio, language='ko'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


# microphone에서 auido source를 생성합니다
# r2 = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r2.listen(source)
#
# # 구글 웹 음성 API로 인식하기 (하루에 제한 50회)
# try:
#     print("Google Speech Recognition thinks you said : " + r2.recognize_google(audio, language='en-EN'))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))