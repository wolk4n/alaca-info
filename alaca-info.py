import os
import requests
import socket
import optparse
import whois

# RENKLER
sifirla = "\033[0m"
kirmizi = "\033[1;31m"
yesil = "\033[1;32m"
cyan = "\033[1;36m"

# SEMBOLLER
arti = yesil + "[" + kirmizi + "+" + yesil + "]"
eksi = yesil + "[" + kirmizi + "-" + yesil + "]"
bulundu = yesil + "[" + kirmizi + "BULUNDU" + yesil + "]" + sifirla
soru_isareti = yesil + "[" + kirmizi + "?" + yesil + "]"
unlem = yesil + "[" + kirmizi + "!" + yesil + "]"

def logo():
    print(kirmizi + """
   _____  .__                         .___        _____       
  /  _  \ |  | _____    ____ _____    |   | _____/ ____\____  
 /  /_\  \|  | \__  \ _/ ___\\__  \    |   |/    \   __\/  _ \ 
/    |    \  |__/ __ \\  \___ / __ \_  |   |   |  \  | (  <_> )
\____|__  /____(____  /\___  >____  / |___|___|  /__|  \____/ 
        \/          \/     \/     \/           \/             
           
           [ PASSIVE INFORMATION GATHERING TOOL ]
                    # Coded By wolkan """+ yesil +"""    

           [1] WHOIS             [2] DNS LOOKUP
           [3] GEOIP             [4] SUBNET LOOKUP
           [5] HOST FİNDER       [6] PAGE LINKS
           [7] ROBOTS.TXT        [E] EXIT

    """)

while True:
    try:
        logo()

        q  = input(arti + " Choice: ")
        

        if (q == "1"):
            target = input(unlem + " Target Site: ")
            w = whois.whois(target)
            print(w.text)


        elif (q == "2"):
            target = input(unlem + " Target Site: ")
            dnslookup = 'https://api.hackertarget.com/dnslookup/?q='+ target
            info = requests.get(dnslookup)
            print(info.text)


        elif (q == "3"):
            target = input(unlem + " Target IP: ")
            hostname = requests.get("https://ipinfo.io/{}/hostname".format(target)).text
            city = requests.get("https://ipinfo.io/{}/city".format(target)).text
            region = requests.get("https://ipinfo.io/{}/region".format(target)).text
            country = requests.get("https://ipinfo.io/{}/country".format(target)).text
            location = requests.get("https://ipinfo.io/{}/loc".format(target)).text
            organization = requests.get("https://ipinfo.io/{}/org".format(target)).text
            postal = requests.get("https://ipinfo.io/{}/postal".format(target)).text
            time_zone = requests.get("https://ipinfo.io/{}/timezone".format(target)).text
            print("""{} Alan Adı: {}{} Şehir: {}{} Bölge: {}{} Ülke: {}{} Lokasyon: {}{} Organizasyon: {}{} Posta: {}{} Zaman Dilimi: {}""".format(bulundu,hostname,bulundu,city,bulundu,region,bulundu,country,bulundu,location,bulundu,organization,bulundu,postal,bulundu,time_zone))


        elif (q == "4"):
            target = input(unlem + " Target Site: ")
            sublookup = 'https://api.hackertarget.com/subnetcalc/?q='+ target
            info = requests.get(sublookup)
            print(info.text)


        elif (q == "5"):
            target = input(unlem + " Target Site: ")
            pagelinks = 'https://api.hackertarget.com/pagelinks/?q='+ target
            info = requests.get(pagelinks)
            print(info.text)


        elif (q == "6"):
            target = input(unlem + " Target Site: ")
            hostsearch = 'https://api.hackertarget.com/hostsearch/?q='+ target
            info = requests.get(hostsearch)
            print(info.text)


        elif (q == "7"):
            target = input(unlem + " Target Site: ")
            robots ='http://'+target+'/robots.txt'
            info = requests.get(robots)
            print(info.text)

        elif (q == "e" or q == "E"):
            print(eksi + " Exiting the program...")
            break

    except KeyboardInterrupt:
        print(" Exiting the program...")