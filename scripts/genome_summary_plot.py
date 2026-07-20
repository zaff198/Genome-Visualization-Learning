import matplotlib
matplotlib.use("Agg")

from Bio import SeqIO
import matplotlib.pyplot as plt


# Read fasta
names = []
lengths = []
gc_values = []

for record in SeqIO.parse("subset10.fasta", "fasta"):

    seq = str(record.seq).upper()

    names.append(record.id)

    lengths.append(len(seq))

    gc = ((seq.count("G") + seq.count("C")) /
          len(seq)) * 100

    gc_values.append(gc)


# Create figure
fig, axes = plt.subplots(2, 1, figsize=(10,8))


# Length plot
axes[0].bar(
    range(len(lengths)),
    lengths
)

axes[0].set_title(
    "Genome subset: sequence lengths"
)

axes[0].set_ylabel(
    "Length (bp)"
)


# GC plot
axes[1].bar(
    range(len(gc_values)),
    gc_values
)

axes[1].set_title(
    "GC content of sequences"
)

axes[1].set_ylabel(
    "GC (%)"
)

axes[1].set_xlabel(
    "Sequence number"
)


plt.tight_layout()


plt.savefig(
    "genome_summary_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)


print("Dashboard created")
