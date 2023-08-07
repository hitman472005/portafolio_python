import smtplib

print("enviando")


mensajexd= "hola bro como estas"

conexion = smtplib.SMTP('smtp.gmail.com', 587)
conexion.ehlo()
conexion.starttls()

conexion.login('angelstevengonzalezf@gmail.com','angelsteven2806')

conexion.sendmail('angelstevengonzalezf@gmail.com','angelstevengonzalezf@gmail.com', msg = mensajexd )

conexion.quit()

