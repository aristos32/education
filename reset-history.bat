@echo off
cd /d "%~dp0"

git checkout --orphan temp
if errorlevel 1 exit /b 1

git add -A
if errorlevel 1 exit /b 1

git commit -m "Fresh start"
if errorlevel 1 exit /b 1

git branch -D main
if errorlevel 1 exit /b 1

git branch -m main
if errorlevel 1 exit /b 1

git push --force origin main
if errorlevel 1 exit /b 1

git reflog expire --expire=now --all
git gc --prune=now

pause