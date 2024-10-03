# Time Table Generator 
This is a simple timetable generator made using Flask. It creates procedurally generated generated timetables for the different classes in a semester.
It uses a HTML based frontend combined with a Flask backend which creates the server for all user interactions. The subjects in a given semester are entered into a subject list.
From this subject list each subject is randomly placed onto an empty timetable. For Example,
```
given subjects are Math - M, Chemistry - C and DBMS - D, the generated timetable would be
                                _ _ _        M D D
                                _ _ _  >>>>  C D M
                                _ _ _        M M C
```
Each randomly selected subject is placed in a priority order, the lab based subjects are given first priority and the theory based subjects are arranged next and so on. The timetables also contain break sessions and free periods for students ;)

## Requirements:
- Flask 1.1.1

## Getting Started: 
- To run the code open ttg.exe or type ```python hello.py``` in your console. 
Then type in ```http://127.0.0.1:5000/zxc.html``` in your web browser's address bar. 
To change the sample timetable reload the page.

- Alternatively:
To run the code in command line type in ```set FLASK_APP=hello.py```
For Linux/OSX replace set with export
then type ```python -m flask run```


## Impact of project:
- The Timetable Generator saved more than 20 hours of timetable planning by the faculty across all branches in my college. 
- This project helped me understand why coding in Python is fun and how important it is automating manual tasks.


## TODO:
- Fix UI
- Add database connections to the timetables for effective storage.
- Provide edit options to the professors and head of the department to change the timetable in case of any collisions in class assignment.

(P.S. this is the very first project I created in college, so please forgive the messy code)


