from unidecode import unidecode
def quitar_acentos(texto):
    return unidecode(texto).lower()
class GameBotProConsole:
    def __init__(self):
        self.opciones = {
            "genero": ["accion", "aventura", "estrategia", "simulacion", "rol", "deportes", "multijugador", "indie"],
            "plataforma": ["pc", "playstation", "xbox", "nintendo", "movil"],
            "dificultad": ["baja", "media", "alta", "indiferente"],
            "multijugador": ["si", "no", "indiferente"],
            "duracion": ["corta", "media", "larga", "indiferente"],
            "tematica": ["fantasia", "ciencia ficcion", "historico", "terror", "deporte", "indiferente"]
        }
        self.juegos = [
            {"nombre": "Doom Eternal", "genero": "accion", "plataforma": ["pc", "playstation", "xbox"], "dificultad": "alta", "multijugador": False, "duracion": "media", "tematica": ["ciencia ficcion"]},
            {"nombre": "The Legend of Zelda: Breath of the Wild", "genero": "aventura", "plataforma": ["nintendo switch"], "dificultad": "media", "multijugador": False, "duracion": "larga", "tematica": ["fantasia"]},
            {"nombre": "Valorant", "genero": "multijugador", "plataforma": ["pc"], "dificultad": "media", "multijugador": True, "duracion": "media", "tematica": ["ciencia ficcion"]},
            {"nombre": "Stardew Valley", "genero": "simulacion", "plataforma": ["pc", "movil"], "dificultad": "baja", "multijugador": True, "duracion": "larga", "tematica": ["fantasia"]},
            {"nombre": "Dark Souls", "genero": "rol", "plataforma": ["pc", "playstation", "xbox"], "dificultad": "alta", "multijugador": False, "duracion": "media", "tematica": ["fantasia"]},
            {"nombre": "Among Us", "genero": "multijugador", "plataforma": ["pc", "movil"], "dificultad": "baja", "multijugador": True, "duracion": "corta", "tematica": ["ciencia ficcion"]},
            ##juegos agregados depus para pribar
            {"nombre": "FIFA 24", "genero": "deportes", "plataforma": ["playstation", "xbox"], "dificultad": "media", "multijugador": True, "duracion": "media", "tematica": ["deporte"]},
            {"nombre": "Celeste", "genero": "indie", "plataforma": ["pc", "nintendo switch"], "dificultad": "alta", "multijugador": False, "duracion": "corta", "tematica": ["fantasía"]},
            {"nombre": "Sea of Thieves", "genero": "aventura", "plataforma": ["xbox", "pc"], "dificultad": "media", "multijugador": True, "duracion": "larga", "tematica": ["fantasía", "piratas"]},
            {"nombre": "Mario Kart 8 Deluxe", "genero": "deportes", "plataforma": ["nintendo switch"], "dificultad": "media", "multijugador": True, "duracion": "corta", "tematica": ["deporte", "fantasía"]},
            {"nombre": "Resident Evil Village", "genero": "aventura", "plataforma": ["pc", "playstation", "xbox"], "dificultad": "alta", "multijugador": False, "duracion": "media", "tematica": ["terror", "ciencia ficción"]},
            {"nombre": "Candy Crush Saga", "genero": "indie", "plataforma": ["móvil"], "dificultad": "baja", "multijugador": False, "duracion": "corta", "tematica": ["fantasía"]},
            {"nombre": "Football Manager 2024", "genero": "estrategia", "plataforma": ["pc"], "dificultad": "alta", "multijugador": False, "duracion": "larga", "tematica": ["deporte"]},
            {"nombre": "The Sims 4", "genero": "simulación", "plataforma": ["pc", "playstation", "xbox"], "dificultad": "baja", "multijugador": True, "duracion": "larga", "tematica": ["fantasía"]},
            {"nombre": "Cyberpunk 2077", "genero": "rol", "plataforma": ["pc", "playstation", "xbox"], "dificultad": "media", "multijugador": False, "duracion": "larga", "tematica": ["ciencia ficción"]},
            {"nombre": "Overcooked! 2", "genero": "multijugador", "plataforma": ["pc", "playstation", "xbox", "nintendo switch"], "dificultad": "media", "multijugador": True, "duracion": "corta", "tematica": ["fantasía"]},
            {"nombre": "Hollow Knight", "genero": "indie", "plataforma": ["pc", "nintendo switch", "playstation", "xbox"], "dificultad": "alta", "multijugador": False, "duracion": "media", "tematica": ["fantasía"]},
            {"nombre": "Papers, Please", "genero": "estrategia", "plataforma": ["pc"], "dificultad": "media", "multijugador": False, "duracion": "corta", "tematica": ["histórico"]},
            {"nombre": "Left 4 Dead 2", "genero": "acción", "plataforma": ["pc", "xbox"], "dificultad": "media", "multijugador": True, "duracion": "media", "tematica": ["terror", "ciencia ficción"]},
            {"nombre": "God of War Ragnarök", "genero": "acción", "plataforma": ["playstation"], "dificultad": "media", "multijugador": False, "duracion": "larga", "tematica": ["fantasía", "histórico"]},
            {"nombre": "Hades", "genero": "indie", "plataforma": ["pc", "nintendo switch"], "dificultad": "alta", "multijugador": False, "duracion": "media", "tematica": ["fantasía", "mitología"]},
            {"nombre": "Minecraft", "genero": "simulación", "plataforma": ["pc", "playstation", "xbox", "nintendo switch", "móvil"], "dificultad": "indiferente", "multijugador": True, "duracion": "larga", "tematica": ["fantasía"]},
            {"nombre": "The Witcher 3: Wild Hunt", "genero": "rol", "plataforma": ["pc", "playstation", "xbox", "nintendo switch"], "dificultad": "media", "multijugador": False, "duracion": "larga", "tematica": ["fantasía"]},
            {"nombre": "Fortnite", "genero": "multijugador", "plataforma": ["pc", "playstation", "xbox", "nintendo switch", "móvil"], "dificultad": "media", "multijugador": True, "duracion": "media", "tematica": ["ciencia ficción"]},
            {"nombre": "Animal Crossing: New Horizons", "genero": "simulación", "plataforma": ["nintendo switch"], "dificultad": "baja", "multijugador": True, "duracion": "larga", "tematica": ["fantasía"]},
            {"nombre": "Rainbow Six Siege", "genero": "acción", "plataforma": ["pc", "playstation", "xbox"], "dificultad": "alta", "multijugador": True, "duracion": "media", "tematica": ["terror", "estrategia"]},
            {"nombre": "Dead Cells", "genero": "indie", "plataforma": ["pc", "playstation", "xbox", "nintendo switch"], "dificultad": "alta", "multijugador": False, "duracion": "media", "tematica": ["fantasía"]},
            {"nombre": "Cuphead", "genero": "indie", "plataforma": ["pc", "xbox", "nintendo switch"], "dificultad": "alta", "multijugador": True, "duracion": "corta", "tematica": ["fantasía", "clásico"]},
            {"nombre": "Dead or Alive", "genero": "acción", "plataforma": ["pc", "playstation", "xbox"], "dificultad": "media", "multijugador": True, "duracion": "media", "tematica": ["deporte"]},
        ]
        self.preferencias = {k: None for k in self.opciones}
        self.preguntas = {
            "genero": ("¿Qué género(s) prefieres? (varios separados por coma)", True),
            "plataforma": ("¿En qué plataforma juegas?", False),
            "dificultad": ("¿Qué nivel de dificultad prefieres?", False),
            "multijugador": ("¿Prefieres juegos multijugador? (si/no/indiferente)", False),
            "duracion": ("¿Qué duración prefieres?", False),
            "tematica": ("¿Qué temática prefieres? (varios separados por coma)", True)
        }
    def pedir_respuesta(self, clave, texto, permitir_varios):
        opciones_norm = self.opciones[clave]
        while True:
            print(f"\n{texto}\nOpciones válidas: {', '.join(opciones_norm)}")
            resp = quitar_acentos(input("Tu respuesta (o 'salir' para terminar): ").strip())
            if resp == "salir":
                print("Saliendo del programa."); exit()
            respuestas = [r.strip() for r in resp.split(",")] if permitir_varios else [resp]
            if all(r in opciones_norm for r in respuestas):
                return respuestas if permitir_varios else resp
            print(f"Error: elige opciones válidas: {', '.join(opciones_norm)}")
    def recomendar_juego_avanzado(self, prefs, juegos):
        recomendaciones = []
        for juego in juegos:
            score, detalles = 0, []
            def coincide(c, jv):
                return c == "indiferente" or c == jv
            # Género
            gen_usr = prefs["genero"]
            if (isinstance(gen_usr, list) and juego["genero"] in gen_usr) or (gen_usr == juego["genero"]):
                score += 1; detalles.append(f"Género coincide ({juego['genero']})")
            # Plataforma
            if prefs["plataforma"] in juego["plataforma"]:
                score += 1; detalles.append(f"Plataforma coincide ({prefs['plataforma']})")
            # Dificultad
            if coincide(prefs["dificultad"], juego["dificultad"]):
                score += 1; detalles.append(f"Dificultad coincide ({juego['dificultad']})")
            # Multijugador
            multi_pref = prefs["multijugador"]
            multi_juego = juego["multijugador"]
            if multi_pref == "indiferente" or (multi_pref == "si") == multi_juego:
                score += 1; detalles.append(f"Multijugador coincide ({multi_pref})")
            # Duración
            if "duracion" in prefs and coincide(prefs["duracion"], juego.get("duracion", "indiferente")):
                score += 1; detalles.append(f"Duración coincide ({juego.get('duracion', 'desconocida')})")
            # Temtica
            tem_usr = prefs.get("tematica")
            tem_jue = juego.get("tematica", [])
            if tem_usr:
                if (isinstance(tem_usr, list) and any(t in tem_jue for t in tem_usr)) or (tem_usr in tem_jue):
                    score += 1; detalles.append("Temática coincide")
            if score >= 4:
                recomendaciones.append((score, juego["nombre"], detalles))
        return sorted(recomendaciones, key=lambda x: x[0], reverse=True) or None
    def iniciar(self):
        print("Bienvenido a GameBot Pro\n")
        while True:
            for clave, (texto, varios) in self.preguntas.items():
                self.preferencias[clave] = self.pedir_respuesta(clave, texto, varios)
            recs = self.recomendar_juego_avanzado(self.preferencias, self.juegos)
            print("\nResultados de tus preferencias:\n")
            if recs:
                print("Te recomiendo estos juegos (ordenados por coincidencia):\n")
                for score, nombre, detalles in recs:
                    print(f"{nombre} (Coincidencias: {score})\n  Detalles: {', '.join(detalles)}\n")
            else:
                print("No encontré juegos que coincidan. Prueba con Minecraft, ¡a todos les gusta! =)\n")
            while True:
                opcion = quitar_acentos(input("¿Deseas continuar o salir? (continuar/salir): ").strip())
                if opcion == "salir":
                    print("Gracias por usar GameBot Pro. ¡Hasta luego!"); exit()
                elif opcion == "continuar":
                    self.preferencias = {k: None for k in self.opciones}
                    print("\nReiniciando...\n")
                    break
                else:
                    print("Por favor escribe 'continuar' o 'salir'.")
if __name__ == "__main__":
    GameBotProConsole().iniciar()
