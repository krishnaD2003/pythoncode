import re

text = '''

Elon musk's phone number is +919991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number +913544-537777 , Modi's phone : +91245-2675362
'''
pattern = '[+]\d{12}|[+]\d{6}-\d{6}|[+]\d{5}-\d{7}'
matches = re.findall(pattern,text)
matches
