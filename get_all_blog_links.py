import os

# 这里必须要加一个单引号，防windows的一些问题...

script_paths=   [   
                    r"D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife\source\_posts\get_blog_links.py",
                    r"D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife2\source\_posts\get_blog_links.py",
                    r"D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife3\source\_posts\get_blog_links.py",
                    r"D:\OneDrive - CUHK-Shenzhen\Linkeer365TinyMoment\source\_posts\get_blog_links.py",
                    r"D:\OneDrive - CUHK-Shenzhen\Linkeer365Blog\Linkeer365.github.io\source\_posts\get_blog_links.py",
                ]

script_dirs=   [   
                    r"D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife\source\_posts",
                    r"D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife2\source\_posts",
                    r"D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife3\source\_posts",
                    r"D:\OneDrive - CUHK-Shenzhen\Linkeer365TinyMoment\source\_posts",
                    r"D:\OneDrive - CUHK-Shenzhen\Linkeer365Blog\Linkeer365.github.io\source\_posts",
                ]


paths=[ r"D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife\source\_posts\all_links.txt",
        r"D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife2\source\_posts\all_links.txt",
        r"D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife3\source\_posts\all_links.txt",
        r"D:\OneDrive - CUHK-Shenzhen\Linkeer365TinyMoment\source\_posts\all_links.txt",
        r"D:\OneDrive - CUHK-Shenzhen\Linkeer365Blog\Linkeer365.github.io\source\_posts\all_links.txt",
        ]

target_path=r"D:\upload2ArchiveOrg_UsingArchivenow\ArchiveMePlease\outer_links.txt"
target_path2=r"D:\upload2ArchiveOrg_UsingArchivenow\ArchiveMePlease\outer_links2.txt"

for idx in range(len(script_dirs)):
    script_dir=script_dirs[idx]
    # script_path=script_paths[idx]
    os.chdir(script_dir)
    print(script_dir)
    os.system("python ./get_blog_links.py")

links=[]

for path in paths:
    with open(path,"r",encoding="utf-8") as f:
        links.extend([each.strip("\n") for each in f.readlines()])

print(links)

links_s="\n".join(links)+"\n"

with open(target_path,"w",encoding="utf-8") as f:
    f.write(links_s)

with open(target_path2,"a",encoding="utf-8") as f:
    f.write(links_s)

print("done.")
# for link in links:
#     print(link)