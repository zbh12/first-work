#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import re
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36',}
comments = []
cursor='0'
source='1614232231352'

for i in range(0,999):
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+cursor+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='+source
    html = requests.get(url, headers=headers).content.decode()
    comments = re.compile(r'"content":"(.*?)"', re.S)
    list= re.findall(comments, html)
    with open('comment.txt', 'a', encoding='utf-8') as f:
        for i in list:
            i = i.replace("\n", "")
            f.write(i)
            f.write("\n")
    cursor=re.findall('"last":"(.*?)"',html,re.S)[0].replace("\n","").replace(" ","")
    source=str(int(source)+1)
print("爬取成功")


# In[ ]:




