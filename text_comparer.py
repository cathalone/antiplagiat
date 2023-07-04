import difflib
import cheker
import file_utilities


class TextComparer:

    def __init__(self, path1, path2):
        files = file_utilities.read_files(path1, path2, split=False)
        self.text1 = file_utilities.preprocess_code(files[0])
        self.text2 = file_utilities.preprocess_code(files[1])
        self.lines1 = self.text1.split("\n")
        self.lines2 = self.text2.split("\n")

    def similarity(self):
        return cheker.compute_cosine_similarity(self.text1, self.text2)

    def line_by_line_similarity(self, ind1, ind2):
        return cheker.compute_cosine_similarity(self.lines1[ind1], self.lines2[ind2])

    def length(self):
        return len(self.lines1), len(self.lines2)

    def lines(self):
        return self.lines1, self.lines2

