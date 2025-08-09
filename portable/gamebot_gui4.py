import tkinter as tk
from tkinter import scrolledtext
from unidecode import unidecode

class GameBotProChat(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GameBot Pro - Chat David Díaz")
        self.geometry("600x400")
        
        # Categorías a preguntar
        self.categorias = {
            "genero": ["accion", "aventura", "estrategia", "simulacion", "rol", "deportes", "multijugador", "indie"],
            "plataforma": ["pc", "playstation", "xbox", "nintendo switch", "movil"],
            "dificultad": ["baja", "media", "alta", "indiferente"],
            "multijugador": ["si", "no", "indiferente"],
            "duracion": ["corta", "media", "larga", "indiferente"],
            "tematica": ["fantasia", "ciencia ficcion", "historico", "terror", "deporte", "indiferente"]
        }

        self.respuestas = {clave: None for clave in self.categorias}

        # Base de datos de juegos
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

        self.pasos = [
            ("genero", True),
            ("plataforma", False),
            ("dificultad", False),
            ("multijugador", False),
            ("duracion", False),
            ("tematica", True),
        ]
        self.paso_actual = 0
        self.esperando_confirmacion = False
        
        self.chat_area = scrolledtext.ScrolledText(self, state='disabled', wrap=tk.WORD, font=("Arial", 11))
        self.chat_area.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        
        self.entry_respuesta = tk.Entry(self, font=("Arial", 12))
        self.entry_respuesta.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        self.entry_respuesta.bind("<Return>", self.procesar_respuesta)
        
        self.boton_enviar = tk.Button(self, text="Enviar", command=self.procesar_respuesta)
        self.boton_enviar.grid(row=1, column=1, padx=10, pady=5)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.enviar_mensaje("GameBot Pro: ¡Hola! Te ayudaré a encontrar un juego según tus gustos. Escribe 'salir' si quieres terminar.\n")
        self.preguntar_siguiente()

    def enviar_mensaje(self, texto):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, texto + "\n")
        self.chat_area.see(tk.END)
        self.chat_area.configure(state='disabled')

    def preguntar_siguiente(self):
        if self.paso_actual >= len(self.pasos):
            self.mostrar_recomendaciones()
            return
        clave, permite_varios = self.pasos[self.paso_actual]
        opciones = self.categorias[clave]
        mensaje = f"¿Qué {clave} prefieres?"
        if permite_varios:
            mensaje += " (puedes poner varias separadas por coma)"
        mensaje += f"\nOpciones: {', '.join(opciones)}"
        self.enviar_mensaje(f"GameBot Pro: {mensaje}")

    def procesar_respuesta(self, event=None):
        entrada = self.entry_respuesta.get().strip()
        self.entry_respuesta.delete(0, tk.END)

        if not entrada:
            return
        self.enviar_mensaje(f"Tú: {entrada}")

        entrada_norm = unidecode(entrada.lower())

        if entrada_norm == "salir":
            self.enviar_mensaje("GameBot Pro: ¡Hasta luego!")
            self.entry_respuesta.config(state="disabled")
            self.boton_enviar.config(state="disabled")
            return

        if self.esperando_confirmacion:
            if entrada_norm == "si":
                self.respuestas = {k: None for k in self.respuestas}
                self.paso_actual = 0
                self.esperando_confirmacion = False
                self.preguntar_siguiente()
            else:
                self.enviar_mensaje("GameBot Pro: ¡Gracias por usar GameBot Pro!")
                self.entry_respuesta.config(state="disabled")
                self.boton_enviar.config(state="disabled")
            return

        clave, permite_varios = self.pasos[self.paso_actual]
        opciones_norm = [unidecode(o.lower()) for o in self.categorias[clave]]

        if permite_varios:
            seleccion = [r.strip() for r in entrada_norm.split(",")]
            validas = [self.categorias[clave][opciones_norm.index(r)] for r in seleccion if r in opciones_norm]
            if not validas:
                self.enviar_mensaje(f"GameBot Pro: Escoge opciones válidas: {', '.join(self.categorias[clave])}")
                return
            self.respuestas[clave] = validas
        else:
            if entrada_norm not in opciones_norm:
                self.enviar_mensaje(f"GameBot Pro: Escoge una opción válida: {', '.join(self.categorias[clave])}")
                return
            self.respuestas[clave] = self.categorias[clave][opciones_norm.index(entrada_norm)]

        self.paso_actual += 1
        self.preguntar_siguiente()

    def mostrar_recomendaciones(self):
        resultados = []
        for juego in self.juegos:
            coincidencias = 0
            for clave, valor in self.respuestas.items():
                if not valor or valor == "indiferente":
                    continue

                valor_juego = juego[clave]

                if isinstance(valor, list):
                    if isinstance(valor_juego, list):
                        if any(v == elem for v in valor for elem in valor_juego):
                            coincidencias += 1
                    else:
                        if any(v == valor_juego for v in valor):
                            coincidencias += 1
                else:
                    if isinstance(valor_juego, list):
                        if valor in valor_juego:
                            coincidencias += 1
                    elif isinstance(valor_juego, bool):
                        val_bool = True if valor == "si" else False if valor == "no" else None
                        if val_bool is not None and valor_juego == val_bool:
                            coincidencias += 1
                    else:
                        if valor == valor_juego:
                            coincidencias += 1

            if coincidencias >= 3:
                resultados.append(juego["nombre"])

        if resultados:
            self.enviar_mensaje("GameBot Pro: Podrías probar estos juegos:")
            for r in resultados:
                self.enviar_mensaje(f"- {r}")
        else:
            self.enviar_mensaje("GameBot Pro: No encontré coincidencias.")

        self.enviar_mensaje("\n¿Quieres otra recomendación? (si/salir)")
        self.esperando_confirmacion = True


if __name__ == "__main__":
    app = GameBotProChat()
    app.mainloop()
