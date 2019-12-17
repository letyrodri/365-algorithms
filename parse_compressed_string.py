## WORK IN PROGRESS

def getElement(i, s):
    ''' Gets the elements of the same kind, digit or not '''
    e = s[i]
    isDigit = e.isdigit()
    j = i

    while((j < len(s)) and (isDigit == (str(s[j]).isdigit()))):
        j += 1

    return s[i:j], isDigit, j

def getValue(j,k,s):
    start = j #s.indexOf('['')
    t = s[k:j:-1]
    
    end = j+t.index(']')
    return start+1, end
    


def parse_compressed_string(s, start, end):
    i = start
    res = ''
    
    while(i < end):
        e, isDigit, j = getElement(i,s)

        if isDigit:
            x,y = getValue(j, end, s)
            print(x,y)
            val = parse_compressed_string(s, x, y)
            print(e)
            for k in range(int(e)):
                print(val)
                res += val
        else:
            if e not in ['[',']']:
                res += e    
        
        i = j

    return res


def test(s):
    print(parse_compressed_string(s,0, len(s)))

test('hola')
test('3[hola]')    

