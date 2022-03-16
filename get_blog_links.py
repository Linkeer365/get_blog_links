import os
import re
import sqlite3
import sys

if not os.path.exists("all_links.txt"):
    open("all_links.txt","w").close()


conn=sqlite3.connect("D:/get_blog_links/posts.db")
cur=conn.cursor()

pivot=cur.execute("SELECT name FROM sqlite_master where type='table';").fetchall()
if pivot==[]:
    cur.execute("create table pt (project_name varchar(20),title varchar(20),abbr_num varchar(20),inner_links varchar(20))")
    conn.commit()

abbrlinks=[]
project_name=os.getcwd().split(os.sep)[-3]

innerlinks=[]

omits=[")","]"]

cnt=0
for each in os.listdir("."):
    if each.endswith(".md"):
        cnt+=1
        innerlinks_each_post=[]
        urls_s=""
        title=each.replace(".md", "")
        # sqlite 有个坑，就是有时候会把你的连字符-弄没，比如： let-1-1-3.md >> let.md
        title="\"{}\"".format(title)
        with open("./{}".format(each),"r",encoding="utf-8") as f:
            lines=f.readlines()
        for line in lines:
            if line.startswith("abbrlink: "):
                abbr_num=line.split(" ")[1].strip("\n")
                abbrlink=f"https://linkeer365.github.io/{project_name}/{abbr_num}/"
                abbrlink.replace("'","")
                abbrlinks.append(abbrlink)
                # continue
            # 匹配所有链接的 pattern
            elif "web.archive.org" in line:
                continue
            else:
                pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
                urls=re.findall(pattern,line)
                for idx,url in enumerate(urls):
                    for omit in omits:
                        if omit in url:
                            tail_idx=url.find(omit)
                            url=url[0:tail_idx]
                            urls[idx]=url
                # print("urls:",urls)
                innerlinks.extend(urls)
                innerlinks_each_post.extend(urls)
        urls_s=", ".join(innerlinks_each_post)
        if urls_s=="":
            # print("fuck.")
            urls_s="NULL"
        print()
        item=(project_name,title,abbr_num,urls_s)
        print(item)
        cur.execute("insert into pt (project_name,title,abbr_num,inner_links) values (?,?,?,?)",item)
        conn.commit()
        print("one done.")



pagecnt=cnt//10+1 if cnt%10!=0 else cnt//10

pagelinks=[]

for pagenum in range(1,pagecnt+1):
    if pagenum!=1:
        pagelink1=f"https://linkeer365.github.io/{project_name}/page/{pagenum}/"
        pagelink2=f"https://linkeer365.github.io/{project_name}/archives/page/{pagenum}/"
        pagelinks.append(pagelink1)
        pagelinks.append(pagelink2)

guide_links=[   f"https://linkeer365.github.io/{project_name}/",
                f"https://linkeer365.github.io/{project_name}/archives/",
            ]

links=[]

links.extend(guide_links)
links.extend(pagelinks)
links.extend(abbrlinks)
links.extend(innerlinks)

# print(project_name)
# print(abbrlinks)

links_s="\n".join(links)+"\n"

with open("all_links.txt","w",encoding="utf-8") as f:
    f.write(links_s)

