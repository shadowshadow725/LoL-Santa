from typing import List, Tuple

def getCreds(filename: str) -> Tuple[List, List]:
    try:
        f = open(filename)
        dat = f.read()
        user = []
        pwd = []
        dat = dat.split('\n')
        for i in dat:
            if dat:
                line = i.split(':')
                user.append(line[0])
                pwd.append(line[1])
        return user, pwd
    except:
        return None, None



