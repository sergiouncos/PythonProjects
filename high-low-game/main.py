from data import data
from art import logo, vs
import random


def get_random_candidate():
    """Get data from a random candidate/account"""
    return random.choice(data)


def format_data(candidate):
    """Format candidate data into printable format: name, description and country"""
    name = candidate['name']
    description = candidate['description']
    country = candidate['country']
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right or False if does not"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    score = 0
    games_continues = True
    candidate_a = get_random_candidate()
    candidate_b = get_random_candidate()

    while games_continues:
        candidate_a = candidate_b
        candidate_b = get_random_candidate()

        while candidate_a == candidate_b:
            candidate_b = get_random_candidate()

        print(f"Compare A: {format_data(candidate_a)}.")
        print(vs)
        print(f"Against B: {format_data(candidate_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers_count = candidate_a['follower_count']
        b_followers_count = candidate_b['follower_count']
        is_correct = check_answer(guess, a_followers_count, b_followers_count)
        
        if is_correct:
           score +=1
           print(f"You're right! Current score: {score}.")
        else:
            games_continues = False
            print(f"You're wrong! Final score: {score}.")
   
game()
