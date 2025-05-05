import streamlit as st

st.set_page_config(page_title="📘 Teoría del Coeficiente de Spearman", page_icon="📘")

st.title("📘 Introducción al Coeficiente de Spearman")
st.markdown(r"""
El coeficiente de correlación de **Spearman** (\\( r_s \\)) es una medida no paramétrica que evalúa la **fuerza y dirección de una relación monótonica** entre dos variables. A diferencia del coeficiente de Pearson, Spearman no requiere que los datos sean lineales ni que sigan una distribución normal.

---

### 📌 ¿Cuándo se utiliza Spearman?
- Cuando los datos no son normales o contienen **valores atípicos**.
- Cuando se desea evaluar si **una variable aumenta o disminuye consistentemente** con otra, aunque no sea en línea recta.
- Ideal para **datos ordinales** o cuando solo se conoce el **ranking** de los elementos.

---

### 🧠 ¿Cómo se calcula?
Se asignan **rangos** a los datos de ambas variables. Luego, se calcula la diferencia entre estos rangos y se aplica la fórmula:

$$
r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}
$$

Donde:
- \\( d_i \\) es la diferencia entre los rangos de cada observación  
- \\( n \\) es el número de pares de datos

---

### ⚠️ Limitaciones de Spearman
- **No detecta relaciones no monótonas** (por ejemplo, relaciones cuadráticas).
- Es **menos potente** que Pearson cuando se cumplen los supuestos de este último.
- En presencia de **muchos empates**, los rangos pueden distorsionar el resultado.

---

### ✅ Ventajas
- Robusto frente a valores atípicos.
- Funciona con **datos categóricos ordinales**.
- No requiere normalidad ni homocedasticidad.
""")

with st.expander("📌 Consideraciones sobre empates en los rangos"):
    st.markdown(r"""
### 🤔 ¿Qué ocurre cuando hay empates?

Cuando dos o más valores son iguales en una variable, se les asigna el **rango promedio** de sus posiciones. Aunque esta técnica permite seguir aplicando Spearman, **afecta la precisión** del resultado.

---

### 📐 ¿Cómo se calcula el rango promedio?

Si un valor se repite varias veces, se promedian los rangos que le corresponderían si no hubiese empate.  
La fórmula es:

$$
\text{Rango promedio} = \frac{r_1 + r_2 + \dots + r_k}{k}
$$

Donde:
- \\( r_1, r_2, \dots, r_k \\) son los rangos que ocuparían las posiciones empatadas
- \\( k \\) es la cantidad de observaciones empatadas

---

### 📊 Ejemplo simple:
""", unsafe_allow_html=True)

    st.markdown("""
<div style='overflow-x: auto'>
<table>
<thead>
<tr>
<th>Valor original</th>
<th>Posiciones esperadas</th>
<th>Cálculo del rango promedio</th>
<th>Rango asignado</th>
</tr>
</thead>
<tbody>
<tr>
<td>10</td>
<td>1</td>
<td>—</td>
<td>1</td>
</tr>
<tr>
<td>20</td>
<td>2 y 3</td>
<td>\\( (2 + 3) / 2 = 2.5 \\)</td>
<td>2.5</td>
</tr>
<tr>
<td>20</td>
<td>2 y 3</td>
<td>\\( (2 + 3) / 2 = 2.5 \\)</td>
<td>2.5</td>
</tr>
<tr>
<td>30</td>
<td>4</td>
<td>—</td>
<td>4</td>
</tr>
</tbody>
</table>
</div>
""", unsafe_allow_html=True)

    st.markdown(r"""
---

### ⚠️ Efecto de los empates:
- La fórmula estándar de Spearman **asume que no hay empates**.
- Si hay muchos empates, el coeficiente **puede subestimar o sobreestimar** la verdadera correlación.

---

### 💡 ¿Qué hacer ante muchos empates?
""", unsafe_allow_html=True)

    st.markdown("""
<div style='overflow-x: auto'>
<table>
<thead>
<tr>
<th>Situación</th>
<th>Recomendación</th>
</tr>
</thead>
<tbody>
<tr>
<td>Empates ocasionales</td>
<td>Puedes seguir usando Spearman</td>
</tr>
<tr>
<td>Muchos empates o muchas categorías</td>
<td>Considera usar <strong>Kendall's Tau</strong></td>
</tr>
<tr>
<td>Datos ordinales repetitivos</td>
<td>Kendall tiende a ser <strong>más robusto</strong></td>
</tr>
</tbody>
</table>
</div>
""", unsafe_allow_html=True)

    st.markdown(r"""
> **Kendall's Tau** evalúa la relación entre pares ordenados y es menos sensible a los empates, ofreciendo una alternativa más precisa en estas situaciones.

---

### 🧩 En resumen:
- Puedes seguir usando Spearman con empates, pero **su precisión se reduce**.
- **Kendall** es una mejor opción si los empates son frecuentes o el dataset es pequeño y ordinal.
""")

st.page_link("app.py", label="⬅️ Volver al inicio")
