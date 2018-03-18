# prerelease
## task 1

####  1.1
JSP diagrams can show the the function and parameter's structure in the whole programme, including the iteration and the choice.

#### 1.2
the 。meand to making choice between different situations
the * means to iteration of a function

#### 1.3

NOT EOF
salary>50
slalary>=90
projectmanager
leaddeveloper
manager

#### 1.4

Add another block that says salary>70。
if Flase, assign the role as leaddeveloper
if True, goes to the selection of salary>=90
change that False situation to assign the role as consultant

#### 1.5

    IF salary>=70  （line 5)
            IF salary>=90
                THEN 
                    Role<---projectmanager
                ElSE 
                    Role<---consultant
            ENDIF
        ELSE
            Role<---leaddeveloper
    ELSE
        Role<---manager
    
    
#### 1.6

    def determinerole(salary):
        if salary>50:
            if salary>70:
                if salary>=90
                    return 'projectmanager'
                else:
                    return 'consultant'
            else:
                return 'leaddeveloper'
        else:
            return 'manager'











