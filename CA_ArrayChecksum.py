len_array = int(raw_input())

line = raw_input()
array = map(float, line.split())
result = 0
seed = 113
modulo = 10000007

for x in array:
    result = ((result + x)*seed) % modulo 
print int(result),