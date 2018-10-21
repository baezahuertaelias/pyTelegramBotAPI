import os
import subprocess
import telebot

bot = telebot.TeleBot("")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	print("El usuario "+ message.from_user.username + " ejecuto el comando " + message.text)
	print(message.text.find("you"))
	if "start" in message.text:
		bot.send_message(message.chat.id, message.text)
	elif message.text.find("you")>=8:
		print("entro al true")
		if len(message.text) < 9:
			print("a")
			bot.send_message(message.chat.id, "Largo no valido")
		else:
			print("b")
			if "/youtube" in message.text:
				link_video = message.text[9:]
			else:
				link_video = message.text

			
			nombre_video = "youtube-dl -e "+ link_video
			result = subprocess.check_output(nombre_video, shell=True)
			bot.send_message(message.chat.id, "Dame unos segundos mientras bajo tu video... "+result)
			os.system("youtube-dl -o test.mp4 -f mp4 "+link_video)
			bot.send_message(message.chat.id, "Ya lo baje... esta enviandose")
			video = open('test.mp4', 'rb')
			bot.send_video(message.chat.id, video, timeout=999)
			video.close()
			os.remove("test.mp4")
			print("Borrado archivo test.mp4")
	else:
		bot.send_message(message.chat.id, "Ponte vio weon, el comando " + message.text + " no existe")

bot.polling()
