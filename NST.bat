@echo off
set max_iter=%1
set content_weight=%2
set reg_weight=%3
set datarootA="%USERPROFILE%\myproject\venv\DST\example\content.jpg"
set datarootB="%USERPROFILE%\myproject\venv\DST\example\style.jpg"
"%USERPROFILE%\myproject\venv\Scripts\python.exe" "%USERPROFILE%\myproject\venv\DST\NBB\main.py" --datarootA %datarootA% --datarootB %datarootB% --fast
"%USERPROFILE%\myproject\venv\Scripts\python.exe" "%USERPROFILE%\myproject\venv\DST\cleanpoints.py"
"%USERPROFILE%\myproject\venv\Scripts\python.exe" "%USERPROFILE%\myproject\venv\DST\main.py" %max_iter% %content_weight% %reg_weight%
pause