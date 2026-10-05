hello everyone
Microsoft Windows [Version 10.0.26200.9457]
(c) Microsoft Corporation. All rights reserved.

C:\Users\asus> cd ..

C:\Users>cd ..

C:\>cd D:
D:\

C:\>cd /d D:

D:\>mkdir Project

D:\>cd Project

D:\Project>git version
git version 2.55.0.windows.5

D:\Project>cd . > file.py

D:\Project>git init
Reinitialized existing Git repository in D:/Project/.git/

D:\Project> git add file.py

D:\Project> git config --global user.name "Rozhan"

D:\Project> git config --global user.email "jamebozorgrozhan@gmail.com"

D:\Project>git add file.py

D:\Project> git commit -m "empty file created"
[master (root-commit) 6799f80] empty file created
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 file.py

D:\Project> notepad file.py

D:\Project> git add file.py

D:\Project>git commit -m "file changed"
[master 894d2f4] file changed
 1 file changed, 1 insertion(+)

D:\Project>git branch
* master

D:\Project>git remote add origin https://github.com/rozhanjamebozorg/Programming.HSE.git

D:\Project>git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/rozhanjamebozorg/Programming.HSE.git'

D:\Project>git remote -v
origin  https://github.com/rozhanjamebozorg/Programming.HSE.git (fetch)
origin  https://github.com/rozhanjamebozorg/Programming.HSE.git (push)

D:\Project>git branch.
git: 'branch.' is not a git command. See 'git --help'.

The most similar command is
        branch

D:\Project>git branch
* master

D:\Project>git branch -M main

D:\Project>git branch
* main

D:\Project>git push -u origin main
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (6/6), 443 bytes | 443.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/rozhanjamebozorg/Programming.HSE.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

D:\Project>