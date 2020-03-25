<img src="./UI workflow.png" width="700" >

### <a name="install"></a>Installing 

**Install *COVID-19 Tracking System***:
1. Download the "Chess Game" zip file.
2. Unzip the zipfile


### <a name="running"></a> Running 

#### Important Note (before runing): 
1. Go to "ChessEng.py"
2. Find the following line:
```
self.engine = chess.engine.SimpleEngine.popen_uci("/Users/dongchenye/Desktop/Senior Design/Chess Game/stockfish-11-64")
```
3. change the path into your own path:
```
self.engine = chess.engine.SimpleEngine.popen_uci(""your own path"/Chess Game/stockfish-11-64")
```
#### Running

* Open a command line terminal, go to this `./Chess Game` folder 
* Type in command line with following code:  
```
python3 OOPGUI_revised.py 
``` 
