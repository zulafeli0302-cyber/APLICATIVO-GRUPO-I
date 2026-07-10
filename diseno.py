from pyDOE2 import ccdesign, bbdesign
import pandas as pd

def generar_ccd(factores=3, center=(4,4)):
    diseno = ccdesign(factores, center=center)
    return pd.DataFrame(diseno, columns=[f"X{i+1}" for i in range(factores)])

def generar_bbd(factores=3):
    diseno = bbdesign(factores)
    return pd.DataFrame(diseno, columns=[f"X{i+1}" for i in range(factores)])

def decodificar(diseno, minimos, maximos):
    reales = diseno.copy()
    for i, c in enumerate(reales.columns):
        centro = (maximos[i] + minimos[i]) / 2
        paso = (maximos[i] - minimos[i]) / 2
        reales[c] = centro + paso * reales[c]
    return reales

def ejemplo_cacao_ccd():
    df = generar_ccd(3)
    return decodificar(df, [110,15,6], [150,35,10])

def ejemplo_cacao_bbd():
    df = generar_bbd(3)
    return decodificar(df, [110,15,6], [150,35,10])

if __name__ == "__main__":
    print(ejemplo_cacao_ccd())
    print(ejemplo_cacao_bbd())
