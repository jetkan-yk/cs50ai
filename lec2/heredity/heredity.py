import csv
import itertools
import sys

import numpy as np

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    """
    Given a set of people, whom each of them has a random variable T = {True, False},
    represents the person has trait of hearing impairment or not.

    Calculate the probability distribution of each person's random
    variable G = {0, 1, 2}, the number of genes that person has.

    Query X, the probability distribution of G for each person
    Evidence E, the set of people that are assigned to T = {True, False}
    Hidden Y, the set of people that are not assigned to T

    Mathematically,
      P(G | T)
    = α [Σ_(Y=y) P(G, T, y)]

    Hence, the have_trait loop below enumerates all possible cases of T
    for each people that are not assigned to T.

    For example, people = ["Harry", "Ron", "Charlie"] and given that
        T["Harry"] = True, T["Ron"] = False, T["Charlie"] = None (unknown/hidden),
    We need to enumerate these 2 cases:
        T["Harry"] = True, T["Ron"] = False, T["Charlie"] = True
        T["Harry"] = True, T["Ron"] = False, T["Charlie"] = False
    and sum their joint probability as per the enumeration of hidden variables.
    """
    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def has_parent(person, people):
    """
    Returns True if the person has parent information, otherwise False
    Note: father & mother's information are either both present or both absent
    """
    return people[person]["mother"] is not None


def get_gene(person, one_gene, two_genes):
    return (2 if person in two_genes else
            1 if person in one_gene else 0)


def predict_inherit(parent, child):
    """
    Predict the probability of child inherited the gene count from one parent
    Note: parent = {0, 1, 2}, child = {0, 1}
    """
    if parent == 1:
        # Child has 0: P(inherits impairment gene) * P(mutate) + P(inherits normal gene) * P(¬mutate)
        # Child has 1: P(inherits impairment gene) * P(¬mutate) + P(inherits normal gene) * P(mutate)
        # Either of the cases have probability of 0.5
        return 0.5
    elif bool(parent) != bool(child):
        # Parent has gene but child no gene, or vice versa
        # Mutation must have occured
        return PROBS["mutation"]
    else:
        # No mutation
        return 1 - PROBS["mutation"]


def predict_gene(person, people, one_gene, two_genes):
    """
    Predict the probability of a person having the particular gene count
    """
    gene = get_gene(person, one_gene, two_genes)
    # If person has parent information, predict P(G=gene) by enumerating all possible
    # ways of obtaining G=gene number of genes from both parents
    if has_parent(person, people):
        father = people[person]["father"]
        mother = people[person]["mother"]

        # Get father and mother's gene counts from evidence
        f_gene = get_gene(father, one_gene, two_genes)
        m_gene = get_gene(mother, one_gene, two_genes)

        # Loop over all possible ways of obtaining G=gene number of genes
        union = []
        # Each (f, m) tuples represent number of genes inherited from father and mother respectively
        ways = [(f, m) for f in range(2) for m in range(2) if f + m == gene]
        for (f, m) in ways:
            union.append(predict_inherit(f_gene, f) * predict_inherit(m_gene, m))
        # Sum all possible ways of inheriting G=gene number of genes from both parents
        return np.sum(union)

    # Otherwise, return the unconditional probability of P(G=gene)
    else:
        return PROBS["gene"][gene]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    joint = []
    for person in people:
        gene = get_gene(person, one_gene, two_genes)
        trait = person in have_trait
        # P(G, T) = P(G) * P(T | G)
        joint.append(
            predict_gene(person, people, one_gene, two_genes)
            * PROBS["trait"][gene][trait]
        )
    # Calculate joint probability of the population by multiply each individual's probability
    return np.prod(joint)


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person, distribution in probabilities.items():
        if person in two_genes:
            distribution["gene"][2] += p
        elif person in one_gene:
            distribution["gene"][1] += p
        else:
            distribution["gene"][0] += p

        if person in have_trait:
            distribution["trait"][True] += p
        else:
            distribution["trait"][False] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    # Loop each person's probability distribution
    for person in probabilities.values():
        # Loop each random variables (i.e. "gene" and "trait")
        for variable in person.values():
            # Get the sum of probability distribution of the random variable
            denominator = sum(variable.values())
            for outcome, probability in variable.items():
                # Normalize the probability distribution by dividing the sum
                variable[outcome] = probability / denominator


if __name__ == "__main__":
    main()
