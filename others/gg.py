import os
import shutil
from datetime import datetime
import re

# dir=input("Dir:")
# dir="D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife\source\_posts"

dirs=   [  
            "D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife\source\_posts",
            "D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife2\source\_posts",
            "D:\OneDrive - CUHK-Shenzhen\Linkeer365TinyMoment\source\_posts",
        ]

for dir in dirs:
    for file in os.listdir(dir):
        file_path=f"{dir}{os.sep}{file}"
        if file.endswith(".md"):
            with open(file_path,"r",encoding='utf-8') as f:
                lines=f.readlines()
            newlines=[]
            flag=0
            for idx,line in enumerate(lines):
                if "web.archive.org" in line and "lgulife" in line:
                    if "http:" in line:
                        line=line.replace("http:","https:")
                    print(line)
                    if not "sort" in line:
                        url=re.findall("https://web.archive.org/web/\d{14}/https://www.lgulife.com/bbs/post/\d+/?",line)
                        if url==[]:
                            url=re.findall("https://web.archive.org/web/\d{14}/https://www.lgulife.com/news/\d+/?",line)
                        url=url[0]
                    else:
                        line=line.replace("#all_threads","")
                        
                        url=re.findall("https://web.archive.org/web/\d{14}/.*//www.lgulife.com/bbs/post/\d+/?",line)[0]
                        pagenum=re.findall("sort_option=&page=(\d)",line)[0]
                        url=url+"?sort_option=&page="+pagenum
                    quote_url=f"`{url}`"
                    newline=line.replace(url,quote_url)
                    newlines.append(newline)
                    flag=1
                elif "web.archive.org" in line and not "lgulife" in line:
                    begin=line.find("web.archive.org")
                    newline=line[begin+43:]
                    newlines.append(newline)
                    flag=1
                else:
                    newlines.append(line)
            if flag==1:
                newlines_s="".join(newlines)
                with open(file_path,"w",encoding="utf-8") as f:
                    f.write(newlines_s)
            print("one done.")

print("done.")