import sys				# Usado para los colores
import os				# Usado para el clear y para crear la carpeta Dump
import urllib				# Usado para descargar archivos
import requests				# Beautiful y requests son usados para crawlear la pagina
from bs4 import BeautifulSoup

# color cian \033[1;36m
# color rojo \033[1;31m
# color verde \033[1;32m

def banner():
	sys.stdout.write("\033[1;36m")
	os.system("clear")
	print "		        000000                    00000                                         0000000     000000000000"
	print "		      0000000000    00000000    000000000    00000000  000  00000000    000      00000    00000000"
	print "		    0000     0000  0000000000  000     000  00000000  000  0000000000  000        000   00000"
	print "		   0000       000  000    000  000    000   000       000  000   000  000         000  0000"
	print "		   0000       000  000    000   00    000   000       000  000   000  000         000 0000"
	print "		     0000      0  000000000         000    000       000  000   000  000          0000000"
	print "		 0      0000     00000000    0    000      000       000  000000000  000         000000"
	print "		000       0000   000       000      000   000       000  000000000  000          0000000"
	print "		000       0000  000       000       0000  000       000  000   000  000         000  00000"
	print "		0000    00000   000      000000   000000  00000000  000  000   000  0000000000  000   00000000        00000000"
	print "		 0000000000    000         00000000000     000000  000  000   000  0000000000  00000    000000000000000000"
	print "		   000000                     000000                                          0000000      0000000000"
	print
	print
	print
	sys.stdout.write("\033[32m")
	print "		Welcome to the Sp3cialK's Directory Tree Web Scraper. I hope it works well for you ;)"
	print
	print "										      Made by Sp3cialK. Feel free to modify it"
	print
	print
	print
	print

	
#Aqui pueden empezar los errores

def dump(url, carpetaDump):
	source_code = requests.get(url)

	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, "lxml")

	#Crea la carpeta que se le pasa de argumento si todavia no existe
	if (os.path.isdir("./" + carpetaDump) == False):
		os.mkdir(carpetaDump)
		print carpetaDump + " created"
		print

	for link in soup.findAll('a'):
		href = link.get('href')
		print href
		#si es una carpeta y la crawlea y la crea dentro de Dump
		if (("/" in href) and ((href is not "/") and (href is not "../") and (href is not "/../") and (href is not "/.."))):
			print "Going into " + href + " directory"
			print
			dump((url + href), (carpetaDump + "/" + href))

		#sino, es un archivo e intenta descargarlo
		else:		
			try:			
				print "Trying to download " + href				
				descargarArchivo = urllib.URLopener()
				descargarArchivo.retrieve((url + href), (carpetaDump + "/" + href))
				print
			except:
				print "Error, " + href + " not downloaded"
				print
									


def start():
	print "You need to type the page to dump like this: http://www.target.com/dir/to/dump/"
	url = raw_input("Type the webpage: ")
	carpetaDump = "Dump"	
	sys.stdout.write("\033[1;31m")
	
	dump(url, carpetaDump)

	print "The dump is finished. Press enter to go back to the menu..."
	char = sys.stdin.read(1)

#Y aqui terminarian los errores


def more():
	print "This tool is a dumper of files located in a web page. You can use it when you find a transversal directory vulnerability"
	print "The use of this tool is not illegal unless you do not have the permissions of a web owner to use it on his web"
	print	
	print "The tool makes you a folder called Dump, and in that folder downloads you the whole files in the directory you choose."
	print "For example, if you choose to dump https://www.example.com/files it will download you all the files and folders located in the"
	print "'files' folder."
	print "The useful thing of this tool is that earns you a lot of time and effort."
	print "This tool will not bypass you the admin privileges to access a folder."
	print
	print "If you want to learn hacking visit our forum, https://www.hackxcrack.net"
	print "You will not regret it :)"
	print
	print
	print "Press enter to go back to the menu..."
	char = sys.stdin.read(1)


diccionario = {
1:start,
2:more
}


while (True):
	banner()
	print "1. Start the dump"
	print "2. More about this tool"
	print "0. Exit"
	print
	opcion = int(input("Choose the option you want to use: "))
	os.system("clear")
	banner()
	if (opcion == 0):
		break
	elif (opcion != 1 and opcion != 2):
		print "That option does not exists. Press enter to continue..."
		char = sys.stdin.read(1)
	else:		
		diccionario[opcion]()
	os.system("clear")
os.system("clear")
