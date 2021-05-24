import os
import shutil
from datetime import datetime

# dir=input("Dir:")
# dir="D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife\source\_posts"

dirs= [  
        # "D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife\source\_posts",
        "D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife2\source\_posts",
        "D:\OneDrive - CUHK-Shenzhen\Linkeer365ColorfulLife3\source\_posts",
        "D:\OneDrive - CUHK-Shenzhen\Linkeer365TinyMoment\source\_posts",

    ]

for dir in dirs:
    dir2=dir+os.sep+"others"

    if not os.path.exists(dir2):
        os.makedirs(dir2)

    ref_date_str="2020-12-10 19:12:00"
    # ref_date_str="2019-10-20 19:12:00"
    datetime_format="%Y-%m-%d %H:%M:%S"

    ref_date_str2="2021-5-10 11:53:52"
    # ref_date_str2="2021-12-10 19:12:00"
    # datetime_format="%Y-%m-%d"
    ref_date_obj=datetime.strptime(ref_date_str,datetime_format)
    ref_date_obj2=datetime.strptime(ref_date_str2,datetime_format)
    print(ref_date_obj)

    for file in os.listdir(dir):
        file_path=f"{dir}{os.sep}{file}"
        if file.endswith(".py") or file.endswith(".txt"):

            new_path=f"{dir2}{os.sep}{file}"
            os.rename(file_path,new_path)
        if os.path.isdir(file_path) and not "others" in file_path:
            print(file_path)
            new_path=f"{dir2}{os.sep}{file}"
            os.rename(file_path,new_path)
        if file.endswith(".md"):
            with open(file_path,"r",encoding='utf-8') as f:
                lines=f.readlines()
            date_line=lines[3]
            if not date_line.startswith("date: "):
                date_line=lines[4]
                # print(file_path)
                # continue
            # format : len("2019-10-20 19:12:00") = 19 , len("date: ") = 6
            date_str=date_line[6:6+19]
            datetime_obj=datetime.strptime(date_str,datetime_format)
            # 把早期的东西筛掉
            if datetime_obj < ref_date_obj or datetime_obj > ref_date_obj2:
                new_path=f"{dir2}{os.sep}{file}"
                os.rename(file_path,new_path)
            # break
    print("done.")