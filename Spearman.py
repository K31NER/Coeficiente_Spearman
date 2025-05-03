import pandas as pd
import numpy as np 
import plotly.express as px
import streamlit as st 

def Calcular_coeficiente(x: list, y :list) -> tuple[float,pd.DataFrame]:
    """Funciion para calcular el coeficiente de Spearman entre dos listas."""
    # Obtenemos los 2 rangos de las listas
    X = np.array(x)
    Y = np.array(y) 
    if len(x) != len(y):
        raise ValueError("Las listas deben tener la misma longitud.")
    
    try:
        # Volvemos los datos en un dataframe
        df = pd.DataFrame({'X': X, 'Y': Y})
        
        # Calculamos los rangos de cada lista 
        df['rango_x'] = df['X'].rank()
        df['rango_y'] = df['Y'].rank()
        
        # Calculamos la diferencia entre los rangos
        df['d'] = df['rango_x'] - df['rango_y']
        
        # Calculamos el cuadrado de la diferencias
        df['d²'] = df['d'] ** 2
        
        suma_diferencias = df['d²'].sum()
        
        # Calculamos el coeficiente de spearman con su formula
        spearman = 1 - (6 * suma_diferencias) / (len(df["X"]) * (len(df["X"])**2 - 1))
        
        # Devolvemos la tabla y el coeficiente
        return df , spearman
    except Exception as e:
        raise ValueError(f"Error al calcular los rangos: {e}")


def calcular_coeficiente_paso_a_paso(x: list, y: list) -> tuple[pd.DataFrame, float]:
    """Función para calcular el coeficiente de Spearman entre dos listas paso a paso con explicaciones en LaTeX."""

    X = np.array(x)
    Y = np.array(y)

    if len(x) != len(y):
        raise ValueError("Las listas deben tener la misma longitud.")

    try:
        df = pd.DataFrame({'X': X, 'Y': Y})

        # Paso 1
        st.subheader("Paso 1: Crear la tabla inicial")
        st.latex(r"Se\ parte\ de\ dos\ listas:\ X = \{x_1, x_2, ..., x_n\}\ y\ Y = \{y_1, y_2, ..., y_n\}")
        st.dataframe(df)

        # Paso 2
        df['rango_x'] = df['X'].rank()
        df['rango_y'] = df['Y'].rank()
        st.subheader("Paso 2: Calcular los rangos")
        st.latex(r"Se\ asignan\ rangos:\ R(x_i),\ R(y_i)\ \text{ordenando de menor a mayor}")
        st.dataframe(df)

        # Paso 3
        df['d'] = df['rango_x'] - df['rango_y']
        st.subheader("Paso 3: Calcular la diferencia entre rangos")
        st.latex(r"d_i = R(x_i) - R(y_i)")
        st.dataframe(df)

        # Paso 4
        df['d²'] = df['d'] ** 2
        st.subheader("Paso 4: Elevar al cuadrado cada diferencia")
        st.latex(r"d_i^2 = (R(x_i) - R(y_i))^2")
        st.dataframe(df)

        # Paso 5
        suma_diferencias = df['d²'].sum()
        st.subheader("Paso 5: Sumar todas las diferencias al cuadrado")
        st.latex(r"\sum d_i^2 = " + str(suma_diferencias))

        # Paso 6: Fórmula final
        n = len(df["X"])
        spearman = 1 - (6 * suma_diferencias) / (n * (n**2 - 1))

        st.subheader("Paso 6: Aplicar la fórmula del coeficiente de Spearman")
        st.latex(r"""
        r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}
        """)
        st.latex(
            fr"""r_s = 1 - \frac{{6 \cdot {suma_diferencias}}}{{{n}({n}^2 - 1)}} = {round(spearman, 4)}"""
        )

        return df, spearman

    except Exception as e:
        raise ValueError(f"Error al calcular los rangos: {e}")
