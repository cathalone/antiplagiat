if __name__ == "__main__":
    file1 = open("file1")
    s1 = file1.read()
    file2 = open("file2")
    s2 = file2.read()
    print(similarity(s1, s2))