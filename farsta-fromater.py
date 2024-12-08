from Bio import SeqIO  # First install biopython using: pip install biopython

# Define the file path for your FASTA file
input_file = "replace-with-your-FASTA-file"
output_file = "repalce-with-the-output-file-name.fasta"

# Read all sequences
sequences = list(SeqIO.parse(input_file, "fasta"))

# Find the length of the longest sequence
max_length = max(len(record.seq) for record in sequences)

# Pad sequences with "-" to make them the same length as the longest sequence
padded_sequences = []
for record in sequences:
    padded_seq = str(record.seq).ljust(max_length, "-")  # Pad with "-"
    record.seq = padded_seq  # Update the sequence
    padded_sequences.append(record)

# Write padded sequences to a new FASTA file
with open(output_file, "w") as output_fasta:
    SeqIO.write(padded_sequences, output_fasta, "fasta")

print(f"All sequences padded to {max_length} characters.")
print(f"Padded sequences written to: {output_file}")
