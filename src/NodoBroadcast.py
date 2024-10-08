import simpy
import time
from Nodo import *
from Canales.CanalBroadcast import *

# La unidad de tiempo
TICK = 1


class NodoBroadcast(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de Broadcast.'''

    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida, mensaje=None):
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.mensaje = mensaje

    def broadcast(self, env):
        ''' Algoritmo de Broadcast. Desde el nodo distinguido (0)
            vamos a enviar un mensaje a todos los demás nodos.'''
        if self.id_nodo == 0:
            #Nodo distinguido envía mensaje a sus vecinos
            self.mensaje="hola"
            env.process(self.canal_salida.envia(self.mensaje, self.vecinos))

        while True:
            mensaje_recibido = yield self.canal_entrada.get()
        
            if self.mensaje==None:
                self.mensaje = mensaje_recibido

            #Envia mensaje a todos sus vecinos
            env.process(self.canal_salida.envia(mensaje_recibido, self.vecinos))

            yield env.timeout(TICK)

