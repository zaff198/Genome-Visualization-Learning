import matplotlib
matplotlib.use("Agg")

from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np


# Input FASTA
fasta_file = "subset10.fasta"


# Parameters
window_size = 10000   # 10 kb window


# Store data
scaffold_names = []
gc_matrix = []


# Read all sequences
for record in SeqIO.parse(fasta_file, "fasta"):

    seq = str(record.seq).upper()

    scaffold_names.append(record.id)

    gc_values = []

    for i in range(0, len(seq), window_size):

        window = seq[i:i+window_size]

        if len(window) > 0:

            gc = (
                (window.count("G") + window.count("C"))
                / len(window)
            ) * 100

            gc_values.append(gc)

    gc_matrix.append(gc_values)



# Convert to rectangular matrix
max_length = max(len(x) for x in gc_matrix)

matrix = []

for row in gc_matrix:

    row = row + [np.nan] * (max_length - len(row))

    matrix.append(row)


matrix = np.array(matrix)



# Plot heatmap
plt.figure(figsize=(12,6))

plt.imshow(
    matrix,
    aspect="auto",
    interpolation="nearest"
)


plt.colorbar(
    label="GC content (%)"
)


plt.yticks(
    range(len(scaffold_names)),
    scaffold_names,
    fontsize=7
)


plt.xlabel(
    "Genome position (10 kb windows)"
)


plt.ylabel(
    "Scaffold"
)


plt.title(
    "Genome GC Content Heatmap"
)


plt.tight_layout()


plt.savefig(
    "GC_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)


print("GC heatmap created")
print("Scaffolds analysed:", len(scaffold_names))
