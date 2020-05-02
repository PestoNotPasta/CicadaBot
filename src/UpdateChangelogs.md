
This is a bot that will be implemented into the CicadaSolvers discord server to assist mods with answering newcomer questions


- To-Do List:
    * [x] Link LP Pages in commands.json 
    * [x] Finish commands 
    * [ ] Release v1.0 of CicadaBot (Today's the day, hopefully)
    * [x] Export chats of #newcomer-questions and #joins 
    * [ ] Run frequency analysis of common words of #newcomer-questions 
    * [ ] Integrate the data with predefined answers and maybe a Neural Net?
    * [ ] Release v1.2/v2.0 (?) of CicadaBot

[Sat May 2, 21:08]

So yesterday I added the bot to Heroku. I'm pretty much done with the v1.0 of the bot, just need mods to invite it. I might not work on it for a while, maybe give people a chance to experiment with it, give suggestions, feedbacks etc. If there is a need for reshaping then maybe I will. Right now, the code is not very dynamic so might fix that...    

- Changes:
	* Finished all commands
	* Added bot to Heroku servers

[Tue Apr 28, 16:54]

Not much done, just exported the chats. Might take a break from programming because I have to focus on school stuff

- Changes:
	* Added exported-chats (#newcomer-questions and #joins) 

[Tue Apr 28, 02:03]

- Changes:
    * Added requirements.txt (currently empty) 
    * Added setup.py (currenly empty)
    * Added pfp.jpg. 
    * Added `Roast` label to [issues](https://github.com/notPyrrh0/CicadaBot/issues) so you can all tell how shit I am at coding .-.
    * Moved most of the files to src/

-Ideas:
    In order to for the bot to answer newcomer questions it needs to know what to look for in order to answer. This most efficient way I can think of is to run the context of any questions against a wordlist of common words and phrases mentioned in #newcomer-questions as well as check when the user joined so that if a veteran user were to joke about using a Caesar cipher, for example, it wouldn't reply. Hopefully #joins has been around for a while. However, writing out hard coded responses is going to take a while so I think I'll release version 1.0 of the bot that will simply return links when commands are called.    

[Mon Apr 27, 01:43] - First commit

- Changes: 
    * Added CicadaBot.py
    * Added commands.json
    * Added `Suggestions` label to [issues](https://github.com/notPyrrh0/CicadaBot/issues) for suggestions of new functionalities you might need.
