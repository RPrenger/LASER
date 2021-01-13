import argparse
import gzip
import re
from shutil import copyfile
import os

def fix(filename):
    f = gzip.open(filename, 'rt')
    o = gzip.open("/datadrive/tmp.tsv.gz", 'wt')
    final_line = ""
    try:
        for i, line in enumerate(f):
            if line[-1] == '\n':
                line = line[:-1]
            z = re.match("^[a-z][a-z]-[a-z][a-z]/[a-z][a-z]", line)
            if not z:
                assert(i > 0)
                final_line = final_line + line
            else:
                if i > 0:
                    o.write(final_line+'\n')
                final_line = line
        assert(len(final_line) > 4)
        o.write(final_line+'\n')
        f.close()
        o.close()
        copyfile("/datadrive/tmp.tsv.gz", filename)
    except:
        f.close()
        o.close()
        os.remove(filename)
    os.remove("/datadrive/tmp.tsv.gz")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="fix the files")
    parser.add_argument('--filename', type=str)
    args = parser.parse_args()
    fix(args.filename)
