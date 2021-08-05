from heredity import *


def predict_family(n):
    people = load_data(f"data/family{n}.csv")

    probabilities = {
        person: {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}}
        for person in people
    }

    names = set(people)
    for have_trait in powerset(names):
        fails_evidence = any(
            (
                people[person]["trait"] is not None
                and people[person]["trait"] != (person in have_trait)
            )
            for person in names
        )
        if fails_evidence:
            continue

        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    normalize(probabilities)

    return probabilities


def compare(predicted, expected):
    for kPerson, vPerson in predicted.items():
        for kVariable, vVariable in vPerson.items():
            for outcome, probability in vVariable.items():
                assert expected[kPerson][kVariable][outcome] == round(probability, 4)
