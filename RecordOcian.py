
import io

i=3

while i<10001:
    # filescore="Test.txt"
    filename="%d.json" % i
    
    
    with open (filename,'r') as f:                            
        old_change=f.read()
    replacement='"name": "%d",' % i  
    replace1='  "image":"https://greenoceannft.com/nfts/1.jpg",' 
    change=(f'{replacement}\n  {replace1}')
    new_change=old_change.replace(replacement,change)
    i=i+1
    with open (filename,'wt') as f:
        f.write(new_change)
 
     
