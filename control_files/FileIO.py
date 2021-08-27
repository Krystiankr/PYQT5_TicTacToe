import json

class File_Json():
    def __init__(self):
        # Load data from json file
        with open("control_files/data.json") as f:
            self.data = json.load(f)

    # Return dict {"X": 14, "O": 5}
    def return_data(self):
        for element in self.data['Points']:
            print(element, end=' value:')
            print(self.data['Points'][element])
        return self.data['Points']

    def increase_1(self, x_or_o):
        with open("control_files/data.json") as f:
            data = json.load(f)
            print(data)
        data['Points'][x_or_o] += 1

        with open("control_files/data.json", "w") as f:
            json.dump(data, f)

    # Ignore this, is just to initialize the json file
    def save(self):
        data = {}
        data['Points'] = {
            "X": 0,
            "O": 0
        }
        with open("control_files/data.json", "w") as f:
            json.dump(data, f)

