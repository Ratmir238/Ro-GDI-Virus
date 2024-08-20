from playsound import playsound
import os

os.system("StartGDI.bat")
audio_file = "RunMusic.mp3"
playsound(audio_file)
print ("OK")
os.system("Kill_1_GDI.bat")

os.system("StartGDI2.bat")
audio_file = "xz128.mp3"
playsound(audio_file)
print ("OK")
os.system("Kill_2_GDI.bat")

os.system("StartGDI3.bat")
audio_file = "Part1.mp3"
playsound(audio_file)
print ("OK")
os.system("Kill_3_GDI.bat")

os.system("StartGDI4.bat")
audio_file = "Part2.mp3"
playsound(audio_file)
print ("OK")
os.system("Kill_4_GDI.bat")

os.system("StartGDI5.bat")
audio_file = "Part3.mp3"
playsound(audio_file)
print ("OK")
os.system("Kill_5_GDI.bat")
