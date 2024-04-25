class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_triplet = [0, 0, 0]

        for triplet in triplets:
            # Local optimal choice: Do not select a triplet that has any higher value than target values
                # A higher value prevents us from ever reaching the target
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                # Greedily choose the highest values across all triplets as it eventually gives us target
                    # Since a higher value triplet is filtered out, we'll only maerge triplets that are valid
                max_triplet[0] = max(max_triplet[0], triplet[0])
                max_triplet[1] = max(max_triplet[1], triplet[1])
                max_triplet[2] = max(max_triplet[2], triplet[2])

                # Early return when we find the value
                if max_triplet == target:
                    return True
        
        return False