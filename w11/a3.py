from a2 import check
import psycopg2

dict = {
    'leha': '87016781214',
    'misha': '87054789912',
    'rauan': '87781230912',
    'katlet': '87789871012',
    'noname': '832muofwe33', 
    'noname2': '1234567890'
}

incorrect = {}

for row in dict:
    s = dict[row]
    if s.isdigit() and s[0] != '0' and len(s) == 11:
        check(row, dict[row])
    else:
        incorrect[row] = dict[row]

print(incorrect)    


