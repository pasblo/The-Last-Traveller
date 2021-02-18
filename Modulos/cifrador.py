def cifrartxt(texto_a_cifrar, codigo):

	texto_cifrado = ""
	for recorrer in range(len(texto_a_cifrar)):
		texto_cifrado = texto_cifrado +chr(ord(texto_a_cifrar[recorrer])+int(codigo))

	return texto_cifrado

def descifrartxt(texto_a_descifrar, codigo):

	texto_descifrado = ""
	for recorrer in range(len(texto_a_descifrar)):
		texto_descifrado = texto_descifrado +chr(ord(texto_a_descifrar[recorrer])-int(codigo))

	return texto_descifrado

def cifrar_contraseña(contraseña):

	contraseña_cifrada = ""
	codigo = contraseña[0]
	for recorrer in range(len(contraseña)):
		contraseña_cifrada = contraseña_cifrada +chr(ord(contraseña[recorrer])+int(codigo))

	return contraseña_cifrada

def descifrar_contraseña(contraseña, codigo):

	contraseña_descifrada = ""
	for recorrer in range(len(contraseña)):
		contraseña_descifrada = contraseña_descifrada + chr(ord(contraseña[recorrer])-int(codigo))

	return contraseña_descifrada