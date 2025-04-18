
import streamlit as st

st.title("Calculadora de Rentabilidad ENCARTE")

# Entradas del usuario
producto = st.text_input("¿Qué producto deseas fabricar?")
cantidad = st.number_input("Cantidad a fabricar", min_value=1, format="%d")
tintas = st.number_input("Coste de tintas (€)", min_value=0.0, format="%.2f")
soporte = st.text_input("Nombre del soporte")
coste_soporte = st.number_input("Coste del soporte (€)", min_value=0.0, format="%.2f")
laminado = st.number_input("Coste de laminado (€)", min_value=0.0, format="%.2f")
barniz = st.number_input("Coste de barniz (€)", min_value=0.0, format="%.2f")
foil = st.number_input("Coste de foil (€)", min_value=0.0, format="%.2f")
externo = st.number_input("Coste externo de manipulado (€)", min_value=0.0, format="%.2f")

# Botón para calcular
if st.button("Calcular costes"):
    suma_costes = tintas + coste_soporte + laminado + barniz + foil + externo
    coste_unitario = suma_costes / cantidad

    st.subheader("Resultados de Costes")
    st.write(f"**Suma total de costes:** {suma_costes:.2f} €")
    st.write(f"**Coste unitario:** {coste_unitario:.3f} €/unidad")

    # Entrada de precio de venta
    precio_venta = st.number_input("Precio unitario de venta (€)", min_value=0.0, format="%.2f")
    if precio_venta > 0:
        beneficio_unitario = precio_venta - coste_unitario
        beneficio_total = beneficio_unitario * cantidad
        rentabilidad = (beneficio_unitario / coste_unitario) * 100

        st.subheader("Rentabilidad")
        st.write(f"**Beneficio unitario:** {beneficio_unitario:.3f} €")
        st.write(f"**Beneficio total:** {beneficio_total:.2f} €")
        st.write(f"**Rentabilidad:** {rentabilidad:.2f} %")
