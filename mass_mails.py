#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, traceback

sys.path.insert(0, '../')
import re
import smtplib
import time

# Добавляем подклассы - MIME-типов
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:

	fileopen = open('mass_mail.txt', 'r')
	for line in fileopen:

		From = "info@nstopt.ru"
		match = re.search(r'[\w\.-]+@[\w\.-]+', line)
		if match is None:
			email = str(None)
			print(email)
		elif match:
			To = match.group(0)

			msg = MIMEMultipart()
			msg['From']    = From
			msg['To']      = To
			msg['Subject'] = 'Время дарить игрушки!'

			handle = open("mails.html", "r")
			html = handle.read()
			handle.close()

			msg.attach(MIMEText(html, 'html', 'utf-8'))
			server = smtplib.SMTP('localhost', 25)
			server.set_debuglevel(False)                         # Режим отладки
			server.starttls()
			# server.login(From, Pass)                         # Если используется авторизация
			server.send_message(msg)
			server.quit()
			print("Сообщение отправлено: " + str(To))
			# time.sleep(5)

except smtplib.SMTPRecipientsRefused as e:
	print(e)

except smtplib.SMTPException as e:
	print(e)

except smtplib.SMTPServerDisconnected as e:
	print(e)

except KeyboardInterrupt:
	print("Остановка программы")

except UnicodeEncodeError:
	print("Проверьте email, возможны русские символы")

except:
	print('-' * 50)
	print("Прочие исключения")
	traceback.print_exc(limit=2, file=sys.stdout)
	print('-' * 50)