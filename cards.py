def maxScore(cardPoints, k):
    """
    :type cardPoints: List[int]
    :type k: int
    :rtype: int
    """
    if k > len(cardPoints):
        return
        
    if k == len(cardPoints):
        return sum(cardPoints)
    
    def take_cards(cardPoints, i, k, points):
        
        if i == 0:
            return points
        
        # go left
        max_left_sum = take_cards(cardPoints[k-i+1:], i-1, k, points+cardPoints[k-i])
        
        # go right
        max_right_sum = take_cards(cardPoints[:-1], i-1, k, points+cardPoints[-1])
        
        # take one from the left
        return max(max_left_sum, max_right_sum)
        

    
    return take_cards(cardPoints, k, k, 0)

data = [1,2,3,4,5,6,1]
k = 3
print(maxScore(data, k))
