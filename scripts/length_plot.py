import matplotlib
matplotlib.use("Agg")

from Bio import SeqIO
import matplotlib.pyplot as plt

lengths=[]

for record in SeqIO.parse("subset10.fasta","fasta"):
    lengths.append(len(record.seq))

plt.figure(figsize=(8,5))

plt.bar(range(1,len(lengths)+1), lengths)

plt.xlabel("Sequence number")
plt.ylabel("Length (bp)")
plt.title("Length distribution of genome sequences")

plt.savefig(
    "length_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

print("Plot created")
