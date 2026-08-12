from communication_evaluation.fluency_checker import fluency
from communication_evaluation.grammar_checker import grammar
from communication_evaluation.vocabulary_checker import vocabulary
from communication_evaluation.clarity_checker import clarity
from communication_evaluation.filler_detector import filler
from communication_evaluation.structure_checker import structure
from communication_evaluation.score_normalizer import normalize

def evaluate(answer):

    f1 = fluency(answer)
    f2 = grammar(answer)
    f3 = vocabulary(answer)
    f4 = clarity(answer)
    f5 = filler(answer)
    f6 = structure(answer)

    total = f1 + f2 + f3 + f4 + f5 + f6

    return {
        "Fluency": f1,
        "Grammar": f2,
        "Vocabulary": f3,
        "Clarity": f4,
        "Filler": f5,
        "Structure": f6,
        "Raw Score": total,
        "Communication Score": normalize(total, 110)
    }