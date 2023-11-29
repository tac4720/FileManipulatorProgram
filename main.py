def reverse(inputpath: string, outputpath: string): -> None
    with open(inputpath, 'r') as f:
        read_text = f.read()
    with open(outputpath, 'w') as f:
        f.write(read_text[::-1])
        
def copy(inputpath: string, outputpath: string): -> None
    with open(inputpath, 'r') as f:
        read_text = f.read()
    with open(outputpath, 'w') as f:
        f.write(read_text)

def deplicate(inputpath: string, n: int): -> None
    with open(inputpath, 'r') as f:
        read_text = f.read()
    with open(inputpath, 'a') as f:
        for i in range(n):
            f.write(read_text)
        
    
