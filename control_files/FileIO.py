import json

class File_Json():
    def __init__(self):

            with open("data.json") as f:
                self.data = json.load(f)

    def load(self):
        for element in self.data['Points']:
            print(element, end=' value:')
            print(self.data['Points'][element])
        return self.data['Points']

    def refresh_data(self, what_XO, count):
        with open("data.json") as f:
            data = json.load(f)
            print(data)
        data['Points'][what_XO] = count

        with open("data.json", "w") as f:
            json.dump(data, f)

    def increase_xo_1(self, what_XO):
        with open("data.json") as f:
            data = json.load(f)
            print(data)
        data['Points'][what_XO] += 1

        with open("data.json", "w") as f:
            json.dump(data, f)

    def save(self):
        data = {}
        data['Points'] = {
            "X": 0,
            "O": 3
        }
        with open("data.json", "w") as f:
            json.dump(data, f)

