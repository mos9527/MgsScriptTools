import sys
from json import dump
if len(sys.argv) != 3:
    print('Usage: python generate_from_charset.py <charset_file> <output_file>')
    sys.exit(1)
CHARSET = open(sys.argv[1],encoding='utf-8').read()
new = {hex(i)[2:].upper().rjust(4,'0'): {'text' : c} for i,c in enumerate(CHARSET)}
dump(new,open(sys.argv[2],'w',encoding='utf-8'),ensure_ascii=False,indent=2)
