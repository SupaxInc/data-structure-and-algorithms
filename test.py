def maxProduct(nums):
    if not nums:
        return 0

    # Initialize the max product, min product, and result with the first element.
    # max_product tracks the maximum product ending at the current position.
    # min_product tracks the minimum product ending at the current position.
    # This is necessary because a negative number could turn the minimum product into a maximum.
    max_product = min_product = result = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        # If the current number is negative, swapping max_product and min_product is necessary
        # because multiplying a negative number with the min_product could potentially become the max_product.
        if num < 0:
            max_product, min_product = min_product, max_product

        # Update max_product by comparing the product of num and max_product with num itself.
        # This accounts for scenarios where starting fresh with 'num' is better than extending the current product sequence.
        max_product = max(num, max_product * num)

        # Similarly, update min_product. Even if num is negative, this step ensures that the minimum possible product is tracked.
        min_product = min(num, min_product * num)

        # The result is updated to be the maximum value found so far.
        result = max(result, max_product)

    return result

maxProduct([-1, -2, -3, 4])