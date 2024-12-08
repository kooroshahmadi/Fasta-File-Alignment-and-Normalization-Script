## Fasta File Alignment and Normalization Script

### 📜 **Description**  
This Python script processes FASTA files to ensure that all sequences have the same length by padding shorter sequences with gaps (`"-"`) and trimming longer sequences. It identifies the longest sequence in the file as the reference length and adjusts all other sequences accordingly. This normalization is crucial for bioinformatics analyses, such as phylogenetic tree construction and multiple sequence alignment, where input sequences must be uniform in length.

---

### 💡 **Use Case**  
This script is useful in a variety of bioinformatics applications:
- **Phylogenetic Tree Construction**: Ensures sequences are of equal length for tree-building tools like **IQ-TREE** and **RAxML**.
- **Multiple Sequence Alignment (MSA)**: Prepares sequence data for tools like **MAFFT** and **ClustalW**, which require consistent sequence lengths.
- **Molecular Evolution Analysis**: Supports tools like **PAML** and **BEAST** that analyze genetic variation, conserved regions, and selection pressure.
- **High-Throughput Data Processing**: Normalizes large genomic datasets, ensuring compatibility with online platforms and local software.
- **Error Handling for Online Tools**: Prevents job failures due to sequence length issues in servers like **IQ-TREE**.
- **Educational Tool**: Ideal for teaching sequence alignment and bioinformatics data preprocessing.

---

### 🚀 **Features**
1. **Automatic Length Adjustment**: Detects the longest sequence and adjusts all others to match.
2. **Error Handling**: Improves robustness by managing incomplete or improperly formatted sequences.
3. **Easy Integration**: Simple to run or integrate into bioinformatics pipelines.

---

### 🧰 **Requirements**
- Python 3.6 or higher
- Libraries:  
  - `biopython` for parsing and processing FASTA files

---

### 🛠️ **How to Use**  
1. Clone the repository:
   ```bash
   git clone https://github.com/kooroshahmadi/Fasta-File-Alignment-and-Normalization-Script.git
   cd Fasta-File-Alignment-and-Normalization-Script
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python fasta_normalization.py input.fasta output.fasta
   ```

---

### 🔬 **Example**
Input (`input.fasta`):
```fasta
>seq1
ATGCCG
>seq2
ATG
>seq3
ATGCCGTT
```

Output (`output.fasta`):
```fasta
>seq1
ATGCCG--
>seq2
ATG-----
>seq3
ATGCCGTT
```

---

### 📌 **Where to Use It?**
This script is ideal for bioinformaticians and researchers working with sequence data in evolutionary, molecular, and genomic studies. It ensures compatibility with tools like **IQ-TREE** and other alignment or phylogenetic software, making it an essential part of the bioinformatics data preprocessing pipeline.
