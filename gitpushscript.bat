@echo off
git status
pause
set /p commitMsg=Enter Commit Message: 
git add .
git commit -m "%commitMsg%"
@REM change the branch name 'main' to any other branch.
git push origin main
pause
