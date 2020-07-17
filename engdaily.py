"""Get passages from www.englishdaily626.com"""

from requests_html import HTMLSession
import re

def get(psgloc, base_url="http://www.englishdaily626.com/{}.php?{:03d}"):
    urllist = [base_url.format(psgloc, i) for i in range(1, 1000)]
    session = HTMLSession()
    xpath = ("body/p/table[1]/tr/td/table[4]/tr[3]/td[2]/table/"
    "tr[1]/td[2]/table/tr")
    for url in urllist:
        r = session.get(url)
        if r.status_code == 404:
            break
        tr = r.html.xpath(xpath)
        para = tr[-1].find('td', first=True).find('p')
        text = "".join([re.sub(r"\n(.+)\n", r" _\1_ ", p.text) for p in para])