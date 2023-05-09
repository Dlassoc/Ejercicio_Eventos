from typing import Dict, Any

class AnalizadorEventos:
  def __init__(self, nombre_archivo: str):
       self.nombre_archivo = nombre_archivo

  def procesar_eventos(self) -> Dict[str, Any]:
    eventos_por_tipo = {}
    eventos_por_servidor = {}
    total_eventos = 0

    with open(self.nombre_archivo, "r", encoding = "ISO-8859-1") as file:
     for linea in file:
       if "Tipo de evento" in linea:
         tipo_evento = linea.strip().split(": ")[1]
         eventos_por_tipo[tipo_evento] = eventos_por_tipo.get(tipo_evento, 0) + 1
         total_eventos += 1

       elif "Servidor" in linea:
         nombre_servidor = linea.strip().split(": ")[1]
         eventos_por_servidor[nombre_servidor] = eventos_por_servidor.get(nombre_servidor, 0) + 1
         total_eventos += 1


    estadisticas = {
       "total_eventos": total_eventos,
       "eventos_por_tipo": eventos_por_tipo,
       "eventos_por_servidor": eventos_por_servidor
       }


    return estadisticas


A = AnalizadorEventos("eventos.txt")
A.procesar_eventos()
