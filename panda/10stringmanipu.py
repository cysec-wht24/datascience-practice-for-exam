import re
import numpy as np
import pandas as pd

# ── a) STRING BUILT-IN METHODS ───────────────────────────────────
val = 'a,b, guido'

print(val.split(','))                              # ['a', 'b', ' guido']
pieces = [x.strip() for x in val.split(',')]       # strip whitespace
print('::'.join(pieces))                           # 'a::b::guido'

print('guido' in val)                              # True  (substring check)
print(val.find(':'))                               # -1    (not found, no error)
print(val.count(','))                              # 2
print(val.replace(',', '::'))                      # 'a::b:: guido'

# ── b) REGULAR EXPRESSIONS ───────────────────────────────────────
text = "foo bar\t baz \tqux"
print(re.split('\s+', text))                       # ['foo', 'bar', 'baz', 'qux']

# find all emails
text = "Dave dave@google.com\nSteve steve@gmail.com\nRob rob@gmail.com"
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE)

print(regex.findall(text))                         # all emails
print(regex.search(text))                          # first match object
print(regex.match(text))                           # None (no match at start)

# ── c) PANDAS VECTORIZED STRING METHODS ──────────────────────────
data = pd.Series({
    'Dave': 'dave@google.com',
    'Steve': 'steve@gmail.com',
    'Rob': 'rob@gmail.com',
    'Wes': np.nan
})

print(data.isnull())                               # Wes = True
print(data.str.contains('gmail'))                  # Rob, Steve = True, Wes = NaN
print(data.str.findall(pattern, flags=re.IGNORECASE))  # extract email parts
print(data.str.match(pattern, flags=re.IGNORECASE))    # True/False per row
print(data.str[:5])                                # slice first 5 chars

# 3 concepts:

# | Section          | Key methods                                      |
# |------------------|--------------------------------------------------|
# | String built-ins | split, strip, join, find, count, replace         |
# | Regex (re)       | findall, search, match, split, compile           |
# | Pandas str       | str.contains, str.findall, str.match, str[:n]    |