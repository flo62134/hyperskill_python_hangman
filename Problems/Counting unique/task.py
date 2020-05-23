# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'
domains_list = Belov
domains_list.extend(Smith)
domains_list.extend(Sarada)
domains_set = set(domains_list)
print(len(domains_set))
