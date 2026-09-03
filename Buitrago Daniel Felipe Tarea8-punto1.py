#Daniel Felipe Buitrago
#Punto3
def main():
    inscritos = [0 for i in range(4)]
    lista = []
    cupos = [0 for i in range(4)]
    selec = [0 for i in range(4)]
    respuesta = "s"

    print("\nBienvenido")
    while respuesta == "s":
        print("\nRegistrese")
        nombre = input("\tNombre: ")
        codigo = input("\tCódigo: ")
        correo = input("\tCorreo: ")

        print("\n\tLabor 1 \t Bienvenida")
        print("\tLabor 2 \t Registro")
        print("\tLabor 3 \t Refrigerios")
        print("\tLabor 4 \t Informacion")
        opcion = int(input("\tIngrese la labor (1--2--3--4): "))

        labor = opcion - 1

        estudiante = [nombre, codigo, correo, labor]
        lista.append(estudiante)
        inscritos[labor] = inscritos[labor] + 1
        respuesta = input("\n¿Desea registrar otro estudiante? (s/n): ")

    print("\nNumero de inscritos\n")
    print("\tBienvenida: ", inscritos[0])
    print("\tRegistro: ", inscritos[1])
    print("\tRefrigerios: ", inscritos[2])
    print("\tInformacion: ", inscritos[3])

    print("\nCupos Para Contratar\n")
    cupos[0] = int(input("\tBienvenida: "))
    cupos[1] = int(input("\tRegistro: "))
    cupos[2] = int(input("\tRefrigerios: "))
    cupos[3] = int(input("\tInformacion: "))

    labores = ["Bienvenida", "Registro", "Refrigerios", "Informacion"]

    print("\nElegidos\n")
    for j in range(4):
        print("\t" + labores[j] + ":")
        for i in range(len(lista)):
            labor = lista[i][3]
            if labor == j and selec[labor] < cupos[labor]:
                print("\t", lista[i][0], "\t", lista[i][1], "\t", lista[i][2])
                selec[labor] = selec[labor] + 1
        print()
    print("Gracias, fin del programa")

main()
