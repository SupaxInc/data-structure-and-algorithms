class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Edge case: If its not divisible by group size then theres not enough cards to group
        if len(hand) % groupSize != 0:
            return False
        
        cardsCount = Counter(hand)
        sortedCards = sorted(cardsCount) # Sort the key of the cards by ascending order

        # Greedily select the smallest card first
        for card in sortedCards:
            count = cardsCount[card] # The count is amount of groups the current card needs to start in

            if count > 0:
                # Begin grouping the cards by size of grouPSize
                for i in range(groupSize):
                    # Check if we can add the cards to the group, remember card + i could be card + 0 so it includes current card
                        # The card can't be grouped if it can't start at enough groups.
                        # E.g. card 1 with a count of 2 means it needs to start in 2 groups since its the smallest number.
                        # So if the subsequent card has less than 2 groups counts then it would break the group
                        # as it would not be able to create the same amount of groups as card 1.
                        # It breaks the consecutive nature of each group
                    if cardsCount[card + i] < count:
                        return False
                    # Decrement the entire group count
                    cardsCount[card + i] -= count
            
        return True