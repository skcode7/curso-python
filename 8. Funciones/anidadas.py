def comenzar_playlist(lista):
    def reproducir():
        for track in lista:
            print(track)
    
    reproducir()    #invoca sub-funcion

lista = ["track 1", "track 2", "track 3", "track 4"]
comenzar_playlist(lista)
