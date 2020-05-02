[Tue Apr 28, 16:54]

Not much done, just exported the chats. Might take a break from programming because I have to focus on school.

- Changes:
	* Added exported-chats (#newcomer-questions and #joins) 

- To-Do List:
    * [x] Link LP Pages in commands.json 
    * [ ] Finish commands (85% Complete)
    * [ ] Release v1.0 of CicadaBot
    * [x] Export chats of #newcomer-questions and #joins 
    * [ ] Run frequency analysis of common words of #newcomer-questions 
    * [ ] Integrate the data with predefined answers and maybe a Neural Net?
    * [ ] Release v1.2/v2.0 (?) of CicadaBot


[Tue Apr 28, 02:03]

- Changes:
    * Added requirements.txt (currently empty) 
    * Added setup.py (currenly empty)
    * Added pfp.jpg. 
    * Added `Roast` label to [issues](https://github.com/notPyrrh0/CicadaBot/issues) so you can all tell how shit I am at coding .-.
    * Moved most of the files to src/

-Ideas:
    In order to for the bot to answer newcomer questions it needs to know what to look for in order to answer. This most efficient way I can think of is to run the context of any questions against a wordlist of common words and phrases mentioned in #newcomer-questions as well as check when the user joined so that if a veteran user were to joke about using a Caesar cipher, for example, it wouldn't reply. Hopefully #joins has been around for a while. However, writing out hard coded responses is going to take a while so I think I'll release version 1.0 of the bot that will simply return links when commands are called.    

- To-Do List:
    * [x] Link LP Pages in commands.json 
    * [ ] Finish commands (85% Complete)
    * [ ] Release v1.0 of CicadaBot
    * [ ] Export chats of #newcomer-questions and #joins 
    * [ ] Run frequency analysis of common words of #newcomer-questions 
    * [ ] Integrate the data with predefined answers and maybe a Neural Net?
    * [ ] Release v1.2/v2.0 (?) of CicadaBot

[Mon Apr 27, 01:43] - First commit

- Changes: 
    * Added CicadaBot.py
    * Added commands.json
    * Added `Suggestions` label to [issues](https://github.com/notPyrrh0/CicadaBot/issues) for suggestions of new functionalities you might need.

- To-Do List:
    * [ ] Add links to LP Pages in commands.json 
    * [ ] Finish commands
