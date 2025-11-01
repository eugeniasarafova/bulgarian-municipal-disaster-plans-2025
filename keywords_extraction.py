# Example for keyword analysis for extracted municipal plan texts. The keywords listed below are in bulgarian language as the analysed documents are in bulgarian.
# Libraries used - pandas

import pandas as pd
import glob

# Define the folder where the extracted .txt files are stored
folder = "extracted_texts/"

# Define keywords to search for (in Bulgarian)
keywords = {
    "earthquake": "земетресение",
    "flood": "наводнение",
    "nuclear_radiation": "радиация",
    "fire": "пожар",
    "landslide": "свлачище",
    "heatwave": "гореща вълна",
    "drought": "засушаване",
    "climate_change": "изменение на климата",
    "epidemic": "епидемия",
}

# Prepare an empty list to collect results
records = []

# Loop through all text files in the folder
for file_path in glob.glob(folder + "*.txt"):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read().lower()

    # Count keyword occurrences
    counts = {k: text.count(v) for k, v in keywords.items()}

    # Record the results
    records.append({
        "filename": file_path.split("/")[-1],
        **counts
    })

# Convert to a DataFrame
df = pd.DataFrame(records)

# Save to CSV
df.to_csv("hazard_keyword_counts.csv", index=False, encoding="utf-8")

print("Keyword counts saved to hazard_keyword_counts.csv")
print(df.head())

# Note: There are some keywords that are synonims in bulgarian which lead to the fact that there wes a need for a manual checking up of all the documents for verification. There were cases where not traditional terms were used in the plans.
