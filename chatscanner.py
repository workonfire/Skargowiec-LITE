from time import sleep


def follow(input_file):
    input_file.seek(0, 2)
    while True:
        log_line = input_file.readline()
        if not log_line:
            sleep(0.1)
            continue
        yield log_line


class Scanner:
    def __init__(self, logs_path, bad_words_file):
        self.searched_words = []
        self.logs_path = logs_path
        self.warning = False
        self.charged_user_nick = None
        try:
            with open(bad_words_file) as searched_words_file:
                for word in searched_words_file.readlines():
                    self.searched_words.append(word.rstrip())
        except FileNotFoundError:
            with open(bad_words_file, 'a') as searched_words_file:
                searched_words_file.write("***")

    def scan(self):
        """
        Launches an infinite chat scanning sequence.
        :return:
        """
        with open(self.logs_path) as log_file:
            for line in follow(log_file):
                if "[CHAT]" and any(string in line for string in self.searched_words):
                    self.warning = True
                    self.charged_user_nick = line.rstrip().split('!')[2].split(' ')[1] if '->' not in line else ''
