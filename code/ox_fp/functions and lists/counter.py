"""
This module demonstrates the use of the Counter class
from the collections module to count the occurrences
of words in a given input string.
"""

from collections import Counter

N = 5
HILL = """
When the Anglo-saxons invaded Britain it is clear that
they took over many place names as names, without understanding 
their meaning. The evidence is to be found in names like Penhill, 
where Old English hyll was added unnecessarily to a word which 
represented Old Welsh pann, hill. A Penhill in Lancashire developed 
into Pendle Hill, a name which means hill-hill-hill. England also has 
a Torpenhow Hill, or hill-hill-hill-hill."""

data = HILL.split()
HILL = HILL.lower()
numerical_data = Counter(data)
sorted_data = sorted(
    list(numerical_data.keys()),
    key = lambda x : numerical_data[x],
    reverse = True
)

for word in sorted_data[:max(N, len(sorted_data))]:
    print(f"{word}: {numerical_data[word]}")
