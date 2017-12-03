import hashlib


def calculate_variant_md5(chromosome, position, reference, alternate):
    key = '|'.join(list(map(str, [chromosome, position, reference, alternate])))
    return hashlib.md5(key.encode('utf-8')).hexdigest()
