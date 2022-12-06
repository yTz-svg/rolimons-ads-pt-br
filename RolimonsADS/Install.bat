echo off


echo Check if you have python installed on your computer, if the program is met with problems, look at read_me


timeout /t 10

echo Install for requests
pip install requests
timeout /t 3
cls



echo Install for discord_webhook
pip install discord_webhook
timeout /t 3
cls


echo Install for json
pip install json
timeout /t 3
cls

echo Install for time
pip install time
timeout /t 3
cls

echo INSTALLATION DONE SUCCESSFULLY
echo Created by yTz#1000
timeout /t 5

exit