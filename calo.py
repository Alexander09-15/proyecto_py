def calcular_macros():
    s = input("¿Eres hombre o mujer?: ")
    peso = int(input("Dime tu peso (kg): "))
    altura = int(input("Dime tu altura (cm): "))
    edad = int(input("Dime tu edad: "))
    actividad = input("¿Cuánta actividad haces (nada, ligero, moderado, intenso, muy intenso)?: ")
    distribuir = input("¿Qué objetivo buscas (ganancia muscular, pérdida de grasa)?: ")

    def hombre():
        man = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
        if actividad == "nada":
            return man * 1.2
        elif actividad == "ligero":
            return man * 1.375
        elif actividad == "moderado":
            return man * 1.55
        elif actividad == "intenso":
            return man * 1.725
        elif actividad == "muy intenso":
            return man * 1.9

    def mujer():
        woman = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
        if actividad == "nada":
            return woman * 1.2
        elif actividad == "ligero":
            return woman * 1.375
        elif actividad == "moderado":
            return woman * 1.55
        elif actividad == "intenso":
            return woman * 1.725
        elif actividad == "muy intenso":
            return woman * 1.9

    if distribuir == "ganancia muscular":
        proteinas = 25
        grasas = 20
        carbo = 45
    elif distribuir == "pérdida de grasa":
        proteinas = 30
        grasas = 25
        carbo = 25   

    if s == "hombre":
        resultado = hombre()
    elif s == "mujer":
        resultado = mujer()
    else:
        resultado = "No ingresaste una opción válida"

    calorias_proteinas = (proteinas / 100) * resultado
    calorias_grasas = (grasas / 100) * resultado
    calorias_carbo = (carbo / 100) * resultado


    gramos_proteinas = calorias_proteinas / 4
    gramos_grasas = calorias_grasas / 9
    gramos_carbo = calorias_carbo / 4

    print(f"Tu gasto calórico estimado es: {int(resultado)} calorías.")
    print(f"Debes consumir aproximadamente {int(gramos_proteinas)}g de proteínas.")
    print(f"Debes consumir aproximadamente {int(gramos_grasas)}g de grasas.")
    print(f"Debes consumir aproximadamente {int(gramos_carbo)}g de carbohidratos.")


