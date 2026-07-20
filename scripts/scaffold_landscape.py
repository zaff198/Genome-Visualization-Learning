import matplotlib
matplotlib.use("Agg")

from Bio import SeqIO
import matplotlib.pyplot as plt


# Input FASTA
fasta_file = "subset10.fasta"


# Read sequences
scaffolds = []

for record in SeqIO.parse(fasta_file, "fasta"):
    scaffolds.append(
        (
            record.id,
            len(record.seq)
        )
    )


# Sort largest to smallest
scaffolds.sort(
    key=lambda x: x[1],
    reverse=True
)


names = [x[0] for x in scaffolds]
lengths = [x[1] for x in scaffolds]


# Create plot
plt.figure(figsize=(10,6))


plt.barh(
    range(len(lengths)),
    lengths
)


plt.yticks(
    range(len(names)),
    names,
    fontsize=7
)


plt.xlabel(
    "Scaffold length (bp)"
)

plt.ylabel(
    "Scaffold"
)


plt.title(
    "Genome Assembly Scaffold Landscape"
)


# Add length labels
for i, value in enumerate(lengths):
    plt.text(
        value,
        i,
        f" {value/1e6:.2f} Mb",
        va="center",
        fontsize=7
    )


plt.gca().invert_yaxis()


plt.tight_layout()


plt.savefig(
    "scaffold_landscape.png",
    dpi=300,
    bbox_inches="tight"
)


print("Scaffold landscape created")
print("Number of scaffolds:", len(lengths))
print("Largest scaffold:", max(lengths), "bp")
print("Total assembly size:", sum(lengths), "bp")
