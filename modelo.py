import pandas as pd
import statsmodels.formula.api as smf

def ajustar_modelo(df):
    formula=("Calidad ~ Temperatura + Tiempo + Humedad + "
             "I(Temperatura**2)+I(Tiempo**2)+I(Humedad**2)+"
             "Temperatura:Tiempo+Temperatura:Humedad+Tiempo:Humedad")
    modelo=smf.ols(formula,data=df).fit()
    return modelo

def resumen(modelo):
    anova=modelo.summary2().tables[1]
    return {
        "r2":modelo.rsquared,
        "r2_ajustado":modelo.rsquared_adj,
        "coeficientes":anova,
        "residuos":modelo.resid
    }

if __name__=="__main__":
    df=pd.read_csv("data/cacao.csv")
    m=ajustar_modelo(df)
    print(m.summary())
