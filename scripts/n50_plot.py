import matplotlib
matplotlib.use("Agg")

from Bio import SeqIO
import matplotlib.pyplot as plt

# Read sequences
lengths = []

for record in SeqIO.parse("subset10.fasta", "fasta"):
    lengths.append(len(record.seq))

# Sort largest to smallest
lengths.sort(reverse=True)

# Total assembly length
total_length = sum(lengths)

# Calculate N50 and L50
running = 0
N50 = 0
L50 = 0

for i, length in enumerate(lengths):
    running += length
    if running >= total_length / 2:
        N50 = length
        L50 = i + 1
        break

print("Total length:", total_length)
print("Number of sequences:", len(lengths))
print("N50:", N50)
print("L50:", L50)

# Plot scaffold lengths
plt.figure(figsize=(8,5))

plt.bar(
    range(1, len(lengths)+1),
    lengths
)

plt.xlabel("Scaffold rank (largest to smallest)")
plt.ylabel("Length (bp)")
plt.title(
    f"Assembly statistics\nN50={N50} bp, L50={L50}"
)

plt.tight_layout()

plt.savefig(
    "N50_L50_plot.png",
    dpi=300,
    bbox_inches="tight"
)

print("N50/L50 plot created")
