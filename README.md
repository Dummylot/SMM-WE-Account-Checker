# SMM-WE-Account-Checker
This is an account checker for the fan game Super Mario Maker:World Engine i made it by using wireshark. 
If you want to install the game i will let the link





## How does it work 
**Context**


I was playing the game so I decided to login then check how the login API work

it interact with a server http://103.195.100.145:35566/online/user/login
but when I opened the link on the browser i found that i needed a token so i went back to wireshark to see if there is any token. I found one but I'll not share it here it is on the code so you can check it.

**How the code works**
So the code interact with the login API http://103.195.100.145:35566/online/user/login. it just send the infos you wrote with the token needed then it get your info and check if the account exist or no. or if the password is correct or no.

**What does the API takes from your PC/Mobile**
The API takes your ip address like every website or api so when you do a POST or GET request to the API it shows your IP Address. but also it shows you if you are admin in their discord server (here it is : https://discord.gg/enginekingdom ) and also your rank and level uploaded.

## The Game
Here is the game http://103.195.100.145:35566/downloads
download it from here.



I hope you enjoy this tool. please leave a star if you liked.

