import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

x = []
y = []

with open("coords.txt") as f:
    for line in f:

        # skip headers and blank lines
        if line.startswith("[") or line.strip() == "":
            continue

        parts = line.split()

        try:
            x.append(int(parts[0]))
            y.append(int(parts[2]))

        except:
            continue


plt.figure(figsize=(6,6))

plt.scatter(
    x,
    y,
    s=3
)

plt.xlabel("Sequence 1 position (bp)")
plt.ylabel("Sequence 2 position (bp)")

plt.title("Genome dot plot")

plt.tight_layout()

plt.savefig(
    "dot_plot.png",
    dpi=300,
    bbox_inches="tight"
)

print("Dot plot created")
