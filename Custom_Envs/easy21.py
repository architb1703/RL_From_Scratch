import numpy as np

class Easy21:
    def __init__(self):
        self.state = [None, None]
        self.terminated = False
        self.reset()

    def draw_card(self):
        next_card = np.random.randint(1,11)
        next_color = -1 if np.random.random() < 0.33 else 1     # -1-red, 1-black
        return(next_card*next_color)

    def step(self, action):
        [dealer_sum, player_sum] = self.state
        reward = 0

        if(action==0): #Hit
            next_card = self.draw_card()
            player_sum += next_card
            if(player_sum<1 or player_sum>21):
                reward = -1    
                self.terminated = True
        else:          #Stick
            while(dealer_sum>=1 and dealer_sum<17):
                next_card = self.draw_card()
                dealer_sum += next_card

            if(dealer_sum<1 or dealer_sum>21): #Dealer goes bust
                reward = 1
            else:
                if(dealer_sum>player_sum):
                    reward = -1
                elif(dealer_sum<player_sum):
                    reward = 1

            self.terminated = True

        self.state = [dealer_sum,player_sum]
        return(self.state, reward, self.terminated)
            
    def reset(self):
        dealer_card = np.random.randint(1,11)
        player_card = np.random.randint(1,11)
        self.state = [dealer_card, player_card]
        self.terminated = False
        return [self.state, self.terminated]

