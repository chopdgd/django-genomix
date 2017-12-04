import hashlib


def calculate_variant_md5(chromosome, position, reference, alternate):
    """Calculate MD5 hash for a variant

    Args:
        chromosome (str): Chromosome
        position (int): Genomic position
        reference (str): Reference allele
        alternate (str): Alternate allele

    Returns:
        str: MD5 hash for a variant
    """
    key = '|'.join(list(map(str, [chromosome, position, reference, alternate])))
    return hashlib.md5(key.encode('utf-8')).hexdigest()
