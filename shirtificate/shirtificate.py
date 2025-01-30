from fpdf import FPDF
from fpdf import enums

class PDF(FPDF):
    def header(self):
        titleText = "CS50 Shirtificate"
        self.set_font("helvetica", style="B", size=20)
        self.cell(w=180,
                  text=titleText,
                  align='C',
                  border=1,
                  center=True
                  )

def main():
    nameCertificate = input("Name: ") + " took CS50"
    pdf = PDF()
    pdf.add_page()
    pdf.ln(100)
    pdf.image("shirtificate.png", x=enums.Align.C, y=50, w=pdf.epw)
    pdf.set_title("CS50 Shirtificate")
    pdf.set_text_color(255,255,255)
    pdf.set_font_size(28)
    pdf.multi_cell(w=120, text=nameCertificate, align='C', center=True)
    pdf.output("shirtificate.pdf")




if __name__ == "__main__":
    main()

