import random


class Game:

    def __init__(self):
        self.user_score = 0
        self.pc_score = 0
        self.game_choices = ['rock', 'paper', 'scissors']

    def pc_choice(self) -> str:
        """Generate computer choise

        Returns:
            str: 'rock, paper, scissors'
        """        
        return random.choice(self.game_choices).lower()
    
    def user_choice(self):
        """Get user choice

        Returns:
            str: 'rock, paper, scissors'
        """ 

        try:
            print('-----------------------------------------')
            print('Rock, Paper,  Scissors')

            user_input =  str(input('Enter your choise: '))

            if user_input not in self.game_choices:
                print(f'Please Enter valid data. {",".join(self.game_choices)}')
                return self.user_choice()
            
            return user_input.lower()
        
        except ValueError:
            print('Please Enter valid data.')

        return self.user_choice()

    def decide_winner(self, user_choice:str, pc_choice:str) -> bool:
        """_summary_

        Args:
            user_choice (str)
            pc_choice (str)

        Returns:
            boolian: True -> continue game
        """
 
        if pc_choice == user_choice:
            print("It's a Tie!")
            return True

        winning_rules = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }

        if winning_rules[pc_choice] == user_choice:
            self.increment_score('pc')
        else:
            self.increment_score('user')
            
        print(f'user {user_choice}, pc {pc_choice}')
        return True 
                
    def show_players_score(self):
        print(f'user {self.user_score}, pc {self.pc_score}')
        
    def increment_score(self, player:str):

        if player == 'user':
            self.user_score += 1

        elif player == 'pc':
            self.pc_score += 1
        
        else:
            raise ValueError('Invalid player...')

    def play(self) -> bool:
        """start playing game

        Returns:
            boolian: False -> end game, True -> continue game
        """

        if self.is_max_score():
            return False

        pc = self.pc_choice()
        user = self.user_choice()

        result = self.decide_winner(user_choice=user, pc_choice=pc)
        self.show_players_score()

        return result

    def reset_scores(self):
        self.user_score = 0
        self.pc_score = 0

    def is_max_score(self) -> bool:

        if self.pc_score == 3:
            print('pc win...')
            return True
        
        if self.user_score == 3:
            print('user win...')
            return True
        
        return False


def main():
    game = Game()

    while True:

        result_game = game.play()

        if not result_game:

            user_input = input('Do you want play again? enter any key to play agein. q/Q for exit.').strip().lower()

            if user_input == 'q':
                break
            
            game.reset_scores()


if __name__ == '__main__':
    main()
    