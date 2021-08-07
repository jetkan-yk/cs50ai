import os
import random as rd
import re
import sys

DAMPING = 0.85
SAMPLES = 10000
THRESHOLD = 0.001  # pageRank changes must be > threshold to be effective


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
    # If page has no outgoing links, choose randomly from all N pages with equal probability
    if not neighbors:
        neighbors = corpus.keys()

    # Calculate the probability distribution in Case 1
    for neighbor in neighbors:
        probability[neighbor] += damping_factor / len(neighbors)

    return probability


def normalize(sample):
    """
    Return a dictionary such that each probability distribution is
    normalized (i.e., sums to 1, with relative proportions the same).
    """
    total = sum(sample.values())
    for key in sample.keys():
        sample[key] /= total
    return sample


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = corpus.keys()
    sample = {page: 0 for page in pages}

    # Surfer starts sampling from a random page
    surfer = rd.choice(list(pages))
    sample[surfer] += 1
    # Sample (n - 1) times
    for _ in range(n - 1):
        model = transition_model(corpus, surfer, damping_factor)
        surfer = rd.choices(list(model.keys()), list(model.values()), k=1)[0]
        sample[surfer] += 1

    return normalize(sample)


def links_to(corpus, page):
    """
    Return a list of pages that links to the page
    """
    links = []
    for source, targets in corpus.items():
        if not targets or page in targets:
            links.append(source)
    return links


def calculate(pageRank, corpus, page, damping_factor):
    """
    Calculate the pageRank[page] using the iterative algorithm
    """
    N = len(corpus)
    sigma = 0
    for link in links_to(corpus, page):
        # If the source page has no link, assume it can visit all N pages
        numLinks = N if not corpus[link] else len(corpus[link])
        sigma += pageRank[link] / numLinks

    return (1 - damping_factor) / N + damping_factor * sigma


def has_changes(value1, value2):
    """
    Return true if delta > THRESHOLD
    """
    return abs(value1 - value2) > THRESHOLD


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = corpus.keys()
    pageRank = {page: 1 / len(pages) for page in pages}

    while True:
        changelogs = []

        prevRank = pageRank.copy()
        for page in pages:
            pageRank[page] = calculate(prevRank, corpus, page, damping_factor)
            changelogs.append(has_changes(prevRank[page], pageRank[page]))

        # Repeat until no PageRank value changes by more than 0.001
        if all(not change for change in changelogs):
            return pageRank


if __name__ == "__main__":
    main()
