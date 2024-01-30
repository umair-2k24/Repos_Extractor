from sys import argv
from os import system
from os import remove

if not system('wget --version >nul') == 0:
    print('    install wget!!!')
    exit()
    
try:
    if argv[1] == '-u':
        link = argv[2] + '?tab=repositories'
    elif argv[1] == '-r':
        link = argv[2]
except IndexError:
    print(f'\n    {argv[0]} [argv(-u/-r)] [link]')
    print('\t    -u for user page link')
    print('\t    -r for user repo page link')
    exit()

filename = 'repositories.html'
system('if exist ' + filename + 'del ' + filename)

try:
    remove(filename)
except FileNotFoundError:
    pass

site_domain='https://github.com'
# print(link)

system('wget \"'+link+'\" -O '+filename)

end = link.find('?')
key = link[len(site_domain):end] + '/'

# print(key)

obj = []

# exit()


with open(filename,'r',newline='',encoding='utf-8') as f:
    obj = f.readlines()
    
links = []

for i in obj:
    if '<a href=' in i and key in i:
        i = str(i)
        start = i.find('"')
        end = i.find('"',start+1)
        links.append(i[start:end+1])

f_links = []

for i in links:
    i = str(i)
    start = i.find('/')
    end = i.find('/',start+1)
    end = i.find('/',end+1)
    
    f_links.append(site_domain+i[start:end]+'.git')

my_set = set(f_links)

f_links = list(my_set)

with open('output.txt','w') as file:
    for i in f_links:
        if 'https://github.com.git' not in i:
            file.write(i+'\n')
            print(i)
    
