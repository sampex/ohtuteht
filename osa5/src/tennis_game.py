class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_even_score(self):
        if self.player1_score >=3:
            return "Deuce"
        else:
            return self.get_score_str(self.player1_score) + "-All"

    def get_win_or_advantage(self):
        leading_player = self.player1_name if self.player1_score > self.player2_score else self.player2_name
        if(abs(self.player1_score - self.player2_score) >= 2):
            return f"Win for {leading_player}"
        
        return f"Advantage {leading_player}"
        
    @staticmethod
    def get_score_str(score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"

    def get_normal_score(self):
        return f"{self.get_score_str(self.player1_score)}-{self.get_score_str(self.player2_score)}"

    def get_score(self):
        if self.player1_score - self.player2_score == 0:
            return self.get_even_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_win_or_advantage()
        
        return self.get_normal_score()
