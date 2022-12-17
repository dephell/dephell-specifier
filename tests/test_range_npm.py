# external
import pytest

# project
from dephell_specifier import RangeSpecifier


# https://github.com/npm/node-semver/blob/master/test/index.js
@pytest.mark.parametrize('spec, version', [
    # simple version
    ('1.0.0 - 2.0.0', '1.2.3'),
    ('^1.2.3+build', '1.2.3'),
    ('^1.2.3+build', '1.3.0'),
    ('1.0.0', '1.0.0'),

    # open ranges
    ('>=*', '0.2.4'),
    ('', '1.0.0'),
    ('>1.0.0', '1.1.0'),
    ('<=2.0.0', '2.0.0'),
    ('<=2.0.0', '1.9999.9999'),
    ('<=2.0.0', '0.2.9'),
    ('<2.0.0', '1.9999.9999'),
    ('<2.0.0', '0.2.9'),
    ('>= 1.0.0', '1.0.0'),
    ('>=  1.0.0', '1.0.1'),
    ('>=   1.0.0', '1.1.0'),
    ('> 1.0.0', '1.0.1'),
    ('>  1.0.0', '1.1.0'),
    ('<=   2.0.0', '2.0.0'),
    ('<= 2.0.0', '1.9999.9999'),
    ('<=  2.0.0', '0.2.9'),
    ('<    2.0.0', '1.9999.9999'),
    ('<\t2.0.0', '0.2.9'),
    ('>=0.1.97', '0.1.97'),

    # or's
    ('0.1.20 || 1.2.4', '1.2.4'),
    ('>=0.2.3 || <0.0.1', '0.0.0'),
    ('>=0.2.3 || <0.0.1', '0.2.3'),
    ('>=0.2.3 || <0.0.1', '0.2.4'),
    ('||', '1.3.4'),
    ('1.2.x || 2.x', '2.1.3'),
    ('1.2.x || 2.x', '1.2.3'),

    # stars
    ('2.x.x', '2.1.3'),
    ('1.2.x', '1.2.3'),
    ('x', '1.2.3'),
    ('2.*.*', '2.1.3'),
    ('1.2.*', '1.2.3'),
    ('1.2.* || 2.*', '2.1.3'),
    ('1.2.* || 2.*', '1.2.3'),
    ('*', '1.2.3'),
    # ('2', '2.1.2'),
    # ('2.3', '2.3.1'),

    ('~0.0.1', '0.0.1'),
    ('~0.0.1', '0.0.2'),
    ('~x', '0.0.9'),
    ('~2', '2.0.9'),
    ('~2.4', '2.4.0'),
    ('~2.4', '2.4.5'),
    ('~>3.2.1', '3.2.2'),
    ('~1', '1.2.3'),
    ('~>1', '1.2.3'),
    ('~> 1', '1.2.3'),
    ('~1.0', '1.0.2'),
    ('~ 1.0', '1.0.2'),
    ('~ 1.0.3', '1.0.12'),
    ('~ 1.0.3alpha', '1.0.12'),

    ('>=1', '1.0.0'),
    ('>= 1', '1.0.0'),
    ('<1.2', '1.1.1'),
    ('< 1.2', '1.1.1'),
    ('~v0.5.4-pre', '0.5.5'),
    ('~v0.5.4-pre', '0.5.4'),
    ('=0.7.x', '0.7.2'),
    ('<=0.7.x', '0.7.2'),
    ('>=0.7.x', '0.7.2'),
    ('<=0.7.x', '0.6.2'),

    ('~1.2.1 >=1.2.3', '1.2.3'),
    ('~1.2.1 =1.2.3', '1.2.3'),
    ('~1.2.1 1.2.3', '1.2.3'),
    ('~1.2.1 >=1.2.3 1.2.3', '1.2.3'),
    ('~1.2.1 1.2.3 >=1.2.3', '1.2.3'),
    ('~1.2.1 1.2.3', '1.2.3'),
    ('>=1.2.1 1.2.3', '1.2.3'),
    ('1.2.3 >=1.2.1', '1.2.3'),
    ('>=1.2.3 >=1.2.1', '1.2.3'),
    ('>=1.2.1 >=1.2.3', '1.2.3'),

    ('>=1.2', '1.2.8'),
    ('^1.2.3', '1.8.1'),
    ('^0.1.2', '0.1.2'),
    ('^0.1', '0.1.2'),
    ('^0.0.1', '0.0.1'),
    ('^1.2', '1.4.2'),
    # ('^1.2.3-alpha', '1.2.3-pre'),
    # ('^1.2.0-alpha', '1.2.0-pre'),
    # ('^0.0.1-alpha', '0.0.1-beta'),
    # ('^0.0.1-alpha', '0.0.1'),
    # ('^0.1.1-alpha', '0.1.1-beta'),

    # ('^x', '1.2.3'),
    # ('x - 1.0.0', '0.9.7'),
    # ('x - 1.x', '0.9.7'),
    # ('1.0.0 - x', '1.9.7'),
    # ('1.x - x', '1.9.7'),
    # ('<=7.x', '7.9.9'),
])
def test_included(spec, version):
    assert version in RangeSpecifier(spec)


@pytest.mark.parametrize('spec, version', [
    ['1.0.0 - 2.0.0', '2.2.3'],
    # ['1.2.3+asdf - 2.4.3+asdf', '1.2.3-pre.2'],
    # ['1.2.3+asdf - 2.4.3+asdf', '2.4.3-alpha'],
    ['^1.2.3+build', '2.0.0'],
    ['^1.2.3+build', '1.2.0'],
    ['^1.2.3', '1.2.3-pre'],
    ['^1.2', '1.2.0-pre'],
    # ['>1.2', '1.3.0-beta'],
    # ['<=1.2.3', '1.2.3-beta'],
    ['^1.2.3', '1.2.3-beta'],

    ['1.0.0', '1.0.1'],
    ['>=1.0.0', '0.0.0'],
    ['>=1.0.0', '0.0.1'],
    ['>=1.0.0', '0.1.0'],
    ['>1.0.0', '0.0.1'],
    ['>1.0.0', '0.1.0'],
    ['<=2.0.0', '3.0.0'],
    ['<=2.0.0', '2.9999.9999'],
    ['<=2.0.0', '2.2.9'],
    ['<2.0.0', '2.9999.9999'],
    ['<2.0.0', '2.2.9'],
    ['>=0.1.97', '0.1.93'],
    ['0.1.20 || 1.2.4', '1.2.3'],
    ['>=0.2.3 || <0.0.1', '0.0.3'],
    ['>=0.2.3 || <0.0.1', '0.2.2'],

    ['2.x.x', '3.1.3'],
    ['1.2.x', '1.3.3'],
    ['1.2.x || 2.x', '3.1.3'],
    ['1.2.x || 2.x', '1.1.3'],
    ['2.*.*', '1.1.3'],
    ['2.*.*', '3.1.3'],
    ['1.2.*', '1.3.3'],
    ['1.2.* || 2.*', '3.1.3'],
    ['1.2.* || 2.*', '1.1.3'],
    ['2', '1.1.2'],
    ['2.3', '2.4.1'],

    ['~0.0.1', '0.1.0-alpha'],
    ['~0.0.1', '0.1.0'],
    ['~2.4', '2.5.0'],
    ['~2.4', '2.3.9'],
    ['~>3.2.1', '3.3.2'],
    ['~>3.2.1', '3.2.0'],
    ['~1', '0.2.3'],
    ['~>1', '2.2.3'],
    ['~1.0', '1.1.0'],
    ['<1', '1.0.0'],
    ['>=1.2', '1.1.1'],
    ['~v0.5.4-beta', '0.5.4-alpha'],
    ['=0.7.x', '0.8.2'],
    ['>=0.7.x', '0.6.2'],
    # ['<0.7.x', '0.7.2'],
    ['<1.2.3', '1.2.3-beta'],
    ['=1.2.3', '1.2.3-beta'],
    # ['>1.2', '1.2.8'],
    # ['^0.0.1', '0.0.2-alpha'],
    # ['^0.0.1', '0.0.2'],
    ['^1.2.3', '2.0.0-alpha'],
    ['^1.2.3', '1.2.2'],
    ['^1.2', '1.1.9'],

])
def test_excluded(spec, version):
    assert version not in RangeSpecifier(spec)
