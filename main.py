from libreria_gramatica import LibreriaGramaticaExacta

def main():
    try:
        print("=== PROGRAMA PRINCIPAL USANDO LA LIBRERÍA ===")
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

        if not LibreriaGramaticaExacta.lenguaje_a_interpretar(consulta):
            print("La consulta no cumple las reglas gramaticales del lenguaje a interpretar.")
            return

        print("\nLa consulta cumple las reglas gramaticales.")

        resultado = LibreriaGramaticaExacta.realizar_consulta_con_lenguaje_determinado_a_un_motor_de_ia(consulta, contenido)
        print("\n=== RESULTADO DE LA CONSULTA ===")
        print(resultado)

        partes_relevantes = LibreriaGramaticaExacta.interpretar_los_resultados_extrayendo_partes_relevantes_de_la_misma(contenido)
        print("\n=== PARTES RELEVANTES ===")
        print("\n".join(partes_relevantes) if partes_relevantes else "No se encontraron partes relevantes.")

        opcion_audio = input("\n¿Desea generar el resultado en audio TTS? (si/no): ").lower()
        if opcion_audio == "si":
            mensaje_audio = LibreriaGramaticaExacta.los_resultados_pueden_ser_reproducidos_en_audio(resultado)
            print(mensaje_audio)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
