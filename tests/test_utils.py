import pytest

from genomix import utils


@pytest.mark.parametrize("chromosome,position,reference,alternate,expected", [
    ('1', 10, 'A', 'T', '3bc3103903539cd947ee940d8e75a0e9'),
    ('1', 100, 'A', 'C', '4ca2bf7f5a0ed6f70700d1258ff35125'),
    ('1', 1000, 'A', 'G', '1a0a4091c6d29c0a2470c715237f76d3'),
])
def test_calculate_md5(chromosome, position, reference, alternate, expected):
    assert utils.calculate_variant_md5(chromosome, position, reference, alternate) == expected
