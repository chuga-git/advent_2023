import pyperclip
import sys

def cb_to_file(dir, fname):
    fpath = f'{dir}/{fname}'
    
    with open(fpath, 'w') as f:
        lines = pyperclip.paste().split('\n')
        f.writelines(lines)
    
    print(f"File written to {fpath}") 

if __name__ == '__main__':
    dir = sys.argv[1].strip()
    fname = sys.argv[2].strip()
    
    cb_to_file(dir, fname)