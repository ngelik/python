RM dist\*.*
echo Y | RMDIR dist\logs /S
echo Y | RMDIR build /S

copy logging.yaml dist
mkdir dist\logs