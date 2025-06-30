def registar_jugador(partidos, jugadores):
    print("registrar un jugador")
    nombre = input ("nombre del jugador").strip()

    if nombre in jugadores:
        print("error, el jugador ingresado ya esta registrado")
        return partidos
    print("Seleccione el partido")
    PRINT("1. ESTRELLAS DEL NORTE (maximo 50 jugadores)")
    print("2. ingrs el norte (maximo 60 jugadores)") 
    opcion = input ("seleccione el partido").strip()
    if opcion not in ('1','2'):
        print("opcion no valida")
        return partidos
    


    if opcion =='1':
        jugadores [nombre]+= nombre
        partidos ['f1']-= 1
    
    
    def main():
        partidos= { 'f1': 50, 'f2': 60}
        jugadores = {}
    print('Ojala no volver a escucharr ese nombre')
