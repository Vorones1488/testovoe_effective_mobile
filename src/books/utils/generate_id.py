import os
from itertools import count


class GenerateID:
    count_id = 0

    def __init__(self, id_path="./database/.lost_id"):
        self.id_path = id_path

    def create_id(self):
        """id generation"""
        try:
            with open(self.id_path, "r") as f:
                lost_count = f.readline()
                self.count_id = int(lost_count) + 1
            return self.count_id
        except FileNotFoundError:
            self.count_id += 1
            return self.count_id

    def seve_lost_id(self):
        """Saving the last generated id"""
        with open(self.id_path, "w") as f:
            f.write(str(self.count_id))


generete_id = GenerateID()
