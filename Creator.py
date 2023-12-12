import re
i=3
q=2


lineses=0
with open('Release_squid_fixx.json') as f:
    lines = f.readlines()
    

str = '"name": "2",'
pattern = re.compile(re.escape(str))
with open('1.json', 'w') as f:
    for line in lines:
        lineses+=1
        result = pattern.search(line)
        if result is None:
            f.write(line)
        else:
            lineses-=6
            print(lineses)  
            break  
             
# прочитаем файл построчно
with open('1.json', 'r') as f:
    lines = f.readlines()

# запишем файл построчно убрав последние 2 строчки
with open('1.json', 'w') as f:
    f.writelines(lines[:-2])
with open('1.json', 'r') as f:
    lines = f.readlines()
    # # запишем файл построчно убрав последние 2 строчки
with open('1.json', 'w') as f:
    f.writelines(lines[5:])
with open ("1.json",'r') as f:                            
    old_change=f.read()
new_change=old_change.replace("]","] }")
with open ("1.json",'wt') as f:
    f.write(new_change)


while i<10002:
    with open('Release_squid_fixx.json') as f:
        lines = f.readlines()[lineses:]
    filename="%d.json" % q    
    str = '"name": "%d",' % i
    pattern = re.compile(re.escape(str))
    with open(filename, 'w') as f:
        for line in lines:
            lineses+=1
            result = pattern.search(line)
            if result is None:
                f.write(line)
            else:
                lineses-=7
                break 
    # прочитаем файл построчно
    with open(filename, 'r') as f:
        lines = f.readlines()
    # # запишем файл построчно убрав последние 2 строчки
    with open(filename, 'w') as f:
        f.writelines(lines[:-2])

    with open(filename, 'r') as f:
        lines = f.readlines()
    # # запишем файл построчно убрав последние 2 строчки
    with open(filename, 'w') as f:
        f.writelines(lines[5:])
    
    with open (filename,'r') as f:                            
        old_change=f.read()
    new_change=old_change.replace("]","] }")
    with open (filename,'wt') as f:
        f.write(new_change)            
    i+=1
    q+=1
         

        