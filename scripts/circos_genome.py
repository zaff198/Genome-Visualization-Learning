from Bio import SeqIO
from pycirclize import Circos


# Input FASTA
fasta_file = "subset10.fasta"


# Read scaffold lengths
scaffolds = {}

for record in SeqIO.parse(fasta_file, "fasta"):
    scaffolds[record.id] = len(record.seq)


# Create circos object
circos = Circos(
    scaffolds,
    space=3
)


# Add tracks
for sector in circos.sectors:

    # scaffold name
    sector.text(
        sector.name,
        r=110
    )

    # length track
    track = sector.add_track(
        (90,100)
    )

    track.axis()

    track.text(
        f"{sector.size/1e6:.2f} Mb",
        r=95
    )


# Plot
fig = circos.plotfig()

fig.savefig(
    "circos_genome.png",
    dpi=300,
    bbox_inches="tight"
)


print("Circos plot created")
print("Number of scaffolds:", len(scaffolds))
