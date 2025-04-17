from collections import Counter

def find_winner(votes):
    """
    Args:
     votes(list_str)
    Returns:
     str
    """
    max_vote = 0
    
    winners = {}
    
    lookup = Counter(votes)

    print(lookup)

    max_vote = max(lookup.values())

    print("The max vote is ", max_vote)
    
    winners = [x for x, vote in lookup.items() if vote == max_vote]

    print("the list is ", winners)
    print("the winner is ", min(winners))
    
    return min(winners) if winners else ""

print("Th winner is ", find_winner( ["sam", "john", "jamie", "sam"]))