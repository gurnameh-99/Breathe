import requests

resp = requests.post("http://localhost:5000/", files={'file': open('./Respiratory_Sound_Database/audio_and_txt_files/103_2b2_Ar_mc_LittC2SE.wav', 'rb')})

print(resp.json())