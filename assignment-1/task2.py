import re

def find_all_python(text):
  matches = re.findall(r"\bPython\b", text)
  return matches


text = "hi there my name is python! and i know something Python,maybe later i will do Python something will do"
occu = find_all_python(text)

if occu:
  print(f"Found '{len(occu)}' occurrences of 'Python': {occu}")
else:
  print("No occurrences of 'Python' found in the text.")
