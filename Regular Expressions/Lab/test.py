import re

text = """
Ha HaHa
"""

pattern = re.compile(r'\BHa')
match = re.findall(pattern, text)

print(match)