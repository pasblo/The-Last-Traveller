import webbrowser

def abrirpaginaweb(pagina, dominio):

	webbrowser.open_new_tab("http://www." + pagina + dominio)

def abrirbuscador(buscador, elemento_buscado, dominio_pagina = ".com", dominio_pais = "es"):

	if buscador == "yahoo":
			webbrowser.open_new_tab("https://" + dominio_pais + ".search."+ buscador + dominio_pagina + "/yhs/search?p=" + elemento_buscado)

	elif buscador == "google":
		webbrowser.open_new_tab("https://www." + buscador + dominio_pagina + "/?gws_rd=ssl#q=" + elemento_buscado)

	elif buscador == "bing":
		webbrowser.open_new_tab("www" + buscador + dominio_pagina + "/search?q=" + elemento_buscado)

	elif buscador == "youtube":
		webbrowser.open_new_tab("https://www." + buscador + dominio_pagina + "/results?search_query=" + elemento_buscado)

	else:
		print("Ese buscador no esta predefinido porfavor escriba otro")

def buscarcualquiercosa(elemento_a_buscar):

	webbrowser.open_new_tab(elemento_a_buscar)