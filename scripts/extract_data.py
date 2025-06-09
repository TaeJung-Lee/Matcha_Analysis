import pdfplumber
import re
import pandas as pd
import os

print("Starting updated PDF extraction...")

# --- Setup ---
pdf_folder = os.path.join("..", "data", "raw_pdfs")
output_dir = os.path.join("..", "data", "cleaned_csv")
os.makedirs(output_dir, exist_ok=True)

all_data = []

for filename in os.listdir(pdf_folder):
    if not filename.endswith(".pdf"):
        continue

    year_match = re.search(r"(\d{4})", filename)
    if not year_match:
        print(f"Skipping {filename} (no year in filename)")
        continue

    year = int(year_match.group(1))
    pdf_path = os.path.join(pdf_folder, filename)
    print(f"Processing {filename}...")

    row = {
        "year": year,
        "total_field_ha": None,
        "tencha_field_ha": None,
        "cultivated_farmers": None,
        "operating_farmers": None,
        "total_aracha_tons": None,
        "tencha_tons": None,
        "autumn_tencha_tons": 0.0,
        "total_tencha_tons": None,
        "total_aracha_yen_m": None,
        "tencha_yen_m": None,
        "autumn_tencha_yen_m": 0.0,
        "total_tencha_yen_m": None
    }

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()

                match_total_field = re.search(r"\n茶\s*園\s*面\s*積\s+([\d,]+\.\d+)", text)
                if match_total_field:
                    row["total_field_ha"] = float(match_total_field.group(1).replace(",", ""))

                match_tencha_field = re.search(r"て\s*ん\s*茶\s*園\s*([\d,]+\.\d+)", text)
                if match_tencha_field:
                    row["tencha_field_ha"] = float(match_tencha_field.group(1).replace(",", ""))

                match_cultivated = re.search(r"栽\s*培\s*農\s*家\s*数\s*(\d+)", text)
                if match_cultivated:
                    row["cultivated_farmers"] = int(match_cultivated.group(1))

                match_operating = re.search(r"経\s*営\s*農\s*家\s*数\s*(\d+)", text)
                if match_operating:
                    row["operating_farmers"] = int(match_operating.group(1))

                match_total_aracha = re.search(r"荒\s*茶\s*生\s*産\s*量\s*([\d,]+\.\d+)", text)
                if match_total_aracha:
                    row["total_aracha_tons"] = float(match_total_aracha.group(1).replace(",", ""))

                match_tencha = re.search(r"て\s*ん\s*茶\s*([\d,]+\.\d+)", text)
                if match_tencha:
                    row["tencha_tons"] = float(match_tencha.group(1).replace(",", ""))

                match_autumn_tencha = re.search(r"秋\s*て\s*ん\s*茶\s*\*1\s*([\d,]+\.\d+)", text)
                if match_autumn_tencha:
                    row["autumn_tencha_tons"] = float(match_autumn_tencha.group(1).replace(",", ""))

                match_aracha_yen = re.search(r"荒\s*茶\s*生\s*産\s*金\s*額\s*([\d,]+\.\d+)", text)
                if match_aracha_yen:
                    row["total_aracha_yen_m"] = float(match_aracha_yen.group(1).replace(",", ""))

                match_tencha_yen = re.search(r"荒\s*茶\s*生\s*産\s*金\s*額[^\n]+?\n.*?て\s*ん\s*茶\s*([\d,]+\.\d+)", text, re.DOTALL)
                if match_tencha_yen:
                    row["tencha_yen_m"] = float(match_tencha_yen.group(1).replace(",", ""))

                match_autumn_tencha_yen = re.search(r"荒\s*茶\s*生\s*産\s*金\s*額[^\n]+?\n.*?秋\s*て\s*ん\s*茶\s*\*1\s*([\d,]+\.\d+)", text, re.DOTALL)
                if match_autumn_tencha_yen:
                    row["autumn_tencha_yen_m"] = float(match_autumn_tencha_yen.group(1).replace(",", ""))

        # --- Post-processing calculations ---
        row["total_tencha_tons"] = (row["tencha_tons"] or 0) + (row["autumn_tencha_tons"] or 0)
        row["total_tencha_yen_m"] = (row["tencha_yen_m"] or 0) + (row["autumn_tencha_yen_m"] or 0)

        all_data.append(row)

    except Exception as e:
        print(f"Error processing {filename}: {e}")

# --- Save combined dataset ---
df = pd.DataFrame(all_data)
print(df)

output_path = os.path.join(output_dir, "uji_matcha_extracted.csv")
df.to_csv(output_path, index=False)
print(f"Saved to: {output_path}")
