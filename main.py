import requests
import unittest

url = 'https://mach-eight.uc.r.appspot.com/'


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    players = data.get('values', [])

    target_height = 153
    def find_pairs(players, target_height):
        seen ={}
        pairs = []
        
        for player in players:
            height = float(player['h_in'])
            complement = target_height - height

            if complement in seen:
                pairs.append((f'{player['first_name']} {player['last_name']}', seen[complement]))
            
            seen[height] = f'{player['first_name']} {player['last_name']}'
        
        return pairs if pairs else 'No matches found.'
    
    try:
        target_height = float(input("Please enter height in inches: "))
        result = find_pairs(players, target_height)

        if isinstance(result, list):
            for pair in result:
                print(f'-  {pair[0]}    {pair[1]}')
        else:
            print(result)
    except ValueError:
        print("Please enter a valid number")

else:
    print(f'Error obtaining data: {response.status_code}')



class TestNBAPlayerHeightPairs(unittest.TestCase):

    def test_valid_pairs(self):
        players = [
            {'first_name' : 'Player1', 'last_name' : 'One', 'h_in' : '72'},
            {'first_name' : 'Player2', 'last_name' : 'Two', 'h_in' : '68'},
            {'first_name' : 'Player3', 'last_name' : 'Three', 'h_in' : '67'},
        ]
        target_height = 140
        result = find_pairs(players, target_height)
        self.assertEqual(result, [('Player2 Two', 'Player1 One')])

    def test_no_pairs(self):
        players = [
            {'first_name' : 'Player1', 'last_name' : 'One', 'h_in' : '72'},
            {'first_name' : 'Player2', 'last_name' : 'Two', 'h_in' : '68'},
        ]
        target_height = 150
        result = find_pairs(players, target_height)
        self.assertEqual(result, 'No matches found.')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            int('not_a_number')

if __name__ == '__main__':
    unittest.main()