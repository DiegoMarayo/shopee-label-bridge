from pypdf import PdfReader, PdfWriter, Transformation
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import mm
import io
import copy
import os

LABEL_WIDTH = 100 * mm
LABEL_HEIGHT = 144 * mm

def criar_base():
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=(LABEL_WIDTH, LABEL_HEIGHT))
    c.showPage()
    c.save()
    buffer.seek(0)
    return PdfReader(buffer)

#  ETAPA 1 - EXTRAÇÃO
def extrair_etiquetas(input_pdf, output_temp):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    total = 0

    for page in reader.pages:

        largura = float(page.mediabox.width)
        altura = float(page.mediabox.height)

        # 🔥 SEUS AJUSTES (mantidos)
        margem_esquerda = largura * 0.0
        margem_topo = altura * 0.0

        gap_x = largura * 0.01
        gap_y = altura * 0.0

        largura_label = (largura - margem_esquerda - gap_x) / 2
        altura_label = (altura - margem_topo - gap_y) / 2

        quadrantes = [
            # 1
            (
                margem_esquerda,
                altura - margem_topo - altura_label,
                margem_esquerda + largura_label,
                altura - margem_topo
            ),
            # 2
            (
                margem_esquerda,
                margem_topo,
                margem_esquerda + largura_label,
                margem_topo + altura_label
            ),
            # 3
            (
                margem_esquerda + largura_label + gap_x,
                altura - margem_topo - altura_label,
                largura,
                altura - margem_topo
            ),
            # 4
            (
                margem_esquerda + largura_label + gap_x,
                margem_topo,
                largura,
                margem_topo + altura_label
            ),
        ]

        for (x1, y1, x2, y2) in quadrantes:

            base_pdf = criar_base()
            base_page = base_pdf.pages[0]

            largura_crop = x2 - x1
            altura_crop = y2 - y1

            escala = min(
                LABEL_WIDTH / largura_crop,
                LABEL_HEIGHT / altura_crop
            )

            transform = (
                Transformation()
                .translate(-x1, -y1)
                .scale(escala)
            )

            temp_page = copy.deepcopy(page)

            base_page.merge_transformed_page(temp_page, transform)

            writer.add_page(base_page)
            total += 1

    with open(output_temp, "wb") as f:
        writer.write(f)

    print(f"📦 Geradas (bruto): {total}")

#  ETAPA 2 - LIMITAR
def limitar_etiquetas(input_pdf, output_pdf, max_etiquetas):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    total = 0

    for i, page in enumerate(reader.pages):
        if i >= max_etiquetas:
            break
        writer.add_page(page)
        total += 1

    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"✅ Total final: {total} etiquetas")

#  EXECUÇÃO
if __name__ == "__main__":

    input_pdf = "entrada.pdf"
    temp_pdf = "temp.pdf"
    output_pdf = "saida_100x150.pdf"

    # INPUT DO USUÁRIO
    while True:
        try:
            total_etiquetas = int(input("Digite o total de etiquetas: "))
            if total_etiquetas > 0:
                break
            else:
                print("Digite um número maior que 0.")
        except:
            print("Entrada inválida. Digite um número inteiro.")

    # 1️⃣ extrai tudo
    extrair_etiquetas(input_pdf, temp_pdf)

    # 2️⃣ limita ao total correto
    limitar_etiquetas(temp_pdf, output_pdf, total_etiquetas)

    # 3️⃣ remove temporário
    if os.path.exists(temp_pdf):
        os.remove(temp_pdf)

    print("🚀 Processo finalizado com sucesso!")