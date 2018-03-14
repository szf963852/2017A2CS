class Assessment:
    def __init__(self, t, m):
        self.Title = t
        self.MaxMarks = m

    def OutputAssessmentDetails(self):
        print(self.Title, " Marks: ",self.MaxMarks)

class Course:
    def __init__(self, t, m): # sets up a new course
        self.CourseTitle = t
        self.MaxStudents = m
        self.NumberOfLessons = 0
        self.CourseLesson = []
        self.CourseAssessment = Assessment

    def AddLesson(self, t, d, r):
        self.NumberOfLessons = self.NumberOfLessons + 1
        self.CourseLesson.append(Lesson(t, d, r))

    def AddAssessment(self, t, m):
        CourseAssessment = Assessment(t, m)

    def OutputCourseDetails(self):
        print(self.CourseTitle, end=' ')
        print("Maximum number of students: ",self.MaxStudents)
        for i in range(self.NumberOfLessons):
            print(self.CourseLesson[i].OutputLessonDetails())

class Lesson:
    def __init__(self, t, d, r):
        self.LessonTitle = t
        self.DurationMinutes = d
        self.requiresLab = r

    def OutputLessonDetails(self):
        print(self.LessonTitle,self.DurationMinutes)



MyCourse = Course("Problem Solving", 10)
MyCourse.AddAssessment("physics", 100)
MyCourse.AddLesson("computer", 60, False)
MyCourse.AddLesson("economics", 120, True)
MyCourse.AddLesson("english", 60, False)
MyCourse.OutputCourseDetails()
