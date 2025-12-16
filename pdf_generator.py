from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_pdf(rfp_text, best_match_row, pricing):
    os.makedirs("saved_rfps", exist_ok=True)

    file_name = f"saved_rfps/RFP_Quotation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "B2B RFP QUOTATION")
    y -= 30

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Date: {datetime.now().strftime('%d-%m-%Y')}")
    y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "RFP Summary")
    y -= 15

    c.setFont("Helvetica", 10)
    for line in rfp_text.split("\n"):
        c.drawString(50, y, line)
        y -= 12

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Recommended Product")
    y -= 15

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"SKU: {best_match_row['SKU']}")
    y -= 12
    c.drawString(50, y, f"Spec Match: {best_match_row['SpecMatch(%)']}%")
    y -= 12
    c.drawString(50, y, f"Voltage: {best_match_row['Voltage']} KV")
    y -= 12
    c.drawString(50, y, f"Conductor: {best_match_row['Conductor']}")
    y -= 12
    c.drawString(50, y, f"Insulation: {best_match_row['Insulation']}")
    y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Commercial Summary")
    y -= 15

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Material Cost: ₹ {pricing['Material Cost']:,}")
    y -= 12
    c.drawString(50, y, f"Testing Cost: ₹ {pricing['Testing Cost']:,}")
    y -= 12
    c.drawString(50, y, f"Total Quoted Cost: ₹ {pricing['Total Cost']:,}")

    y -= 40
    c.drawString(50, y, "This is a system-generated quotation.")

    c.save()
    return file_name
