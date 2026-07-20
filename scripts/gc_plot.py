import matplotlib
matplotlib.use("Agg")

from Bio import SeqIO
import matplotlib.pyplot as plt

# Read first sequence from FASTA
record = next(SeqIO.parse("subset10.fasta", "fasta"))

sequence = str(record.seq).upper()

# Window size (10 kb)
window = 10000

positions = []
gc_values = []

# Calculate GC percentage
for i in range(0, len(sequence), window):
    fragment = sequence[i:i+window]

    if len(fragment) > 0:
        gc = ((fragment.count("G") + fragment.count("C")) /
              len(fragment)) * 100

        positions.append(i)
        gc_values.append(gc)

# Make plot
plt.figure(figsize=(10,4))

plt.plot(positions, gc_values)

plt.xlabel("Genome position (bp)")
plt.ylabel("GC content (%)")
plt.title("GC content across scaffold")

plt.tight_layout()

plt.savefig(
    "GC_content_plot.png",
    dpi=300,
    bbox_inches="tight"
)

print("GC plot created")
