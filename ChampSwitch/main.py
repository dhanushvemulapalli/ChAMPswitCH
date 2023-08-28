import csv
import random

def is_power_of_two(num):
    return num & (num - 1) == 0

def read_teams_from_csv(filename):
    teams = {}
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            team_name, team_points = row
            teams[team_name] = int(team_points)
    return teams

def read_match_results_from_csv(filename, n_times):
    match_results = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) != n_times * 2:
                print("Error: The number of match results in the CSV is not as expected.")
                return None
            match_results.append(row)
    return match_results

def calculate_chances_of_winning(teams, n_times, percentage):
    total_points = sum(teams.values())
    chances = {}

    for team, points in teams.items():
        probability = 0
        for _ in range(n_times):
            x = random.uniform(0, 1)
            probability += (points * x)

        probability = (probability / (n_times * total_points))*75/100
        chances[team] = f"{probability*2:.2%}"

    return chances



if __name__ == "__main__":
    filename = "teams_data.csv"
  
    n_teams = int(input("Enter the number of teams (should be a power of 2): "))
    n = int(input("Enter the number of times to run the tournament (n): "))
    percentage = int(input("Enter the percentage of tournament completed "))

    if not is_power_of_two(n_teams):
        print("Error: The number of teams should be a power of 2.")
    else:
      
      teams = read_teams_from_csv(filename)
      if len(teams) != n_teams:
        print(f"Error: The number of teams in the CSV should be {n_teams}.")
      else:
          chances = calculate_chances_of_winning(teams, n, percentage)

          s=0
          for team, probability in chances.items():
            s += float(probability.strip('%')) / 100 

      total_probability = s
      remaining_probability = 1 - total_probability
      print("")
      print ("************** PERCENTAGES OF WINNING **************")
      print("")

      for team, probability in chances.items():
          initial_prob = float(probability.strip('%')) / 100
          new_prob = initial_prob + remaining_probability / n_teams
          print(f"{team} : {new_prob:.2%}")

