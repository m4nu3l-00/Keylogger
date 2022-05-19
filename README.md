# Keylogger
This Keylogger is part of the seminar paper where the Keystroke Dynamics will be examinated with a Neural Network.  
The Neural Network could be found here: https://github.com/kai66w/Studienarbeit_NN  

## How to use this project
By default the GUI will be started. To start the console the program must be executed with the argument `-c`.  
For starting the GUI explicitly the program must be started with argument `-g`.  
Executing the program with `-h` a help will be displayed.
### GUI
Start and stop the Keylogger with the corresponding "Start/Stop" button.  
Alternatively the Keylogger could be stopped with the End-key.  
This key can be set with the "Set end-key" button.
![image](https://user-images.githubusercontent.com/61203017/169260423-04d6c8e7-9097-4246-9891-277d2f634fa3.png)
### Console
Following commands are available:\
`help`:  Prints the help-interface\
`exit`:  Terminate the Program\
`start`: Starts the keylogger\
`stop`: Stops the keylogger\
`set stop key`: Setting the stop-key which will terminate the keylogger\
`show stop key:`: Prints the defined stop-key

### Output
The recored data is saved to a csv-file which is called "keylogger.csv".  
An already existing file will be overwritten.
## More information
Read the seminar paper.
