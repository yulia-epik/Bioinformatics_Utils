def calculate_gc(seq: str) -> float:
    """
    Calculates the GC content in the sequence: GC count / sequence length * 100 %

    Arguments:
    seq(str): the sequence to check

    Returns:
    float: the GC content as a percentage
    """
    seq_length = len(seq)
    gc_count = 0
    for i in seq:
        if i == 'G' or i == 'C':
            gc_count += 1
    gc_content = (gc_count / seq_length) * 100
    return(gc_content)

def check_gc(gc_content: float, gc_bounds: float | tuple[float, float]) -> bool:
    """
    Checks whether the GC content is within the specified bounds or not

    Arguments:
    gc_content(float): GC content in the sequence as a percentage  
    gc_bounds(float | tuple[float, float]): the GC bounds specified 
    either by a tuple of two numbers (lower and upper bounds)
    or by a single number (upper bound only)

    Returns:
    bool: True if the GC content satisfies the specified bounds,
    otherwise False.
    """
    type_bounds = type(gc_bounds)
    if type_bounds == int or type_bounds == float:
        return(gc_content <= gc_bounds)
    else:
        lower_gc_bound = gc_bounds[0]
        upper_gc_bound = gc_bounds[1]
        return(lower_gc_bound <= gc_content <= upper_gc_bound)

def check_length(seq: str, length_bounds: int | tuple[int, int]) -> bool:
    """
    Checks whether the sequence length is within the specified bounds or not

    Arguments:
    seq(str): the sequence to check
    length_bounds(int | tuple[int, int]): the length bounds specified 
    either by a tuple of two numbers (lower and upper bounds)
    or by a single number (upper bound only)

    Returns:
    bool: True if the sequence length satisfies the specified bounds,
    otherwise False.
    """
    seq_length = len(seq)
    type_bounds = type(length_bounds)
    if type_bounds == int:
        return(seq_length <= length_bounds)
    else:
        lower_bound = length_bounds[0]
        upper_bound = length_bounds[1]
        return(lower_bound <= seq_length <= upper_bound)

def calculate_mean_quality(quality_string: str) -> float:
    """
    Calculates the mean Phred quality score from a FASTQ quality string

    Arguments:
    quality_string(str): the FASTQ quality string encoded using Phred+33

    Returns:
    float: the mean Phred quality score 
    """
    seq_length = len(quality_string)
    quality_score = 0
    for i in quality_string:
        quality_score += ord(i) - 33
    mean_quality = quality_score / seq_length
    return(mean_quality)

def check_quality(mean_quality: float, quality_threshold: float) -> bool:
    """
    Checks whether the mean Phred quality meets the threshold

    Arguments:
    mean_quality(float): the mean Phred quality score of the sequence
    quality_threshold(float): the minimum acceptable mean Phred quality score.

    Returns:
    bool: True if the mean quality score is greater than or equal to the threshold, otherwise False.
    """
    return(mean_quality >= quality_threshold)