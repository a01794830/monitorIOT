import streamlit as st
import logging

logger = logging.getLogger(__name__)

def app():
    logger.info("Entrando a la página Preguntas Ejemplo")
    st.title("Preguntas de Ejemplo - IoT Monitor")

    ejemplo_pregs = [
        "¿Cuál es la latitud del dispositivo 6cfc7a7a?",
        "¿Cuál es la longitud del dispositivo 6cfc7a7a?",
        "¿Cuál es el nivel de batería del dispositivo 58fc7458?",
        "¿Dónde se encuentra en este momento la persona con ID a4be2b7f en latitud?",
        "¿Dónde se encuentra en este momento la persona con ID a4be2b7f en longitud?",
        "¿Qué dispositivos tienen batería menor que 20%?",
        "¿Qué dispositivos tienen señal menor que -90 dBm?",
        "¿Qué usuarios tienen un dispositivo con tamper_detected=TRUE?",
        "¿Qué dispositivos han violado restricciones?",
        "¿Cuál es el estado del dispositivo 12ab34cd?",
        "¿Cuáles son las coordenadas de todos los dispositivos de la persona con ID ffff1234?",
        "¿Cuántos dispositivos están inactivos (status=0)?",
        "¿Hay dispositivos con batería muy baja?",
        "Muestra la última ubicación de user_id=abc123",
        "¿Quién tiene el nivel de batería más alto?",
        "¿Existen dispositivos con tamper_detected=TRUE y batería menor de 10%?",
        "¿Qué dispositivos se encuentran fuera de su zona permitida?",
        "¿Cuántos dispositivos han reportado restricción violada?",
        "¿Cuál es el promedio de señal en todos los dispositivos?",
        "¿Qué usuario tiene la señal más débil?",
        "¿Cuántos dispositivos en total están activos (status=1)?",
        "¿Cuáles son las coordenadas exactas del dispositivo ID 9999abcd?",
        "¿Qué nivel de batería tienen los dispositivos con tamper_detected=FALSE?",
        "¿Cuál es el usuario asociado al dispositivo con ID 5db3e12f?",
        "¿Se encuentra algún dispositivo con latitud mayor a 45?",
        "¿Qué dispositivo está más cerca del ecuador (latitud=0)?",
        "¿Cuáles dispositivos reportaron su última actualización el día 2025-01-25?",
        "¿Qué usuario sale con frecuencia de su zona restringida?",
        "¿Cómo saber la ubicación en tiempo real de un dispositivo?",
        "¿Cuál fue la última vez que se detectó tamper en el dispositivo 74fdc9b1?",
        "¿Cuántos dispositivos hay con señal por debajo de -100 dBm?",
        "¿Hay algún dispositivo con restricción_violation=TRUE en la ciudad X?",
        "Muestra todas las coordenadas de los dispositivos con batería < 15%.",
        "¿Qué dispositivos no han reportado manipulación (tamper_detected=FALSE)?",
        "¿Cuál es la persona con el mayor número de dispositivos activos?",
        "¿Podrías listar todos los dispositivos y sus estados?",
        "¿Algún dispositivo en la zona lat=30..31, lon=-95..-94?",
        "¿En qué fecha se actualizó por última vez el dispositivo 6cfc7a7a?",
        "¿Cuántos dispositivos tienen status=2?",
        "¿Hay algún dispositivo sin señal (signal_strength=Null o -999)?",
        "¿Existen usuarios con más de un dispositivo que reporta tamper_detected=TRUE?",
        "¿Cuántos dispositivos se encuentran con battery_level < 5% y status=1?",
        "¿Cuál es la persona con ID 056558c7 y dónde está su dispositivo?",
        "Listar todos los dispositivos que tengan restricción_violation=TRUE y lat>40",
        "¿Cómo saber si el dispositivo 6cfc7a7a cambió su estado recientemente?",
        "¿Cuáles son los últimos 5 registros del dispositivo 6cfc7a7a?",
        "Muestra la señal y la batería de cada dispositivo de user_id=f00dabcd",
        "¿Hay dispositivos con timestamp anterior a 2025-01-20?",
        "¿Qué dispositivos se han reactivado en la última hora?",
        "¿Cuáles son las coordenadas del usuario con ID abcd1234?",
        "¿Cuál es el device_id con menor nivel de batería?",
        "¿Cuántos dispositivos están operando normalmente?"
    ]

    for p in ejemplo_pregs:
        st.write(f"- {p}")

def main():
    app()

if __name__ == "__main__":
    main()
