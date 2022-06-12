import os

# 这里必须要加一个单引号，防windows的一些问题...

paths=["./posts.db","./linkeer_links.txt","./inside_links.txt","./not-yet.txt"]

for path2 in paths:
    if os.path.exists(path2):
        os.remove(path2)

origin_dir=os.getcwd()

script_paths=   [   
                    r"D:\Blogs\Linkeer365ColorfulLife\source\_posts\get_blog_links_final.py",
                    r"D:\Blogs\Linkeer365ColorfulLife2\source\_posts\get_blog_links_final.py",
                    r"D:\Blogs\Linkeer365ColorfulLife3\source\_posts\get_blog_links_final.py",
                    r"D:\Blogs\Linkeer365TinyMoment\source\_posts\get_blog_links_final.py",
                    r"D:\Blogs\Linkeer365TinyMoment2\source\_posts\get_blog_links_final.py",
                    r"D:\Blogs\Linkeer365.github.io\source\_posts\get_blog_links_final.py",
                    r"D:\Blogs\Linkeer365BookReview\source\_posts\get_blog_links_final.py",
                ]

script_dirs=   [   
                    r"D:\Blogs\Linkeer365ColorfulLife\source\_posts",
                    r"D:\Blogs\Linkeer365ColorfulLife2\source\_posts",
                    r"D:\Blogs\Linkeer365ColorfulLife3\source\_posts",
                    r"D:\Blogs\Linkeer365TinyMoment\source\_posts",
                    r"D:\Blogs\Linkeer365TinyMoment2\source\_posts",
                    r"D:\Blogs\Linkeer365.github.io\source\_posts",
                    r"D:\Blogs\Linkeer365BookReview\source\_posts",
                ]


paths=[ r"D:\Blogs\Linkeer365ColorfulLife\source\_posts\all_links.txt",
        r"D:\Blogs\Linkeer365ColorfulLife2\source\_posts\all_links.txt",
        r"D:\Blogs\Linkeer365ColorfulLife3\source\_posts\all_links.txt",
        r"D:\Blogs\Linkeer365TinyMoment\source\_posts\all_links.txt",
        r"D:\Blogs\Linkeer365TinyMoment2\source\_posts\all_links.txt",
        r"D:\Blogs\Linkeer365.github.io\source\_posts\all_links.txt",
        r"D:\Blogs\Linkeer365BookReview\source\_posts\all_links.txt",
        ]


# linkeer_path=r"D:\upload2ArchiveOrg_UsingArchivenow\ArchiveMePlease\linkeer_links.txt"

linkeer_path=r".\linkeer_links.txt"
# inside_path=r"D:\upload2ArchiveOrg_UsingArchivenow\ArchiveMePlease\inside_links.txt"
inside_path=r".\inside_links.txt"

inside_path2=r"D:\upload2ArchiveOrg_UsingArchivenow\ArchiveMePlease\inside_links.txt"
linkeer_path2=r"D:\upload2ArchiveOrg_UsingArchivenow\ArchiveMePlease\linkeer_links.txt"

# target_path=r"D:\upload2ArchiveOrg_UsingArchivenow\ArchiveMePlease\outer_links.txt"
# target_path2=r"D:\upload2ArchiveOrg_UsingArchivenow\ArchiveMePlease\outer_links2.txt"

for idx in range(len(script_dirs)):
    script_dir=script_dirs[idx]
    # script_path=script_paths[idx]
    os.chdir(script_dir)
    print(script_dir)
    os.system("python ./get_blog_links_final.py")

links=[]

for path in paths:
    with open(path,"r",encoding="utf-8") as f:
        links.extend([each.strip("\n") for each in f.readlines()])

print(links)

linkeers=[]
insides=[]

for link in links:
    if "linkeer365.github.io" in link:
        linkeers.append(link)
    else:
        insides.append(link)

# index_links=["https://linkeer365.github.io/Linkeer365ColorfulLife3/links/",
#              "https://linkeer365.github.io/Linkeer365ColorfulLife2/links/",
#              "https://linkeer365.github.io/Linkeer365ColorfulLife/links/",
#              "https://linkeer365.github.io/Linkeer365TinyMoment2/links/",
#              "https://linkeer365.github.io/Linkeer365TinyMoment/links/",
#              "https://linkeer365.github.io/Linkeer365BookReview/links/",
#              "https://linkeer365.github.io/links/",
#             ]

# linkeers.extend(index_links)

linkeers_s="\n".join(linkeers)+"\n"
insides_s="\n".join(insides)+"\n"

os.chdir(origin_dir)

with open(linkeer_path,"w",encoding="utf-8") as f:
    f.write(linkeers_s)

with open(inside_path,"w",encoding="utf-8") as f:
    f.write(insides_s)

with open(inside_path2,"w",encoding="utf-8") as f:
    f.write(insides_s)

with open(linkeer_path2,"w",encoding="utf-8") as f:
    f.write(linkeers_s)

# links_s="\n".join(links)+"\n"
#
# with open(target_path,"w",encoding="utf-8") as f:
#     f.write(links_s)
#
# with open(target_path2,"a",encoding="utf-8") as f:
#     f.write(links_s)

print("done.")
# for link in links:
#     print(link)