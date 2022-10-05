import json
import os.path

class JSONUtil():
    def __init__(self):
        self.data = {}
        self.path = ""

    def createEmptyFile(self, path):
        self.path = path
        self.data = {}

        with open(self.path, "w") as output_file:
            json.dump(self.data, output_file)

    def importData(self, path):
        self.path = path

        with open(self.path, "r") as output_file:
            self.data = json.load(output_file)

        return self.data

    def updateFile(self, path, data):
        self.path = path
        self.data = data

        with open(self.path, "w") as output_file:
            json.dump(self.data, output_file)
