from typing import List, Tuple

def getCreds(filename: str) -> Tuple[List, List]:
    try:
        f = open(filename)
        dat = f.read()
        lines = []
        dat = dat.split('\n')
        for i in dat:
            if dat:
                line = i.split(':')
                lines.append((line[0], line[1]))
        return user, pwd
    except:
        return None, None



