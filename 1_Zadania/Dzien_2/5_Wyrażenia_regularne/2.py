import re

text_to_search = open('text.txt').read()

autor = re.findall(r'autor', text_to_search)
print ("autor:", len(autor))

ciag = re.findall(r'\d%', text_to_search)
print ("ciag cyfr:", len(ciag))

koniec = re.findall(r'\w\.', text_to_search)
print ("znaki z kropka:", len(koniec))

polski = re.findall(r'polski', text_to_search, re.I)
print("polski:", len(polski))