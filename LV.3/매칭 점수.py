class WebPage(object):
    def __init__(self, idx, url, value, outlink):
        self.idx = idx
        self.url = url
        self.value = value
        self.outlink = outlink
        self.matchpoint = value

def solution(word, pages):
    parseUrl = "<meta property=\"og:url\" content=\""
    linkUrl = "<a href=\""
    arrWebPages = []
    
    for idx, page in enumerate(pages):
        idxUrl = page.find(parseUrl)
        Url = ""
        
        for i in range(idxUrl+len(parseUrl), len(page)):
            if page[i] == "\"":
                break
            else:
                Url += page[i]
        
        idx_a = page.find(linkUrl)
        links = []
        
        while idx_a > 0:
            link = ""
            for i in range(idx_a + len(linkUrl), len(page)):
                if page[i] == "\"":
                    break
                else:
                    link += page[i]
            links.append(link)
            
            idx_a = page.find(linkUrl, idx_a + len(linkUrl)+1)
            
        wordCount = 0
        idxWord = page.lower().find(word.lower())
        
        while idxWord > 0:
            match = ""
            for m in range(idxWord, len(page)):
                if page[m].isalpha():
                    match += page[m]
                else:
                    break
            if match.lower() == word.lower():
                wordCount += 1
            idxWord = page.lower().find(word.lower(), idxWord + len(word)+1)
        
        webpage = WebPage(idx, Url, wordCount, links)
        arrWebPages.append(webpage)
        
    for i in range(len(arrWebPages)):
        for j in range(len(arrWebPages)):
            if i == j:
                continue

            if arrWebPages[i].url in arrWebPages[j].outlink:
                arrWebPages[i].matchpoint += (arrWebPages[j].value / len(arrWebPages[j].outlink))
        
    arrWebPages.sort(key=lambda x: (x.matchpoint, -x.idx))

    return arrWebPages[-1].idx

print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
