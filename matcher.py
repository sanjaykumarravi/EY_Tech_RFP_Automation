import pandas as pd

def match_skus(rfp_text):
    catalog = pd.read_csv("data/product_catalog.csv")
    scores = []
    for _, row in catalog.iterrows():
        score = 0
        if str(row['Voltage']) in rfp_text:
            score += 25
        if row['Conductor'] in rfp_text:
            score += 25
        if row['Insulation'] in rfp_text:
            score += 25
        if row['Standard'] in rfp_text:
            score += 25
        scores.append(score)
    catalog['SpecMatch(%)'] = scores
    return catalog.sort_values("SpecMatch(%)", ascending=False)
