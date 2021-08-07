import os
import random as rd
import re
import sys

DAMPING = 0.85
SAMPLES = 10000
SIGNIFICANT = 0.001  # significant decimal points for iterative algorithm


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.

    Case 1:
        With probability damping_factor, the random surfer should randomly
        choose one of the links from page with equal probability.
    Case 2:
        With probability (1 - damping_factor), the random surfer should
        randomly choose one of all pages in the corpus with equal probability.
    """
    # Initialize probability distribution in Case 2
    probability = {page: (1 - damping_factor) / len(corpus) for page in corpus.keys()}

    neighbors = corpus[page]
    # If page has no outgoing links, chooses randomly among all pages with equal probability
    if not neighbors:
        neighbors = corpus.keys()

    # Calculate the probability distribution in Case 1
    for neighbor in neighbors:
        probability[neighbor] += damping_factor / len(neighbors)

    return probability


def normalize(probability):
    """
    Update `probability` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    denominator = sum(probability.values())
    for outcome in probability.keys():
        probability[outcome] /= denominator


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = list(corpus.keys())
    probability = {page: 0 for page in pages}

    # Surfer starts from a random page
    surfer = rd.choice(pages)
    probability[surfer] += 1
    # Sample (n - 1) times
    for _ in range(n - 1):
        model = transition_model(corpus, surfer, damping_factor)
        surfer = rd.choices(list(model.keys()), list(model.values()))[0]
        probability[surfer] += 1

    normalize(probability)

    return probability


def is_significant(value1, value2):
    """
    Return true if delta > 0.001
    """
    return abs(value1 - value2) > SIGNIFICANT


def links_to(corpus, page):
    """
    Return a list of pages that links to the page
    """
    links = []
    for source, targets in corpus.items():
        if not targets or page in targets:
            links.append(source)
    return links


def predict(probability, corpus, page, damping_factor):
    """
    Return the probability[page] using the iterative algorithm

    Case 1:
        With probability 1 - d, the surfer chose a page at random and ended up on page p.
    Case 2:
        With probability d, the surfer followed a link from a page i to page p.
    """
    N = len(corpus)
    links = links_to(corpus, page)
    sigma = 0
    for link in links:
        numLinks = N if not corpus[link] else len(corpus[link])
        sigma += probability[link] / numLinks

    return (1 - damping_factor) / N + damping_factor * sigma


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = corpus.keys()
    probability = {page: 1 / len(pages) for page in pages}

    while True:
        has_changes = []

        prevIter = probability.copy()
        for page in pages:
            probability[page] = predict(prevIter, corpus, page, damping_factor)
            has_changes.append(is_significant(prevIter[page], probability[page]))

        if all(not change for change in has_changes):
            return probability


if __name__ == "__main__":
    main()
