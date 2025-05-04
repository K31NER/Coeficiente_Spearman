import streamlit as st
import plotly.express as px
from Spearman import Calcular_coeficiente, calcular_coeficiente_paso_a_paso

st.set_page_config(
    page_icon="https://cdn-icons-png.flaticon.com/128/891/891175.png",
    page_title="Coeficiente de Spearman",
    layout="wide"
)

st.title("📈 Calculadora de Coeficiente de Spearman")
st.page_link("pages/teoria.py", label="Ir a la teoría", icon="📘")

st.markdown("Ingrese los datos separados por comas (ejemplo: `4, 6, 2, 8, 5`)")

c1, c2 = st.columns(2)

with c1:
    texto_x = st.text_area("Datos de X", value="4, 6, 2, 8, 5")
with c2:
    texto_y = st.text_area("Datos de Y", value="78, 85, 72, 88, 80")

# Elegir modo de cálculo
modo = st.radio("Modo de cálculo", ["🔁 Paso a paso", "⚡ Directo"])


def convertir_a_lista(texto):
    try:
        return [float(x.strip()) for x in texto.split(",") if x.strip() != ""]
    except ValueError:
        st.error("🚫 Asegúrate de ingresar solo números separados por comas.")
        return None

def interpretar_spearman(rs: float) -> str:
    if rs == 1:
        return "💯 Correlación perfecta positiva"
    elif rs == -1:
        return "💀 Correlación perfecta negativa"
    elif rs > 0.8:
        return "🔗 Correlación muy fuerte positiva"
    elif rs > 0.6:
        return "📈 Correlación fuerte positiva"
    elif rs > 0.4:
        return "🔄 Correlación moderada positiva"
    elif rs > 0.2:
        return "⚖️ Correlación débil positiva"
    elif rs > -0.2:
        return "❔ Correlación nula o muy débil"
    elif rs > -0.4:
        return "⚖️ Correlación débil negativa"
    elif rs > -0.6:
        return "🔄 Correlación moderada negativa"
    elif rs > -0.8:
        return "📉 Correlación fuerte negativa"
    else:
        return "🔗 Correlación muy fuerte negativa"

if st.button("🔍 Calcular coeficiente"):
    datos_x = convertir_a_lista(texto_x)
    datos_y = convertir_a_lista(texto_y)

    if datos_x is None or datos_y is None:
        st.stop()

    if len(datos_x) != len(datos_y):
        st.error("🚫 Los conjuntos de datos deben tener la misma cantidad de elementos.")
        st.stop()

    try:
        if modo == "🔁 Paso a paso":
            df, rs = calcular_coeficiente_paso_a_paso(datos_x, datos_y)
        else:
            df, rs = Calcular_coeficiente(datos_x, datos_y)
            st.subheader("✅ Resultado final del coeficiente")
            st.latex(fr"""r_s = {round(rs, 4)}""")

        interpretacion = interpretar_spearman(rs)
        st.success(f"📌 Interpretación: **{interpretacion}**")

        st.subheader("📊 :blue[Representación gráfica]")
        fig = px.scatter(df, x="rango_x", y="rango_y", text=df.index,
                         labels={"rango_x": "Rango X", "rango_y": "Rango Y"},
                         title="Relación entre Rangos de X y Y",
                         trendline="ols")
        fig.update_traces(marker=dict(size=12, color="skyblue"), textposition="top center")
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Ocurrió un error al calcular el coeficiente: {e}")
