import numpy as np
from scipy.optimize import minimize

def objetivo(x, modelo):
    temp, tiempo, hum = x
    datos = {
        "Temperatura":[temp],
        "Tiempo":[tiempo],
        "Humedad":[hum]
    }
    return -modelo.predict(datos)[0]

def optimizar(modelo, inicio=[130,25,8]):
    res=minimize(objetivo, inicio, args=(modelo,),
                 bounds=[(110,150),(15,35),(6,10)])
    return {
        "Temperatura":res.x[0],
        "Tiempo":res.x[1],
        "Humedad":res.x[2],
        "Calidad_Predicha":-res.fun,
        "Convergencia":res.success
    }

def gradiente_simple(modelo,punto,delta=0.1):
    base=modelo.predict({
        "Temperatura":[punto[0]],
        "Tiempo":[punto[1]],
        "Humedad":[punto[2]]
    })[0]
    grad=[]
    for i in range(3):
        p=punto.copy()
        p[i]+=delta
        y=modelo.predict({
            "Temperatura":[p[0]],
            "Tiempo":[p[1]],
            "Humedad":[p[2]]
        })[0]
        grad.append((y-base)/delta)
    return np.array(grad)
