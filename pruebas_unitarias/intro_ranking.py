import requests
# Debe tener instalado requests en su computadora
def intro_ranking(tecla, presionar, request_code):
    posturl="http://runinkarun.herokuapp.com/score/api"
    intro = True
    nombre = []
    score = []
    response = requests.get(posturl)
    print(response)
    if response.status_code == 200:
        data = response.json()
        for i in range(1):
            nombre.append(data[i]['playerName'])
            score.append(data[i]['acumScore'])
        while intro:
            for event in range(5):
                if tecla == "q":
                    return "salir del juego"
                if presionar == "si":
                    if tecla == "c":
                        intro = False
                        return "volver al menú"
            # screen.blit(bg_intro, (0, 0))
            # message_to_screen("TOP 10", ORANGE, -160, "mediano")
            # message_to_screen("Jugador    Puntaje", BLACK, -60, "pequena")
            print("TOP 10")
            print("Jugador     Puntaje")
            for i in range(1):
                #message_to_screen(nombre[i] + " : " + str(score[i]), BLACK, -20*-(i+1), "pequena")
                print(nombre[i] + " : " + str(score[i]))
            intro = False
            return "se pinto score en pantalla"
