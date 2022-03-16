import sqlite3
import os
import re

head_path=r"D:\Blogs"
head_link="https://web.archive.org/web"

path_post=r"D:\get_blog_links\posts.db"
path_webpage=r"D:\upload2ArchiveOrg_UsingArchivenow\ArchiveMePlease\webpage.db"

# if not os.path.exists("./not-yet.txt"):
#     open("./not-yet.txt","w",encoding="utf-8").close()

open("./not-yet.txt","w",encoding="utf-8").close()

conn=sqlite3.connect(path_post)
# conn2=sqlite3.connect(path_webpage)
cor=conn.cursor()

name_title_innerLinks=[each for each in cor.execute("select project_name,title,inner_links from pt").fetchall()]

conn2=sqlite3.connect(path_webpage)
cor2=conn2.cursor()
link_versions=[each for each in cor2.execute("select link,versions from wp").fetchall()]

for tup1 in name_title_innerLinks:
    project_name,title,inner_links_s=tup1
    title=title.strip("\"")
    if inner_links_s=="NULL":
        # print("null: ",title)
        continue
    else:
        filepath=r"{}\{}\source\_posts\{}.md".format(head_path,project_name,title)
        print(filepath)
        inner_links=inner_links_s.split(", ")
        # 先长后短
        inner_links=sorted(inner_links,key=len,reverse=True)
        old_news=[]
        for inner_link in inner_links:
            for link,versions in link_versions:
                assert not "," in versions
                if inner_link==link:
                    new_inner_link="{}/{}/{}".format(head_link,versions,link)
                    old_new=(inner_link,"`{}`".format(new_inner_link))
                    old_news.append(old_new)
        if len(old_news)<len(inner_links):
            assert len(old_news)==0
            print("not yet!")
            old_news_s2=str(old_news)
            inner_links_s2=str(inner_links)
            with open("./not-yet.txt","a",encoding="utf-8") as f:
                f.write("Not-yet: "+filepath+"\n")
                f.write("old-news: "+old_news_s2+"\n")
                f.write("inner-links: "+inner_links_s2+"\n")
                f.write("\n\n")
            # continue
        with open(filepath,"r",encoding="utf-8") as f:
            old_lines=f.readlines()
        for idx,old_line in enumerate(old_lines):
            for old,new in old_news:
                if new in old_line:
                    continue
                elif old in old_line:
                    new_line=old_line.replace(old, new)
                    old_line=new_line
            old_lines[idx]=old_line
        new_lines_s="".join(old_lines)
        with open(filepath,"w",encoding="utf-8") as f:
            f.write(new_lines_s)
        print("one done.")


# # # 追加数据库的语法
# #
# cor.execute("attach database ? as db_pt",(path_post,))




# cc=cor.execute("select * from pt inner join wp on inner_links like '%'+link+'%' limit 30").fetchall()

# for idx,c in enumerate(cc,1):
#     print(idx,c)
#
# # print(cor.execute("PRAGMA database_list").fetchall())