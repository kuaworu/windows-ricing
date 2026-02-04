# windows-ricing
### windows ricing - Windowsi välimuse ja käitumise kohandamine, muutes selle sarnasemaks Linuxile.

### Projekti eesmärk
Muuta Windowsi kohandamine sarnaseks Linuxiga, tagades mugava akende haldamise ja rakenduste automaatkäivituse.

---

### README versioonid teistes keeltes:
- [english](README.md)
- [русский](README.ru.md)
- [eesti](README.et.md)

---

# Eelvaade

![l](images/img1.jpg)
![o](images/img2.jpg)
![l](images/img3.jpg)

---

## 1. glazewm

#### glazewm on aknahaldur Windowsi jaoks. See paigutab aknad automaatselt koodi põhjal.

Selles projektis on kasutatud originaalse glazewm repositooriumi konfigu väikeste muudatustega.

---

#### glazewm paigaldamine

Mine sellesse repositooriumisse:
https://github.com/glzr-io/glazewm

Vajuta paremal pool "releases" ja laadi alla sobiv versioon.

Mina kasutasin: v3.9.1 Standalone Installer (x64)

Tööks on vajalik ka zebar:
https://github.com/glzr-io/zebar

Mina kasutasin: v3.2.0 Installer (Windows x64)

---

### Liidese muutmine

1. Käivita zebar administraatori õigustes.
2. Käivita glazewm administraatori õigustes.
3. glazewm peaks ilmuma süsteemsesse salve (system tray).
Kui seda seal pole, mine arvuti seadetesse - Personalization - Taskbar, leia "Other taskbar icons" ja lülita glazewm sisse.
4. Tee süsteemses salves glazewm ikoonil paremklõps ja vali "show config folder".
5. Kopeeri kood minu glazewm/config.yaml failist ja asenda sellega oma konfig, mis laaditi automaatselt koos glazewm-iga.
6. Salvesta ja vajuta klahvikombinatsiooni alt+shift+r - muudatused peaksid rakenduma automaatselt.

---

## 2. Automaatkäivitus arvuti sisselülitamisel

Kui jätta see punkt vahele, siis pärast taaskäivitust glazewm ei tööta, kuni sa seda uuesti administraatorina ei käivita. Et mitte korrata sama tegevust iga kord pärast arvuti käivitamist, tee järgmist:

Paigalda python: https://www.python.org/downloads/

Salvesta minu kood autostart.py, seejärel ava cmd administraatori õigustes ja sisesta käsk:

```
schtasks /create /tn "autostart_glazewm" /tr "C:\Program Files\glzr.io\GlazeWM\glazewm.exe" /sc onlogon /rl highest /f

```

Käivitame läbi cmd, et kood täidetaks kõrgeimate õigustega; kui käivitada kood näiteks läbi Visual Studio, siis see ei toimi.

Ava Task Scheduler (ajaplaneerija) ja leia ülesanne "autostart_glazewm". Kui sa seda näed, siis on kõik õigesti tehtud ja toimib.

---

### Kui midagi ei tööta, võimalikud probleemid:

1. Vale tee glazewm failini cmd käsus ja autostart.py failis. Kontrolli, kuhu glazewm.exe on paigaldatud, ja kui asukoht erineb minu omast, muuda see minu koodi teises reas ja seejärel cmd käsus.
2. Viirusetõrje blokeerib automaatkäivituse. Lülita viirusetõrje ajutiselt välja.
3. Python ei ole käivitatud. Käivita pythoni fail ja vasta konsoolis kõikidele küsimustele "y". Kui pythoni paigaldamisel tekkib probleeme, leia mõni õpetus YouTube'ist ja paigalda python nende juhiste järgi.
