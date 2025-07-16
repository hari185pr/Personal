import json
import os

def trim_waifu_dataset(input_file="waifus.json", output_file="waifus_9000.json", limit=9000):
    if not os.path.exists(input_file):
        print(f"❌ Input file '{input_file}' not found.")
        return

    with open(input_file, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    if isinstance(data, list):
        trimmed = data[:limit]
    elif isinstance(data, dict):
        trimmed = dict(list(data.items())[:limit])
    else:
        print("❌ Unsupported JSON format. Must be a list or dict.")
        return

    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(trimmed, outfile, indent=2, ensure_ascii=False)

    print(f"✅ Trimmed dataset saved to '{output_file}' with {limit} waifus.")

if __name__ == "__main__":
    trim_waifu_dataset()