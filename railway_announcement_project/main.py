
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def textToSpeech1(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    
    

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1 - Generate kripya dheyan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is from-city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 7 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 is platform number

    # 11 - Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")

    #1.1 may i have ur attention please
    start = 19000
    finish = 23600
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_eng.mp3", format="mp3")

    #1.2 train no. and train name

    #1.3 from
    start=30000
    finish=31200
    audioProcessed=audio[start:finish]
    audioProcessed.export("3_eng.mp3",format="mp3")

    #1.4 from city name

    #1.5 to
    start=31700
    finish=32500
    audioProcessed=audio[start:finish]
    audioProcessed.export("5_eng.mp3",format="mp3")

    #1.6 to city name

    #1.7 via
    start=33500
    finish=34700
    audioProcessed=audio[start:finish]
    audioProcessed.export("7_eng.mp3",format="mp3")
    
    #1.8 via city name

    #1.9 is arriving shortly on
    start=36500
    finish=39000
    audioProcessed=audio[start:finish]
    audioProcessed.export("9_eng.mp3",format="mp3")

    #1.10 
    start=39000
    finish=40400
    audioProcessed=audio[start:finish]
    audioProcessed.export("10_eng.mp3",format="mp3")


    #1.11 platform number

    #1.12 end tune
    start=41200
    finish=42000
    audioProcessed=audio[start:finish]
    audioProcessed.export("12_eng.mp3",format="mp3")




def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from-city
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4 - Generate via-city
        textToSpeech(item['via'], '4_hindi.mp3')

        # 6 - Generate to-city
        textToSpeech(item['to'], '6_hindi.mp3')

        # 8 - Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')

        # 10 - Generate platform number
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}_hindi.mp3", format="mp3")
    
    for index,item in df.iterrows():
        #1.2 train no and train name
        textToSpeech1(item['train_no']+" " + item['train_name'], '2_eng.mp3')

        #1.4
        textToSpeech1(item['from'] , '4_eng.mp3')

        #1.6 
        textToSpeech1(item['to'] , '6_eng.mp3')

        #1.8
        textToSpeech1(item['via'] , '8_eng.mp3')

        #1.11
        textToSpeech1(item['platform'] , '11_eng.mp3')

        audios=[f"{i}_eng.mp3" for i in range(1,13)]
        announcement=mergeAudios(audios)
        announcement.export( f"announcement_{item['train_no']}_{index+1}_eng.mp3", format="mp3")


def move_files(source_folder,target_folder):
    try:
        for path,dir,files in os.walk(source_folder):
            for file in files:
                if str(file).startswith('announcement_1'):
                    os.rename(path + '\\' + file , target_folder +file)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
    source_folder=r'C:\Users\Dhairya\OneDrive\Desktop\railway_announcement_project'+'\\'
    target_folder=r'C:\Users\Dhairya\OneDrive\Desktop\announcements'+'\\'
    #create a new folder at particular location and copy that path as target folder's path to store all the generated announcements

    move_files(source_folder,target_folder)
    

