import gzip
import hashlib

try:
    from StringIO import BytesIO
except ImportError:
    from io import BytesIO

try:
    import urllib2 as urllib
except ImportError:
    from urllib import request as urllib


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


def retrieve_compressed_data(url):
    if url:
        request = urllib.Request(url)
        opener = urllib.build_opener()
        response = opener.open(request)
        gz_data = BytesIO(response.read())
        gzipper = gzip.GzipFile(fileobj=gz_data)
        data = gzipper.read()
        return data.decode('utf-8').strip().split('\n')
    return []


def retrieve_data(url):
    if url:
        return urllib.urlopen(url).read().decode('utf-8').strip().split('\n')
    return []
