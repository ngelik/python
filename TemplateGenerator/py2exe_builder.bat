call d:\DEV\PYTHON\py_dev27\Scripts\activate.bat 
python py2_exe_setup.py py2exe"
rename dist\main.exe TemplateGenerator.exe
copy run1.bat dist
copy run2.bat dist
copy run3.bat dist
copy test1 dist
copy test2 dist
copy test3 dist

echo.&pause&goto:eof