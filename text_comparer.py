import difflib

class TextComparer:

    def __init__(self, path1, path2):
        file1 = open(path1)
        file2 = open(path2)
        self.text1 = file1.read()
        self.text2 = file2.read()
    def similarity(self):
        normalized1 = self.text1.lower()
        normalized2 = self.text2.lower()
        matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
        return matcher.ratio()

    def line_by_line_similitarity(self, ind1, ind2):
        normalized1 = self.text1[ind1].lower()
        normalized2 = self.text2[ind2].lower()
        matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
        return matcher.ratio()
