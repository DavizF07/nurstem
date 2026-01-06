import tkinter as tk
from tkinter import ttk

# --- Configuración de Colores ---
COLOR_FONDO_EXTERNO = "#FDF6B0"  # Amarillo muy claro
COLOR_TARJETA = "#F8DE66"        # Amarillo fuerte de la tarjeta
COLOR_HEADER = "#FBE36C"         # Amarillo de la barra superior
COLOR_TEXTO = "#FFFFFF"          # Blanco para etiquetas
COLOR_BOTON_ROJO = "#FF4D4D"     # Rojo para cancelar
COLOR_BOTON_VERDE = "#7ED957"    # Verde para aceptar

# --- Definición de Funciones (Marcadores de posición) ---
def cancelar_registro():
    """Lógica para cerrar la ventana o limpiar el formulario"""
    print("Acción: Cancelar")

def aceptar_registro():
    """Lógica para validar y guardar los datos del enfermero"""
    print("Acción: Aceptar y Guardar")

# --- Ventana Principal ---
root = tk.Tk()
root.title("Crear Enfermero")
root.geometry("900x550")
root.configure(bg=COLOR_FONDO_EXTERNO)

# --- Barra Superior (Header) ---
header = tk.Frame(root, bg=COLOR_HEADER, height=60)
header.pack(fill="x", side="top")

# Icono de menú (Simulado con texto/label)
lbl_menu = tk.Label(header, text="≡", bg=COLOR_HEADER, fg="white", font=("Arial", 24))
lbl_menu.pack(side="left", padx=20)

# Icono de usuario (Simulado con texto/label)
lbl_user = tk.Label(header, text="👤", bg=COLOR_HEADER, fg="white", font=("Arial", 24))
lbl_user.pack(side="right", padx=20)

# --- Tarjeta Central (Formulario) ---
# Usamos un Frame para contener todo el formulario
main_card = tk.Frame(root, bg=COLOR_TARJETA, bd=0, highlightthickness=0)
main_card.place(relx=0.5, rely=0.55, anchor="center", width=700, height=450)

# Título de la tarjeta
lbl_titulo = tk.Label(main_card, text="Crear enfermero", bg=COLOR_TARJETA, 
                      fg="white", font=("Arial", 36, "bold"))
lbl_titulo.pack(pady=(10, 5))

# Línea divisoria blanca
linea = tk.Frame(main_card, height=2, bg="white")
linea.pack(fill="x", padx=40, pady=5)

# --- Contenedor de Contenido (Grid) ---
content_frame = tk.Frame(main_card, bg=COLOR_TARJETA)
content_frame.pack(expand=True, fill="both", padx=40, pady=10)

# --- Lado Izquierdo: Imagen e ID ---
left_frame = tk.Frame(content_frame, bg=COLOR_TARJETA)
left_frame.grid(row=0, column=0, padx=20)

# Cuadro de imagen
img_placeholder = tk.Label(left_frame, text="🖼️", bg="white", width=20, height=10)
img_placeholder.pack()

# Entry para ID (Inamovible)
id_entry = tk.Entry(left_frame, font=("Arial", 12), justify="center")
id_entry.insert(0, "ID inamovible generado")
id_entry.config(state="readonly")
id_entry.pack(pady=20)

# --- Lado Derecho: Campos de Texto ---
right_frame = tk.Frame(content_frame, bg=COLOR_TARJETA)
right_frame.grid(row=0, column=1, sticky="nsew")

campos = [
    ("Nombre:", "Avril Paola"),
    ("Apellido:", "Mejía Avianeda"),
    ("CURP:", "MEAAxxxxxxMDFxxxxx"),
    ("RFC:", "MEAAxxxxxxxxx"),
    ("Cel:", "55 xxxx xxxx")
]

entries = {} # Diccionario para acceder a los datos después

for i, (label_text, placeholder) in enumerate(campos):
    tk.Label(right_frame, text=label_text, bg=COLOR_TARJETA, fg="white", 
             font=("Arial", 14, "bold")).grid(row=i, column=0, sticky="e", pady=5, padx=5)
    
    ent = tk.Entry(right_frame, font=("Arial", 12), width=30)
    ent.insert(0, placeholder)
    ent.grid(row=i, column=1, pady=5, padx=5)
    entries[label_text] = ent

# Campo Especialidad (Combobox)
tk.Label(right_frame, text="Especialidad:", bg=COLOR_TARJETA, fg="white", 
         font=("Arial", 14, "bold")).grid(row=5, column=0, sticky="e", pady=5, padx=5)

combo_especialidad = ttk.Combobox(right_frame, values=["General", "Pediatría", "UCI"], font=("Arial", 12))
combo_especialidad.grid(row=5, column=1, pady=5, padx=5, sticky="w")

# --- Botones Inferiores ---
btn_frame = tk.Frame(main_card, bg=COLOR_TARJETA)
btn_frame.pack(side="bottom", fill="x", pady=20, padx=40)

btn_cancelar = tk.Button(btn_frame, text="X Cancelar", bg=COLOR_BOTON_ROJO, fg="white",
                         font=("Arial", 12, "bold"), borderwidth=0, padx=20, 
                         command=cancelar_registro)
btn_cancelar.pack(side="left")

btn_aceptar = tk.Button(btn_frame, text="✔ Aceptar", bg=COLOR_BOTON_VERDE, fg="white",
                        font=("Arial", 12, "bold"), borderwidth=0, padx=20,
                        command=aceptar_registro)
btn_aceptar.pack(side="right")

root.mainloop()