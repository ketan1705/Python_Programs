'''import re
result = re.findall(r'.','AV is a largest analytcs community of india')
print(result)'''

'''import re
result = re.findall(r'\w','AV is a largest analytcs community of india')
print(result)'''

'''import re
result = re.findall(r'\w*','AV is a largest analytcs community of india')
print(result)'''

'''import re
result = re.findall(r'\w+','AV is a largest analytcs community of india')
print(result)'''

'''import re
result = re.findall(r'\w\w','AV is a largest analytcs community of india')
print(result)'''

'''import re
result = re.findall(r'\b\w','AV is a largest analytcs community of india')
print(result)'''

'''>>>result=re.findall(r'@\w+','abc.test@gmail.com,xyz@test.in')
>>>print(result)
['@gmail', '@test']'''

'''>>> result=re.findall(r'@\w+.\w+','abc.test@gmail.com,xyz@test.in')
>>> print(result)
['@gmail.com', '@test.in']'''

'''>>> result=re.findall(r'@\w+.(\w+)','abc.test@gmail.com,xyz@test.in')
>>> print(result)
['com', 'in']'''
