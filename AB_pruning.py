MAX = float('inf')
MIN = -float('inf')
 
def alphaBeta(depth,
              index, 
              Player,
              numList,
              alpha,
              beta):

    if depth == 3:
        return numList[index]
 
    if Player:
      
        optimalValue = MIN
 
        for i in range(0, 2):
             
            value = alphaBeta(depth + 1, index * 2 + i,
                          False, numList, alpha, beta)
            optimalValue = max(optimalValue, value)
            alpha = max(alpha, optimalValue)
 
            if beta <= alpha:
                break
          
        return optimalValue
      
    else:
        
        optimalValue = MAX
 
        for i in range(0, 2):
          
            value = alphaBeta(depth + 1, index * 2 + i,
                            True, numList, alpha, beta)
            optimalValue = min(optimalValue, value)
            beta = min(beta, optimalValue)
 
            if beta <= alpha:
                break
          
        return optimalValue
      
if __name__ == "__main__":
  
    numList = [-20, 2, 3, 7, -1, 1, 12, -12] 
    print("The optimal value is :", alphaBeta(0,
                                              0,
                                              True,
                                              numList,
                                              MIN,
                                              MAX))
     