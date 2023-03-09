def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse = True)
    return scores[0:3]

def high_to_low(scores):
    scores.sort(reverse = True)
    return scores
    
def top_three_when_there_is_a_tie(scores):
    scores.sort(reverse = True)
    
    for score in scores:
        if score == score:
            scores.remove(score)
    return scores[0:3]