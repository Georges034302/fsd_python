# Faculty GUI with Python

The Faculty GUI program is composed of 2 scripts:
-   model.py 
-   controller.py
-   view scripts (student_view.py and faculty_view.py)

the aim of this program is to focus on the topic of files with Python

## The model script:
The model has:

*   The Student class:
    *   Student has 4 fields:
        *   ID randomly generated between of 3-digits size
        *   name formatted as "Student-ID"
        *   mark initialized from parameter
        *   grade auto-calculated based on mark
    *   Student has a function grade to determine the grade based on the mark
    *   Student has a function to match object ID with parameter
    *   Student has a function to return object description: "name: [ mark --> grade]"
*   Database class:
    *   Database has one field, a list of 10 students
    *   Database has a function to return the list of students

## The controller script:
The controller has:
*   The StudentController class
    *   StudentController has 2 fields:
        *   master window object
        *   model Database instance
    *   StudentController has a function to select a student from list and open a new window to show student information
    *   StudentController has a function to return the list of students from Database

## The student_view script:
The student_view has:
*   The StudentView class that inherits TopLevel
    *   StudentView has a title, geometry(300x200)
    *   StudentView should be placed on the right-hand-side of the faculty_view
    *   StudentView has a Label showing the selected student information
    *   StudentView has a close button (to close the window only)
  
## The faculty_view script:
*   The faculty_view script has the root window (300x300)
*   The faculty_view script has a controller instance
*   The faculty_view script has a ListBox showing the students from the model
*   The faculty_view script has a select button opening the selected student information window
The controller loads the data from database into the listbox and monitors button events
