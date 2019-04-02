import requests
from Seq import Seq

server = "http://rest.ensembl.org"
resource = "/sequence/id"
headers = {"Content-Type": "application/json", "Accept": "application/json"}
r = requests.post(server+resource, headers=headers, data='{ "ids" : ["ENST00000371021.4"] }')


data = r.json()
seq = data[0]['seq']

print('\nThe results of the sequence', data[0]['id'], 'are: ')

# nº of bases in the sequence

count = Seq(seq).len()
print('\n   -The total number of bases is: ', count)

# The number of T's basis

counts = Seq(seq).count_bases()
print('\n    -The total number of T bases is: {}: '.format(Seq(seq).count_bases()['T']))

#  The most popular base and percentage:

maxim = max(counts['T'], counts['A'], counts['C'], counts['G'])
for base in counts:
    if counts[base] == maxim:
        popular_base = base

perc_popular = (counts[popular_base]/count)*100

print('\n   -The most popular base in the sequence is', popular_base, 'and the percentage of it is: ', round(perc_popular, 2), '%')

# The percentage of all the bases:
percentage = Seq(seq).perc()
print('\n   -The percentage of A: {}'.format(percentage[0]))
print('\n   -The percentage of T: {}'.format(percentage[1]))
print('\n   -The percentage of C: {}'.format(percentage[2]))
print('\n   -The percentage of G: {}'.format(percentage[3]))
