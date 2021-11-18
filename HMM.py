import numpy as np
import matplotlib.pyplot as plt 
from markovchain import MarkovChain

def main(moodArr):
    sunny2sunny = 0.95
    sunny2rainy = 0.05
    rainy2sunny = 0.5
    rainy2rainy = 0.5
    
    sunnyProb = 0.75
    rainyProb = 0.25
    
    sunnyHappy = 0.9
    sunnySad = 0.1
    rainyHappy = 0.2
    rainySad = 0.8
    
    moods = moodArr
    probabilities = []
    weather = []
    
    if moods[0] == 'Happy':
        probabilities.append((sunnyProb * sunnyHappy, 
                              rainyProb * rainyHappy))
    else:
        probabilities.append((sunnyProb * sunnySad,
                              rainyProb * rainySad))
    
    for i in range(1, len(moods)):
        yesterday_sunny, yesterday_rainy = probabilities[-1]
        
        if moods[i] == 'Happy':
            today_sunny = max(yesterday_sunny * sunny2sunny * sunnyHappy,
                              yesterday_rainy * rainy2sunny * sunnyHappy)
            
            today_rainy = max(yesterday_sunny * sunny2rainy * rainyHappy,
                              yesterday_rainy * rainy2rainy * rainyHappy)
            
            probabilities.append((today_sunny, today_rainy))
            
        else:
            today_sunny = max(yesterday_sunny * sunny2sunny * sunnySad, 
                              yesterday_rainy * rainy2sunny * sunnySad)
            
            today_rainy = max(yesterday_sunny * sunny2rainy * rainySad,
                              yesterday_rainy * rainy2rainy * rainySad)
            
            probabilities.append((today_sunny, today_rainy))
    
    for p in probabilities:
        if p[0] > p[1]:
            weather.append('Sunny')
        else:
            weather.append('Rainy')
    
    P = np.array([[0.95, 0.05, 0.9, 0.1],
                  [0.5, 0.5, 0.2, 0.8],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]) # Transition matrix
    mc = MarkovChain(P, ['Sunny', 'Rainy', 'Happy', 'Sad'])
    mc.draw()    
    
    print(weather)

if __name__ == '__main__':
    moodArr = ['Sad', 'Happy', 'Sad', 'Happy', 'Happy', 'Sad']
    
    main(moodArr)
    