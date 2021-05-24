import os
import re

cur_dir="D:\get_blog_links"
if os.getcwd()!=cur_dir:
    os.chdir(cur_dir)

with open("./time_info_link.txt","r",encoding="utf-8") as f:
    lines=f.readlines()

names=["notreal_catalan","mutilated_catal","eglStGJNFECCFt0"]
link_heads=["https://twitter.com","https://mobile.twitter.com"]

links=[]

for line in lines:
    for name in names:
        for link_head in link_heads:
            link=f"{link_head}/{name}/status/"
            if link in line:
                head_idx=line.find(link)
                # len("1267093696538767360") = 19
                link=line[head_idx:head_idx+len(link)+19]
                links.append(link)

links_s="\n".join(set(links))

with open("./cc3.txt","w",encoding="utf-8") as f:
    f.write(links_s)