import requests
from requests import session
import re
with session() as c:
    url = 'http://117.239.51.139/autonomous_results/resultdisp.php'
    urll = 'http://117.239.51.139/autonomous_results/resultdisp1.php'
    result = requests.post(urll, data={'rollno': '14751A0526', 'myselection': '32btech_may-17', 'submit': 'submit'})
    req=result.text
    markList = re.findall("<td align='center'>([0-9]+)</td><td align='center'>[A-Z]</td>", req)
    print(markList)

