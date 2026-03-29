class LibreriaGramaticaExacta:
    # PARAMETRO 1:
    # Lenguaje a interpretar -> Reglas gramaticales   
    @staticmethod
    def lenguaje_a_interpretar(cadena):
        # Este lenguaje simple acepta:
        # palabras clave: resumen, buscar, relevante, audio
        # conectores: y, o
        # ejemplos:
        # resumen
        # buscar python
        # buscar resultado y resumen
        # relevante
        # audio
        partes = cadena.lower().split()

        if len(partes) == 1:
            if partes[0] in ["resumen", "relevante", "audio"]:
                return True

        if len(partes) == 2:
            if partes[0] == "buscar":
                return True

        if len(partes) == 4:
            if partes[0] == "buscar" and partes[2] in ["y", "o"]:
                return True

        return False

    # =========================================
    # PARAMETRO 2:
    # Realizar consultas con el lenguaje
    # determinado a un motor de I.A.
    # =========================================
    @staticmethod
    def realizar_consulta_con_lenguaje_determinado_a_un_motor_de_ia(consulta, contenido):
        partes = consulta.lower().split()

        # Motor de IA simple simulado
        # Aquí no se conecta a internet ni a una IA real,
        # pero responde como si analizara el texto.
        if consulta.lower() == "resumen":
            return LibreriaGramaticaExacta.generar_resumen(contenido)

        elif consulta.lower() == "relevante":
            relevantes = LibreriaGramaticaExacta.interpretar_los_resultados_extrayendo_partes_relevantes_de_la_misma(contenido)
            if len(relevantes) == 0:
                return "No se encontraron partes relevantes."
            return "\n".join(relevantes)

        elif consulta.lower() == "audio":
            return "Resultado listo para reproducirse en audio."

        elif len(partes) >= 2 and partes[0] == "buscar":
            termino1 = partes[1]
            coincidencias1 = LibreriaGramaticaExacta.buscar_termino(termino1, contenido)

            if len(partes) == 2:
                if len(coincidencias1) == 0:
                    return "No se encontraron coincidencias para: " + termino1
                return "Coincidencias encontradas para '" + termino1 + "':\n" + "\n".join(coincidencias1)

            elif len(partes) == 4:
                conector = partes[2]
                termino2 = partes[3]
                coincidencias2 = LibreriaGramaticaExacta.buscar_termino(termino2, contenido)

                if conector == "y":
                    resultado = []
                    for linea in coincidencias1:
                        if linea in coincidencias2:
                            resultado.append(linea)

                    if len(resultado) == 0:
                        return "No se encontraron líneas que contengan ambos términos."
                    return "Coincidencias con ambos términos:\n" + "\n".join(resultado)

                elif conector == "o":
                    resultado = []
                    for linea in coincidencias1:
                        if linea not in resultado:
                            resultado.append(linea)
                    for linea in coincidencias2:
                        if linea not in resultado:
                            resultado.append(linea)

                    if len(resultado) == 0:
                        return "No se encontraron coincidencias."
                    return "Coincidencias con alguno de los términos:\n" + "\n".join(resultado)

        return "Consulta no válida para el lenguaje determinado."

    # =========================================
    # PARAMETRO 3:
    # Interpretar los resultados extrayendo
    # "partes relevantes" de la misma
    # =========================================
    @staticmethod
    def interpretar_los_resultados_extrayendo_partes_relevantes_de_la_misma(contenido):
        lineas = contenido.split("\n")
        relevantes = []

        for linea in lineas:
            texto = linea.lower()
            if ("importante" in texto or
                "resultado" in texto or
                "resumen" in texto or
                "conclusion" in texto or
                "regla" in texto or
                "python" in texto or
                "xml" in texto or
                "expresion" in texto):
                relevantes.append(linea)

        return relevantes

    # =========================================
    # PARAMETRO 4:
    # Los resultados pueden ser reproducidos
    # en audio
    # =========================================
    @staticmethod
    def los_resultados_pueden_ser_reproducidos_en_audio(texto_resultado):
        # Como esta versión no usa librerías externas,
        # aquí generamos un archivo de texto que sirve
        # como guion para audio o lectura.
        archivo = open("resultado_audio.txt", "w", encoding="utf-8")
        archivo.write("AUDIO DEL RESULTADO\n")
        archivo.write(texto_resultado)
        archivo.close()
        return "Se generó el archivo resultado_audio.txt con el texto para audio."

    # =========================================
    # FUNCIONES DE APOYO
    # =========================================
    @staticmethod
    def leer_archivo(ruta):
        archivo = open(ruta, "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()

        if contenido.strip() == "":
            raise Exception("El archivo está vacío.")

        return contenido

    @staticmethod
    def generar_resumen(contenido):
        lineas = contenido.split("\n")
        cantidad_lineas = len(lineas)
        palabras = len(contenido.split())

        return (
            "Resumen del contenido:\n"
            + "Líneas: " + str(cantidad_lineas) + "\n"
            + "Palabras: " + str(palabras) + "\n"
            + "Primeras líneas:\n"
            + "\n".join(lineas[:3])
        )

    @staticmethod
    def buscar_termino(termino, contenido):
        lineas = contenido.split("\n")
        encontradas = []

        for linea in lineas:
            if termino.lower() in linea.lower():
                encontradas.append(linea)

        return encontradas


def main():
    try:
        print("=== LIBRERIA USANDO TODOS LOS PARAMETROS EXACTOS ===")
        ruta = input("Ingrese la ruta del archivo .txt: ")
        contenido = LibreriaGramaticaExacta.leer_archivo(ruta)

        print("\nLenguaje permitido:")
        print("- resumen")
        print("- relevante")
        print("- audio")
        print("- buscar palabra")
        print("- buscar palabra1 y palabra2")
        print("- buscar palabra1 o palabra2")

        consulta = input("\nIngrese la consulta en el lenguaje determinado: ")

        # PARAMETRO 1: validar lenguaje a interpretar
        if not LibreriaGramaticaExacta.lenguaje_a_interpretar(consulta):
            print("La consulta no cumple las reglas gramaticales del lenguaje a interpretar.")
            return

        print("\nLa consulta cumple las reglas gramaticales.")

        # PARAMETRO 2: realizar consulta al motor de IA
        resultado = LibreriaGramaticaExacta.realizar_consulta_con_lenguaje_determinado_a_un_motor_de_ia(consulta, contenido)

        print("\n=== RESULTADO DE LA CONSULTA ===")
        print(resultado)

        # PARAMETRO 3: interpretar resultados y extraer partes relevantes
        partes_relevantes = LibreriaGramaticaExacta.interpretar_los_resultados_extrayendo_partes_relevantes_de_la_misma(contenido)

        print("\n=== PARTES RELEVANTES ===")
        if len(partes_relevantes) == 0:
            print("No se encontraron partes relevantes.")
        else:
            for parte in partes_relevantes:
                print(parte)

        # PARAMETRO 4: reproducir resultado en audio
        opcion_audio = input("\n¿Desea generar el resultado para audio? (si/no): ").lower()
        if opcion_audio == "si":
            mensaje_audio = LibreriaGramaticaExacta.los_resultados_pueden_ser_reproducidos_en_audio(resultado)
            print(mensaje_audio)

    except Exception as e:
        print("Error:", e)


main()
