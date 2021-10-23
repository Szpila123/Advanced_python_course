def analyze(votes: dict[int], mandates: int, minority_str: str, proc_threshold: int = 5) -> dict[int]:
    '''Analyze election results in single district using d'Hondt method'''
    if mandates <= 0 or not votes or len(votes) == 0:
        return dict()

    total_votes = sum(votes.values())
    passing = [key for key in votes.keys() if (votes[key]*100)/total_votes >= proc_threshold or minority_str in key]
    seats = dict(zip(passing, [(votes[key], 0) for key in passing]))
    for _ in range(mandates):
        next = max(seats.items(), key=lambda x: x[1][0])[0]
        seats[next] = (votes[next]/(seats[next][1] + 2), seats[next][1] + 1)

    return dict([(key, val[1]) for key, val in seats.items()])

