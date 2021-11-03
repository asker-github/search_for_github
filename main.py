import os, time
import webbrowser
import requests

def combination(candidate):
    # candidate:list(list) 对list中的每个list都选一个词,然后拼接
    keywords=[]
    if len(candidate)<1:
        raise
    if len(candidate) == 1:
        return candidate[0]
    else:
        tmpcand=[]
        for i in range(1,len(candidate)):
            tmpcand.append(candidate[i])
        tmpkws=combination(tmpcand)
        for kw_i in candidate[0]:
            for kw_j in tmpkws:
                if kw_i =='':
                    if kw_j !='':
                        keywords.append(kw_j)
                elif kw_j =='':
                    keywords.append(kw_i)
                elif kw_j !='':
                    keywords.append(kw_i+'+'+kw_j)

    return keywords
if __name__ == "__main__":
    # candidate=[['','b'],['&','*'],['1',''],['','=']]
    candidate=[['', 'Semantic'],['code'],['clone','duplicate'],['', 'detect'], ['', 'ast','abstract syntax tree','program dependency graph', 'graph'],['', 'machine learning', 'deep learning'] ]
    keywords = combination(candidate)
    print(keywords)
    print(len(keywords))
    print(set(keywords))
    print(len(set(keywords)))
    for w in keywords:
        r = requests.get('https://github.com/search?q='+w)
        print(r.url)
    # url = 'https://github.com/search?q='
    # webbrowser.open(url)
    # time.sleep(3)
