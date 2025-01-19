import urllib
import urllib.request

try:
	site = urllib.request.urlopen('https://unshorten.me/')
except Exception as sla:
	print('\033[1;31;44mO site não está acessível no momento. Erro: ', sla)
else:
	print('\033[1;32;44mO site está acessível')
	print(site.read())