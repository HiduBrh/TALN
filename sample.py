from Parse import EnglishPosParser

parser = EnglishPosParser()
documents = parser.read_file("eng.train")
print(documents[0].text)

