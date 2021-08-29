"""
Acceptance tests for my_parser.py

Make sure that this file is in the same directory as my_parser.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import os

import pytest

from my_parser import np_chunk, parser, preprocess


@pytest.mark.parametrize("execution", range(1, 11))
def test_parser(execution):
    with open(os.path.join("sentences", f"{execution}.txt")) as f:
        s = f.read()
    s = preprocess(s)
    try:
        trees = list(parser.parse(s))
        print()
        for tree in trees:
            tree.pretty_print()
            print("Noun Phrase Chunks")
            for np in np_chunk(tree):
                print(" ".join(np.flatten()))
    except ValueError as e:
        assert False, e
    if not trees:
        assert False, "Could not parse sentence."
