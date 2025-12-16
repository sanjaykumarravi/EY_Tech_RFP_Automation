import pandas as pd

def price_sku(sku, quantity_km):
    pricing = pd.read_csv("data/pricing_table.csv")
    row = pricing[pricing['SKU'] == sku].iloc[0]
    material = row['UnitPricePerKM'] * quantity_km
    total = material + row['TestCost']
    return {
        "SKU": sku,
        "Material Cost": material,
        "Testing Cost": row['TestCost'],
        "Total Cost": total
    }
