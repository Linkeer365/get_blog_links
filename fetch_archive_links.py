import sqlite3
from datetime import datetime

webpage_path=r"D:\upload2ArchiveOrg_UsingArchivenow\ArchiveMePlease\webpage.db"
webpage_conn=sqlite3.connect(webpage_path)

post_path=r"D:\get_blog_links\posts.db"
post_conn=sqlite3.connect(post_path)

webpage_cursor=webpage_conn.cursor()
post_cursor=post_conn.cursor()

link_versions=webpage_cursor.execute("select link,versions from wp where link like \"%{}%\"".format("linkeer365.github.io")).fetchall()

name_title_abbrs=post_cursor.execute("select project_name,title,abbr_num from pt").fetchall()

name_title_versions=[]

for name,title,abbr in name_title_abbrs:
    for link,versions in link_versions:
        tail=link.split("/")[-2]
        if abbr == tail:
            pack=(name,title,versions)
            name_title_versions.append(pack)
            break

index_file_path_patt="D://Blogs//{}//source//_posts//links//index.md"
post_file_path_patt="D://Blogs//{}//source//_posts//{}.md"

new_packs=[]
for name,title,versions in name_title_versions:
    title=title.replace("\"","")
    pack=name,title,versions
    post_file_path=post_file_path_patt.format(name,title)
    # print(post_file_path)
    with open(post_file_path,"r",encoding="utf-8") as f:
        lines=f.readlines()
    for line in lines:
        if line.startswith("date: "):
            date=line[len("date: "):].strip("\n")
            new_pack=(*pack,date)
            new_packs.append(new_pack)

new_packs=sorted(new_packs,key=lambda x:datetime.strptime(x[3], "%Y-%m-%d %H:%M:%S"),reverse=True)

with open(r"D:\get_blog_links\needing_words.txt","r",encoding="utf-8") as f:
    needing_lines=f.readlines()


archive_lines=[]

path_lines_dict=dict()

for name,title,versions,date in new_packs:
    index_file_path=index_file_path_patt.format(name)
    archive_line="| {} | {} | `{}` |\n".format(date,title,versions)
    archive_lines.append(archive_line)
    path_lines_dict[index_file_path]=archive_lines

for path,lines in path_lines_dict.items():
    newlines=[]
    newlines=needing_lines+lines
    newlines_s="".join(newlines)
    with open(path,"w",encoding="utf-8") as f:
        f.write(newlines_s)
    print("one done.")

print("done.")

# print("one done.")

#     with open(index_file_path,"r",encoding="utf-8") as f:
#         lines=f.readlines()
#     print(lines)
#     pivot_line="Linkeer365BookReview: https://linkeer365.github.io/Linkeer365BookReview"
#     print(index_file_path)
#     try:
#         pivot_idx=lines.index(pivot_line)
#     except ValueError:
#         pivot_idx=lines.index(pivot_line+"\n")

#     needing_lines=lines[0:pivot_idx+1]
#     assert needing_lines[-1] == pivot_line
#     desc_words="\n顺便整理了archive下来的链接，这样只要点进主页就可以查看了：\n"
#     needing_lines_s="".join(needing_lines)+desc_words+"\n"
#     with open(index_file_path,"w",encoding="utf-8") as f:
#         f.write(needing_lines_s)

# for name,title,versions,date in new_packs:
#     index_file_path=index_file_path_patt.format(name)
#     archive_line="| {} | {} | {} |\n".format(date,title,versions)
#     with open(index_file_path,"a",encoding="utf-8") as f:
#         f.write(archive_line)
#         print("one written.")

