"""Get passages from www.englishdaily626.com"""

from requests_html import HTMLSession
import re


def get(
    psgloc="cloze_passages", base_url="http://www.englishdaily626.com/{}.php?{:03d}"
):
    texts = []
    urllist = [base_url.format(psgloc, i) for i in range(1, 1000)]
    session = HTMLSession()
    xpath = "body/p/table[1]/tr/td/table[4]/tr[3]/td[2]/table/tr[1]/td[2]//table/tr"
    for url in urllist:
        r = session.get(url)
        tr = r.html.xpath(xpath)
        try:
            para = tr[-1].find("td", first=True).find("p")
            text = "".join([re.sub(r"\n(.+)\n", r" _\1_ ", p.text) for p in para])
        except Exception as e:
            break
        else:
            texts.append(text)
    return texts
