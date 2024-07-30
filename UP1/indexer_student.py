import pickle


class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = []
        self.index = {}
        self.total_msgs = 0
        self.total_words = 0

    def get_total_words(self):
        return self.total_words

    def get_msg_size(self):
        return self.total_msgs

    def get_msg(self, n):
        return self.msgs[n]

    def add_msg(self, m):
        self.msgs.append(m)
        self.total_msgs += 1

    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    def indexing(self, m, l):
        words = m.split()
        for word in words:
            if word not in self.index:
                self.index[word] = []
            self.index[word].append(l)
            self.total_words += 1

    def search(self, term):
        t = []
        if term in self.index:
            line_numbers = self.index[term]
            for line_number in line_numbers:
                t.append((line_number, self.msgs[line_number]))
        return t


class PIndex(Index):
    def __init__(self, name):
        super().__init__(name)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_poems()

    def load_poems(self):
        with open(self.name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    self.add_msg_and_index(line)

    def get_poem(self, p):
        return self.msgs[p]


if __name__ == "__main__":
    sonnets = PIndex("AllSonnets.txt")
    p3 = sonnets.get_poem(3)
    print(p3)
    s_love = sonnets.search("love")
    print(s_love)
