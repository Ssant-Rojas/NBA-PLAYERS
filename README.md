# NBA-PLAYERS

This is a technical test on the height of NBA players where a summation in inches is made and the height of two players added together should give the target height given by the user.

## Required libraries:
requests: To get data from the remote API.
unittest: To perform unit tests.

## Intall

```bash
git clone https://github.com/Ssant-Rojas/NBA-PLAYERS.git
cd NBA-PLAYERS
```

## Libraries

```bash
pip install requests
pip install unittest
```

```bash
python main.py
```

## Data fetching:

The script performs a GET request to the endpoint https://mach-eight.uc.r.appspot.com/.
The obtained data is processed to extract the players.

-- Function find_pairs:

Finds pairs of players whose sum of heights matches the target value.
Uses a dictionary to improve efficiency when searching for complements.
User interaction:

The user enters a height value.
Input is validated and results are presented.
Error handling:

Catches errors such as invalid input or API connection problems.
Unit Tests (test_main.py)

-- test_valid_pairs:
Verifies that the find_pairs function correctly finds valid pairs.

-- test_no_pairs:
Validates the behavior when there are no pairs that meet the target height.

-- test_invalid_input:
Ensures that invalid inputs generate the expected error.
