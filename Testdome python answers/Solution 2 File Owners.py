def group_by_owners(files):
    flip = {}
    for k,v in files.items():
        flip.setdefault(v,[]).append(k)        
    return flip
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))