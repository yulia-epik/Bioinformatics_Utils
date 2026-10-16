def read_fasta(input_fasta: str) -> list:
    """
    Reads a FASTA file and combines multiline sequences into single lines

    Arguments:
        input_fasta(str): path to the input FASTA file

    Returns:
        list: a list of tuples, where each tuple contains a sequence header
        and the corresponding sequence as a single string
    """
    records = []
    with open(input_fasta) as file:
        header = ''
        sequence = []
        for line in file:
            if line.startswith('>'):
                if header:
                    sample_fasta = (header, ''.join(sequence))
                    records.append(sample_fasta)
                    sequence.clear()
                header = line.strip()
            else:
                sequence.append(line.strip())

        sample_fasta = (header, ''.join(sequence))
        records.append(sample_fasta)
    return(records)

def write_fasta(records: list, output_fasta: str):
    """
    Writes FASTA records to a file

    Arguments:
        records(list): a list of tuples, where each tuple contains a sequence header
        and the corresponding sequence as a single string
        output_fasta(str): path to the output FASTA file
    
    Returns:
        None
    """
    with open(output_fasta, mode = 'w') as output:
        for i in records:
            header = i[0]
            seq = i[1]
            output.write(header + '\n' + seq + '\n')

import re

def read_and_extract_description(input_file: str) -> list:
    """
    Reads BLAST output file and extracts the first protein description from each BLAST results table

    Arguments:
        input_file(str): path to the input BLAST output file

    Returns:
        list: a list of protein descriptions, one for each query
    """
    protein_descriptions = []
    with open(input_file) as file:
        inside_results = False
        for line in file:

            if line.startswith('Sequences producing significant alignments:'):
                inside_results = True
                continue
            if not inside_results:
                continue
            if line.strip().startswith('Scientific'):
                continue
            if line.strip().startswith('Description'):
                continue

            columns = re.split(r"\s{2,}", line.strip())
            description = columns[0]
            protein_descriptions.append(description)

            inside_results = False

        return(protein_descriptions)

def sort_and_write_descriptions(protein_descriptions: list, output_file: str):
    """
    Sorts protein descriptions alphabetically and writes them to an output file, one description per line

    Arguments:
    protein_descriptions(list): a list of protein descriptions, one for each query 
    output_file(str): path to the output file

    Returns:
    None
    """
    protein_descriptions.sort()
    with open(output_file, mode = 'w') as output:
        for description in protein_descriptions:
            output.write(description + '\n')