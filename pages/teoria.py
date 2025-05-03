import streamlit as st

st.set_page_config(page_title="📘 Teoría del Coeficiente de Spearman", page_icon="📘")

st.title("📘 Introducción al Coeficiente de Spearman")
st.markdown("""
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
r_s = 1 - \\frac{6 \\sum d_i^2}{n(n^2 - 1)}
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

---
""")

st.info("👈 Usa el menú de la izquierda para volver a la calculadora y ver el proceso paso a paso.")
