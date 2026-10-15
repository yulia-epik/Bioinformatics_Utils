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