# Bioinformatics_Utils
A Python package with simple utilities for working with bioinformatics data files, including FASTQ, FASTA, and BLAST output files.

## 1. FASTQ Filtering
The **filter_fastq()** function filters FASTQ reads based on:
- GC content: minimum and maximum GC percentage.
- Sequence length: minimum and maximum read length.
- Average quality: minimum average Phred quality score (Phred+33).

Filtered reads are saved in the filtered/ directory.

Helper functions in helpers/fastq.py:
- **calculate_gc()**: calculates the GC content of a nucleotide sequence as a percentage.
- **calculate_mean_quality()**: calculates the average Phred quality score of a read using Phred+33 encoding.
- **check_gc()**: checks whether a read's GC content falls within the specified bounds.
- **check_length()**: checks whether a read's length falls within the specified bounds.
- **check_quality()**: checks whether a read's average quality score meets the minimum threshold.

## 2. Multiline FASTA to Oneline Conversion
The **convert_multiline_fasta_to_oneline()** function converts a multiline FASTA file into a FASTA file where each sequence is written on a single line.

Helper functions in helpers/bio_files.py:
- **read_fasta()**: reads sequences and their headers from a FASTA file.
- **write_fasta()**: writes FASTA headers and sequences to an output file, placing each sequence on a single line.

## 3. BLAST Output Parsing
The **parse_blast_output()** function processes a BLAST results file. It extracts the description of the best hit for each query, sorts the descriptions alphabetically, and writes them to an output file, one description per line.

Helper functions in helpers/bio_files.py:
- **read_and_extract_description()**: reads a BLAST output file and extracts the description of the first hit from each query's results table.
- **sort_and_write_descriptions()**: sorts the extracted protein descriptions alphabetically and writes them to an output file, one description per line.