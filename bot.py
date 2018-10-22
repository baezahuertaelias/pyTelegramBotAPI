import os
import urllib, json
import subprocess
import telebot

bot = telebot.TeleBot("")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	print("El usuario "+ message.from_user.username + " ejecuto el comando " + message.text)
	if "start" in message.text:
		bot.send_message(message.chat.id, message.text)
	
	elif message.text.startswith("/youtube"):

		if(len(message.text)>=10):
			link_video = message.text[9:]
			if "youtu" in link_video:
				nombre_video = "youtube-dl -e "+ link_video
				result = subprocess.check_output(nombre_video, shell=True)
				bot.send_message(message.chat.id, "Dame unos segundos mientras bajo tu video... "+result)
				os.system("youtube-dl -o test"+str(message.date)+".mp4 -f 133 "+link_video)
				bot.send_message(message.chat.id, "Ya lo baje... esta enviandose")
				video = open('test'+str(message.date)+'.mp4', 'rb')
				bot.send_video(message.chat.id, video, timeout=9999)
				video.close()
				os.remove("test"+str(message.date)+".mp4")
				print("Borrado archivo test"+str(message.date)+".mp4")
			else:
				bot.send_message(message.chat.id, "Link incorrecto!!\nRecuerda que el comando tiene que ser \n/youtube https://www.youtube.com/watch?v=XXXXXXXXXs\nO tambien puede ser /youtube youtu.be/XXXXXXXXX")
		else:
			bot.send_message(message.chat.id, "Link incorrecto!!")

	
	elif message.text.startswith("/datos"):
		if(len(message.text)>=8):
			dato=message.text[6:]
			url = "https://api.rutify.cl/search?q="+dato
			response = urllib.urlopen(url)
			data = json.loads(response.read())
			if not data:
				bot.send_message(message.chat.id, "Tu consulta esta mal hecha... revisa")
			else:
				bot.send_message(message.chat.id, "El nombre de la persona es: "+data[0]["name"]+"\ny el rut es: "+data[0]["rut"])

	elif message.text.startswith("/ayuda"):
		bot.send_message(message.chat.id, "Hola! tengo los siguentes comandos:\n /youtube linkdelvideo\n /datos rut o nombre")

	else:
		bot.send_message(message.chat.id, "Avispate masturba colibries, el texto \"" + message.text + "\" no existe")

bot.polling()
