"""
Acceptance tests for traffic.py

Make sure that this file is in the same directory as traffic.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
from traffic import IMG_HEIGHT, IMG_WIDTH, load_data

images, labels = load_data("gtsrb-small")


for image in images:
    assert image.shape == (IMG_WIDTH, IMG_HEIGHT, 3)

for label in labels:
    assert label in range(3)
