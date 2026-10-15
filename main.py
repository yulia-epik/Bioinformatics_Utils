# A. FASTQ-фильтратор
import os

from helpers.fastq import (
    calculate_gc,
    calculate_mean_quality,
    check_gc,
    check_length,
    check_quality,
)


def filter_fastq(input_fastq: str, output_fastq: str, gc_bounds = (0, 100), 
length_bounds = (0, 2**32), quality_threshold = 0):
    """
    Filters FASTQ reads by GC content, sequence length, and mean quality

    Arguments:
    input_fastq(str): path to the input FASTQ file
    output_fastq(str): name of the output file. Filtered reads are saved in the
    'filtered' directory, which is created if it does not exist
    gc_bounds (float | tuple[float, float] | default=(0, 100)): the GC bounds specified 
    either by a tuple of two numbers (lower and upper bounds)
    or by a single number (upper bound only)
    length_bounds(int | tuple[int, int] | default=(0, 2**32)): the length bounds specified 
    either by a tuple of two numbers (lower and upper bounds)
    or by a single number (upper bound only)
    quality_threshold (float): the minimum acceptable mean Phred quality score.

    Returns:
    None: filtered reads are written to the output file
    """
    os.makedirs('filtered', exist_ok = True)
    output_path = os.path.join('filtered', output_fastq)
    with open(input_fastq) as file, open(output_path, mode = 'w') as output:
        line = file.readline()
        while line.startswith('@'):
            seq_name = line.strip()
            seq = file.readline().strip()
            separator = file.readline().strip()
            quality_string = file.readline().strip()
            
            gc_content = calculate_gc(seq)
            gc_result = check_gc(gc_content, gc_bounds)
            length_result = check_length(seq, length_bounds)
            mean_quality = calculate_mean_quality(quality_string)
            quality_result = check_quality(mean_quality, quality_threshold)

            if gc_result and length_result and quality_result:
                output.write(seq_name + '\n' + seq + '\n' + separator + '\n' + quality_string + '\n')

            line = file.readline()

# B. Чтение биоинформатических файлов.
# 1) Функция convert_multiline_fasta_to_oneline
from helpers.bio_files import read_fasta, write_fasta


def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str = None):
    """
    Converts a multiline FASTA file into a file with one line per sequence

    Arguments:
        input_fasta(str): path to the input FASTA file
        output_fasta(str = None): path to the output FASTA file. Uses 'output.fasta' by default
    
    Returns:
        None
    """
    if output_fasta is None:
        output_fasta = 'output.fasta'
    records = read_fasta(input_fasta)
    write_fasta(records, output_fasta)