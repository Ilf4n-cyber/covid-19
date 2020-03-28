#!/bin/usr/python3.8.2
# ^_^ coding:utf-8 ^_^
# Recode lah kena virud kau :v

try:
	import os,sys,json, requests
	from time import sleep
except Exception as R:
	exit("[ModuleNotFound]> %s"%(R))
	

class main:
	def __init__(self):
		self.main()
	
	def berita():
		dat=open('data.json')
		a=json.loads(dat.read())
		os.system('clear')
		print("[+]      Welcome      [+]".center(56))
		os.system('figlet Covid-19')
		print(58*"-")
		print("[+] Author : "+a["author"])
		print("[+] Fungsi : Melihat data kasus dari Virus Corona")
		print("""
	{01} Data dari seluruh Indonesia
	{02} Data dari semua Negara Asia
	{03} Data dari seluruh Dunia
	{00} Keluar
		""")
		while True:
			try:
				pilih=input("[Masukkan Nomor ] : ")
				if pilih in ['1','01']:
					sleep(1)
					data.indonesia()
				if pilih in ['2','02']:
					sleep(1)
					data.asia()
				elif pilih in ['3','03']:
					sleep(1)
					data.dunia()
				elif pilih in ['0','00']:
					exit("[!]\033[1;91m Keluar dari program!\033[0m")
				else:
					print("[!] Pilihan agan tidak ada!")
			except IOError: exit()
			except KeyboardInterrupt: exit()
		
	def start():
		try:
			data=open('data.json')
			datas=json.loads(data.read())
			if 'LeON' or 'Maestro Alvardo' in datas["author"]:
				sleep(1)
				print("[!] Server : \033[1;92m"+datas["server"]+"\033[0m")
				sleep(2)
				main.berita()
			else:
				sleep(2)
				exit("Hai saya : "+datas["author"]+" saya mengubah author aslinya h3h3")
		except IOError:
			exit("[!] Terjadi kesalahan!")
		except KeyboardInterrupt: exit()
		
class data:
	def __init__(self):
		self.data()
		
	def indonesia():
		os.system('clear')
		data=requests.get("https://api.kawalcorona.com/indonesia")
		datas=data.json()
		print("[+] Data Kasus Covid-19 di Indonesia [+]".center(25))
		print(58*"-")
		print("[+] Negara             : \033[96mRepublik "+datas[0]['name']+"\033[0m")
		print("[+] Positif Terjangkit\033[0m :\033[1;93m "+str(datas[0]['positif'])+"\033[97m orang\033[0m")
		print("[+] Sembuh             :\033[1;92m "+str(datas[0]['sembuh'])+"\033[1;97m orang\033[0m")
		print("[+] Meninggal          : \033[1;91m"+str(datas[0]['meninggal'])+"\033[1;97m orang\033[0m")
		print(58*"-")
		print("[!] \033[1;91mJangan lupa jalankan Program ini setiap hari\n    untuk melihat data update!")
		input("\n\033[0mTekan enter untuk kembali.....")
		main.berita()
	
	def dunia():
		os.system('clear')
		positif=requests.get("https://api.kawalcorona.com/positif").json()
		sembuh=requests.get("https://api.kawalcorona.com/sembuh").json()
		meninggal=requests.get("https://api.kawalcorona.com/meninggal").json()
		print("[+] Data Kasus Covid-19 di Seluruh Dunia [+]".center(25))
		print(58*"-")
		print("[+] Positif Terjangkit\033[0m :\033[1;93m "+str(positif['value'])+"\033[1;97m orang\033[0m")
		print("[+] Sembuh             :\033[1;92m "+str(sembuh['value'])+"\033[1;97m orang\033[0m")
		print("[+] Meninggal          : \033[1;91m"+str(meninggal['value'])+"\033[1;97m orang\033[0m")
		print(58*"-")
		print("[!] \033[1;91mJangan lupa jalankan Program ini setiap hari\n    untuk melihat data update!")
		input("\n\033[0mTekan enter untuk kembali.....")
		main.berita()
		
		
	def asia():
		os.system('clear')
		print("[+] Data kasus Covid-19 di semua negara Asia [+] ")
		print(58*"-")
		print("""
[01] Indonesia	   [04] Singapura      [07] Laos
[02] Malaysia	   [05] Thailand       [08] BeruneiDarusalam
[03] China	   [06] Myanmar        [09] Tomor Leste
[10] Kamboja       [99] Kembali        [00] Keluar
		""")
		while True:
			try:
				pilih=input("[Masukkan Nomor ] : ")
				if pilih in ['1','01']:
					sleep(1)
					data.indonesia()
				elif pilih in ['2','02','3','03','4','04','5','05','6','06','7','07','8','08','9','09','10']:
					sleep(1)
					exit("[!] Mohon maaf tunggu update terbaru dari Tools ini!")
					asia.malaysia()
				elif pilih in ['99']:
					main.berita()
				elif pilih in ['0','00']:
					exit("[!] Keluar dari program!")
				else:
					sleep(1)
					print("[!] Pilihan kamu tidak ada!")
			except KeyboardInterrupt: exit()
					
class asia:
	def __init__(self):
		self.asia()
		
	def malaysia():
		os.system('clear')
		data=requests.get("https://api.kawalcorona.com/malaysia")
		datas=data.json()
		negara=str(datas['{"Country_Region":"Malaysia"}'])
		print("[+] Data Kasus Covid-19 di Indonesia [+]".center(25))
		print(58*"-")
		print("[+] Negara             : \033[96mRepublik "+negara+"\033[0m")
		#print("[+] Positif Terjangkit\033[0m :\033[1;93m "+str(datas[0]['positif'])+"\033[97m orang\033[0m")
		#print("[+] Sembuh             :\033[1;92m "+str(datas[0]['sembuh'])+"\033[1;97m orang\033[0m")
		#print("[+] Meninggal          : \033[1;91m"+str(datas[0]['meninggal'])+"\033[1;97m orang\033[0m")
		#print(58*"-")
		#print("[!] \033[1;91mJangan lupa jalankan Program ini setiap hari\n    untuk melihat data update!")
		input("\n\033[0mTekan enter untuk kembali.....")
		main.berita()
	
		
main.start()
