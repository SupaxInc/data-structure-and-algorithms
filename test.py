from collections import Counter

def isNStraightHand(hand, W):
    if len(hand) % W != 0:
        return False  # Quick check to ensure it's possible to divide the hand into groups of W

    card_count = Counter(hand)
    sorted_cards = sorted(card_count)  # Sort the keys of the counter

    for card in sorted_cards:
        if card_count[card] > 0:  # If there are cards left to form a group
            count = card_count[card]
            for i in range(W):  # Attempt to form a group starting with 'card'
                if card_count[card + i] < count:
                    return False  # Not enough cards to form a group
                card_count[card + i] -= count

    return True

# Example usage
print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))  # Output: True
