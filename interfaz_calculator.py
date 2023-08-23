import PySimpleGUI as sg
import math



sg.theme('Dark Green 2') # estilo de la ventana

# Diseño de la interfaz gráfica
layout = [
    [sg.Text("Distancia (km):"), sg.InputText(key='distancia', size=(10, 1))],
    [sg.Text("Frecuencia (GHz):"), sg.Combo(['2.4', '5.8'], default_value='2.4', key='frecuencia')],
    [sg.Button("Calcular"),sg.Button("Resetear")],
    [sg.Text("", size=(40, 1), key='resultado', justification='center')],
    [sg.Text("", size=(40, 3), key='explicacion', justification='center')],
    [sg.Text("Created by: Joaquin Peralta", size=(40, 3), key='explicacion', justification='center')],
    
]

# Crear la ventana
window = sg.Window("Calculadora de Zona de Fresnel", layout, element_justification='center')

# Bucle de eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Salir":
        break
    elif event == "Calcular":
        try:
            distancia_km = float(values['distancia'])
            frecuencia_ghz = float(values['frecuencia'])
            
            zona_fresnel = 8.656 * math.sqrt(distancia_km / frecuencia_ghz) # Formula 
            window['resultado'].update(f"Zona de Fresnel: {zona_fresnel:.2f} metros")
            
            if zona_fresnel < 1:    # si la zona de Fresnel es menor a 1, significa que está prácticamente obstruida.
                explicacion = "Es posible que la zona de fresnel está obstruida. Posible interferencia."          
            elif zona_fresnel >= 1 and zona_fresnel < 2: # Si la zona de Fresnel está entre 1 y 2, se recomienda una alineación precisa entre los puntos de transmisión y recepción para garantizar la calidad de la señal. 
                explicacion = "Se recomienda una alineación precisa para evitar interferencias."
            else: # Si la zona de Fresnel es mayor a 2, esto indica que la zona está mayormente despejada lo cual la señal podría ser más confiable en términos de interferencias.
                explicacion = "La Zona de Fresnel está mayormente despejada. Interferencias mínimas."
                
            window['explicacion'].update(explicacion)
        except ValueError:
            window['resultado'].update("Por favor, ingresa valores numéricos válidos.")
        
    elif event == "Resetear":
        window['distancia'].update('')
        window['frecuencia'].update('')
        window['resultado'].update('')
        window['explicacion'].update('')



# Cerrar la ventana al salir
window.close()
