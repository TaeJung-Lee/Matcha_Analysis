import pdfplumber
import re
import pandas as pd
import os

print("Starting PDF extraction...")

# --- Setup ---
pdf_path = os.path.join("..", "data", "raw_pdfs", "r6chachosa1.pdf")  # Make sure this file exists

# --- Data container ---
data = {
    "year": 2024,
    "tencha_kg": None,
    "aracha_kg": None,
    "aracha_yen": None
}

# --- Open and scan PDF ---
with pdfplumber.open(pdf_path) as pdf:  # ← this defines the 'pdf' variable!
    print("Opened PDF...")

    for i, page in enumerate(pdf.pages):  # ← now 'pdf' is defined, so this works
        text = page.extract_text()
        print(f"\n--- Page {i+1} ---")
        print(text[:500])  # optional preview

        # Match 荒茶 生産量 (tons)
        match_aracha_kg = re.search(r"荒\s*茶\s*生\s*産\s*量\s*([\d,]+\.\d+)", text)
        if match_aracha_kg:
            data["aracha_kg"] = int(float(match_aracha_kg.group(1).replace(",", "")) * 1000)

        # Match 秋てん茶 (tons)
        match_tencha = re.search(r"秋\s*て\s*ん\s*茶\s*\*1\s*([\d,]+\.\d+)", text)
        if match_tencha:
            data["tencha_kg"] = int(float(match_tencha.group(1).replace(",", "")) * 1000)

        # Match 荒茶 生産 金額 (million yen)
        match_aracha_yen = re.search(r"荒\s*茶\s*生\s*産\s*金\s*額\s*([\d,]+\.\d+)", text)
        if match_aracha_yen:
            data["aracha_yen"] = int(float(match_aracha_yen.group(1).replace(",", "")) * 1_000_000)

        if all([data["tencha_kg"], data["aracha_kg"], data["aracha_yen"]]):
            break  # Stop early if we’ve found all three

# --- Save output ---
df = pd.DataFrame([data])
print(df)

output_dir = os.path.join("..", "data", "cleaned_csv")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "uji_production.csv")
df.to_csv(output_path, index=False)
