# Genome Visualization Learning Project

## Overview

This repository contains a reproducible workflow for exploring and visualizing genome assemblies from FASTA files.

The project demonstrates how raw genome sequence data can be transformed into statistical summaries and publication-style visualizations using Linux, Python, Biopython, matplotlib, SeqKit, and pycirclize.

The workflow was developed as a learning project in genome informatics.

<img width="2480" height="3760" alt="genome_visualization_collage" src="https://github.com/user-attachments/assets/7deee0b1-4828-4564-9e39-2766a9b85344" />


---

# Dataset

## Genome Source

The genome assembly used in this project was downloaded from NCBI:

Assembly:
GCA_041941825.1_ASM4194182v1

Organism:
Colletotrichum lindemuthianum

Original file:

GCA_041941825.1_ASM4194182v1_genomic.fna.gz

The complete FASTA file contains thousands of genomic sequences/scaffolds.

For computational practice, a smaller subset was created:

subset10.fasta

This subset contains the first 10 sequences extracted from the complete genome assembly.

All visualization scripts are written so they can later be applied to complete genome assemblies.

---

# Workflow

## 1. FASTA Processing

Input:

- Genome FASTA file

Operations:

- sequence extraction
- sequence length calculation
- GC calculation
- scaffold statistics


Tools:

- SeqKit
- Biopython


---

# Visualizations


## Sequence Length Distribution

Script:

scripts/length_plot.py


Output:

results/length_distribution.png


Purpose:

Shows variation in sequence/scaffold sizes.


---

## GC Content Plot

Script:

scripts/gc_plot.py


Output:

results/GC_content_plot.png


Purpose:

Displays nucleotide composition across genomic regions.


---

## N50 and L50 Analysis

Script:

scripts/n50_plot.py


Output:

results/N50_L50_plot.png


Purpose:

Evaluates assembly continuity.


---

## Scaffold Landscape

Script:

scripts/scaffold_landscape.py


Output:

results/scaffold_landscape.png


Purpose:

Shows scaffold size distribution visually.


---

## GC Content Heatmap

Script:

scripts/gc_heatmap.py


Output:

results/GC_heatmap.png


Purpose:

Displays GC variation across multiple genomic sequences.


---

## Circos Genome Visualization

Script:

scripts/circos_genome.py


Output:

results/circos_genome.png


Purpose:

Creates a circular genome overview similar to figures used in genome publications.


---

## Genome Summary Dashboard

Script:

scripts/genome_summary_plot.py


Output:

results/genome_summary_dashboard.png


Purpose:

Combines multiple genome statistics into a single overview figure.


---

## Dot Plot Experiment

Script:

scripts/dotplot.py


Purpose:

Attempted whole sequence comparison visualization using MUMmer.

This represents a common comparative genomics approach.

---

# Software Environment

Operating system:

Linux (WSL Ubuntu)


Programming:

Python 3.11


Packages:

- Biopython
- matplotlib
- pycirclize


Bioinformatics tools:

- SeqKit
- MUMmer4


Conda environment:

genomeplot


---

# Repository Structure


Genome-Visualization-Learning/





data/
subset10.fasta

scripts/
genome analysis scripts

results/
generated figures






---

# Future Extensions

Possible future additions:

- genome annotation visualization
- GFF feature tracks
- BUSCO genome completeness analysis
- repeat analysis
- whole genome alignment
- synteny analysis
- comparative genomics workflows


---

# Learning Goal

This project demonstrates the complete workflow:

FASTA sequence

↓

Genome statistics

↓

Visualization

↓

Biological interpretation


The repository provides a foundation for future genome assembly and comparative genomics projects.
