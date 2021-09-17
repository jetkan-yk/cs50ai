"""
Unit tests for functions in questions.py

These tests will only work if your own version of questions.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import os

from questions import compute_idfs, load_files, no_punctuation, tokenize

DIRECTORY = "corpus"
FILE = "test.txt"
FILE2 = "test2.txt"
TOKENS = "fall sir learn pick sir batman begins 2005".split()
TOKENS2 = "sir learn".split()


def test_load_files():
    files = load_files(DIRECTORY)

    expected = len([file for file in os.listdir(DIRECTORY) if file.endswith(".txt")])

    assert len(files) == expected


def test_no_punctutation():
    assert no_punctuation("") is True
    assert no_punctuation("abc") is True
    assert no_punctuation("0xb") is True

    assert no_punctuation("a?c") is False
    assert no_punctuation("/c") is False
    assert no_punctuation(".") is False


def test_tokenize():
    create_test_file()

    with open(os.path.join(DIRECTORY, FILE)) as f:
        document = f.read()

    tokens = tokenize(document)

    assert tokens == TOKENS


def test_compute_idfs():
    create_test_file()
    create_test_file2

    idfs = compute_idfs({FILE: TOKENS, FILE2: TOKENS2})
    expected = idfs[TOKENS[0]]
    for k, v in idfs.items():
        if k in ["sir", "learn"]:
            assert v == 0
        else:
            assert v == expected


# helper function


def create_test_file():
    with open(os.path.join(DIRECTORY, FILE), "w") as f:
        f.write(
            """
            'Why do we fall sir? So that we can learn to pick ourselves up.'
                                                - Sir Batman Begins (2005)
            """
        )


def create_test_file2():
    with open(os.path.join(DIRECTORY, FILE2), "w") as f:
        f.write(
            """
            Sir sir sIR siR LEARN learn learn LEARN LeARn
            """
        )
