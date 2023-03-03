import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
st.title("🎓 Diploma PDF Generador")


left, right = st.columns(2)

right.write("Esta es la plantilla que usaremos:")

right.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


left.write("Rellena los datos:")
form = left.form("template_form")
student = form.text_input("Nombre del estudiante")
course = form.selectbox(
    "elegir curso",
    ["Machine Learning con lentes", "Criptografia sin lentes"],
    index=0,
)
grade = form.slider("Puntaje", 1, 100, 60)
submit = form.form_submit_button("Generar PDF")

if submit:
    html = template.render(
        student=student,
        course=course,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    right.success("🎉 ¡Tu diploma fue generado!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️ Descargar PDF",
        data=pdf,
        file_name="diploma.pdf",
        mime="application/octet-stream",
    )
