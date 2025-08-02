import os

# Folder containing PGN files
pgn_folder = "Chess960"
output_file = "merge.pgn"

with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in sorted(os.listdir(pgn_folder)):
        if filename.endswith(".pgn"):
            filepath = os.path.join(pgn_folder, filename)
            with open(filepath, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")  # Separate games with two newlines
print(f"All PGN files merged into {output_file}")
