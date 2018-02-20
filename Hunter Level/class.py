def camel(word):
        
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(camel('Hello World'))
