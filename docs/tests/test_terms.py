#!/usr/bin/env python

# Read in the terms.yml file to validate each entry. Required are:
# - name: research software engineer
#  definition: Those who regularly use expertise in programming to advance research.
#  url: https://us-rse.org/what-is-an-rse/

import pytest
import yaml
import os

here = os.path.dirname(os.path.abspath(__file__))

def test_terms(tmp_path):
    """test that terms are valid.
    """
    termsfile = os.path.join(os.path.dirname(here), '_data', 'terms.yml')   
    print("Testing loading of the terms.yml file")
    assert os.path.exists(termsfile)

    # Read in the terms
    with open(termsfile, 'r') as stream:
        terms = yaml.safe_load(stream)


    seen = []

    # required fields, and cannot be empty
    requireds = ['name', 'definition', 'url']
    for entry in terms:
        print("Testing %s" % entry)
        for required in requireds:
            print('Looking for %s' % required)
            assert required in entry
       
        # Cannot have double quote in definition
        assert '"' not in entry['definition']

        # Url must be defined
        assert entry['url'].strip() not in ["", None]
     
        # don't start with uppercase
        assert entry['name'][0] == entry['name'][0].lower()

        # cannot have duplicates
        assert entry['name'] not in seen
        seen.append(entry['name'])
