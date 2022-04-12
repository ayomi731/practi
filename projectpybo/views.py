from django.shortcuts import render
from django.http import HttpResponse
import speech_recognition as sr
from .models import p_test
import datetime
from django.template import loader
import time


# Create your views here.

# 메인 페이지
def main(request):
    return render(request, 'main.html')

# 문제 연습 페이지
def example(request):
    # 준비시간 45초
    #time.sleep(10)

    def countdown(time_sec):
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = '00:{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            time_sec -= 1
        # print("stop")


    return render(request, 'example.html', {'countdown': countdown(45)})


def index(request):
    # recognize_google() : Google Web Speech API
    # recognize_google_cloud() : Google Cloud Speech API
    # recognize_bing() : Microsoft Bing Speech API
    # recognize_houndify() : SoundHound Houndify API
    # recognize_ibm() : IBM Speech to Text API
    # recognize_wit() : Wit.ai API
    # recognize_sphinx() : CMU Sphinx (오프라인에서 동작 가능)
    comment = ''
    rec = ''

    r = sr.Recognizer()  # Recognizer 객체 생성
    wav_file = sr.AudioFile('./thanks.wav')  # Wav파일 읽어오고

    print(">>> STT ...")
    with wav_file as source:  # 파일 알아서 닫혀주기
        audio = r.record(source)
        # print(r.recognize_google(audio_data=audio, language='ko-KR')) # en-EN
        print(r.recognize_google(audio_data=audio, language='en-EN'))  # en-EN
        answer = r.recognize_google(audio_data=audio, language='en-EN')

        comment += str(answer) + "</br> 읽어주세요! "

    # ============================================================

    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r2.listen(source)

    # 구글 웹 음성 API로 인식하기 (하루에 제한 50회)
    try:
        print("Google Speech Recognition thinks you said : " + r2.recognize_google(audio, language='en-EN'))
        rec = r2.recognize_google(audio, language='en-EN')
        # p_testDatas = p_test(p_file=request.POST['p_file'], p_text=request.POST['p_text'],
        #                     p_date = request.POST['p_date'])
        # p_testDatas.save()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())
    # answerLength = len(answer)
    # recLength = len(rec)
    # score = (recLength / answerLength) * 100
    #
    # print("정답 길이" + str(answerLength))
    # print("")

    comment += ("</br> 사용자 음성 : " + str(rec))

    answerList = answer.split()
    recList = rec.split()

    wrong = []
    from itertools import zip_longest
    for list1, list2 in zip_longest(answerList, recList):
        if not list1 == list2:
            wrong.append(list1)

    context = {'answer': answer, 'rec': rec, 'wrong': wrong}

    # str(answer) + "</br>  읽어주세요!" + "</br> 사용자 : " + str(rec) + "</br> 점수는 " + str(round(score))
    return render(request, 'example.html', context)  # en-EN

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


