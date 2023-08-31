# ChAMPswitCH

Project: Tournament Probability Calculator

What: This project is a Tournament Probability Calculator implemented in Python. It calculates the probabilities of winning for each team participating in a tournament based on the number of matches and the team's initial points.

Why: The Tournament Probability Calculator allows organizers and participants to estimate the chances of winning for each team in the tournament. It provides a statistical analysis that can be used for making strategic decisions and predicting outcomes.

How: The project uses Python programming and CSV file handling to read team data and match results. Here's a breakdown of the main steps:

1. Check if the Number of Teams is a Power of 2:
    - The function `is_power_of_two()` checks if the given number of teams is a power of 2.
2. Read Team Data from CSV:
    - The function `read_teams_from_csv()` reads team data from the CSV file and stores it in a dictionary, where the team name is the key and the initial points are the value.
3. Read Match Results from CSV:
    - The function `read_match_results_from_csv()` reads match results from the CSV file and stores them in a list of lists, where each sublist represents the results of a match.
4. Calculate Chances of Winning:
    - The function `calculate_chances_of_winning()` calculates the probabilities of winning for each team.
    - It simulates the tournament `n_times` (number of times) and generates random probabilities for each team.
    - The final probabilities are normalized, taking into account the team's initial points and the total points in the tournament.
5. Main Program:
    - The user is prompted to enter the number of teams, the number of times to run the tournament (n), and the percentage of tournament completion.
    - The program reads team data and match results from the CSV file.
    - It calculates the probabilities of winning for each team and adjusts them to ensure the total probability is 100%.
    - The program then prints the probabilities of winning for each team.

Note: The project assumes that the `teams_data.csv` file contains team information in the format "team_name,team_points". The number of teams should be a power of 2, and the match results in the CSV file should be in the format "team1_points,team2_points,team3_points,..." for each match.

This project demonstrates proficiency in Python programming, CSV file handling, and probability calculations. It showcases skills in data manipulation, statistical analysis, and simulation-based algorithms.
