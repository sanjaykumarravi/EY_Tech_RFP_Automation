from scraper import read_rfp
from matcher import match_skus
from pricing import price_sku
from pdf_generator import generate_pdf

def run_agents():
    rfp_text = read_rfp()
    matches = match_skus(rfp_text)

    best_match = matches.iloc[0]
    pricing = price_sku(best_match["SKU"], quantity_km=10)

    pdf_path = generate_pdf(rfp_text, best_match, pricing)

    return {
        "rfp_text": rfp_text,
        "matches": matches,
        "pricing": pricing,
        "pdf_path": pdf_path
    }
