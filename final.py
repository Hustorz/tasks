from abc import ABC, abstractmethod

class Student:
    def __init__(self, student_id: int, name: str, email: str, phone_number: int):
        self.id = student_id
        self.name = name 
        self.email = email
        self.number = phone_number
    def __repr__(self):
        return f"Student({self.id}, {self.name}, {self.email}, {self.number})"

class Teacher:
    def __init__(self, teacher_id: int, name: str, subject: str, phone_number: int ):
        self.id = teacher_id
        self.name = name
        self.subject = subject
        self.number = phone_number
    def __repr__(self):
        return f"Teacher({self.id}, {self.name}, {self.subject}, {self.number})"

class Course(ABC):
    def __init__(self, course_id: int, title: str, subject: str,
                 capacity: int = 10, lessons: int = 5, passing_score: float = 60.0):
        self.id = course_id
        self.title = title
        self.subject = subject
        self.capacity = capacity
        self.lessons = lessons
        self.passing_score = passing_score
        self.teacher_id = None
 
    @abstractmethod
    def info(self) -> str:
        pass
 
    def __repr__(self):
        return f"Course({self.id}, {self.title})"

class OnlineCourse(Course):
    def __init__(self, course_id, title, subject, capacity=30, lessons=5,
                 passing_score=60.0, platform="Zoom"):
        super().__init__(course_id, title, subject, capacity, lessons, passing_score)
        self.platform = platform
 
    def info(self) -> str:
        return f"{self.title} (online, {self.platform}, lessons: {self.lessons})"
 
 
class OfflineCourse(Course):
    def __init__(self, course_id, title, subject, capacity=12, lessons=5,
                 passing_score=60.0, classroom="101"):
        super().__init__(course_id, title, subject, capacity, lessons, passing_score)
        self.classroom = classroom
 
    def info(self) -> str:
        return f"{self.title} (in person, classroom. {self.classroom}, lessons: {self.lessons})"

class Enrollment:
    def __init__(self, enrollment_id: int, student_id: int, course_id: int):
        self.id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.status = "active"      
        self.grades = []           
        self.attendance = {}        
 
    def __repr__(self):
        return f"Enrollment({self.id}, student={self.student_id}, course={self.course_id})"

class EnrollmentService:
    def __init__(self, repo: Repository):
        self.repo = repo

    def enroll(self, student_id: int, course_id: int) -> Enrollment:
        enrollment_id = self.repo.next_id()
        enrollment = Enrollment(enrollment_id, student_id, course_id)
        self.repo.add(enrollment)
        return enrollment

    def add_grade(self, enrollment_id: int, grade: float) -> Enrollment:
        enrollment = self.repo.get(enrollment_id)
        enrollment.grades.append(grade)
        return enrollment

    def complete(self, enrollment_id: int) -> Enrollment:
        enrollment = self.repo.get(enrollment_id)
        enrollment.status = "completed"
        return enrollment

class Repository(ABC):     
    @abstractmethod
    def add(self, item):
        pass
 
    @abstractmethod
    def get(self, item_id):
        pass
 
    @abstractmethod
    def all(self) -> list:
        pass
 
class InMemoryRepository(Repository):
    def __init__(self):
        self._items = {}
        self._last_id = 0
 
    def next_id(self) -> int:
        self._last_id += 1
        return self._last_id
 
    def add(self, item):
        self._items[item.id] = item
        return item
 
    def get(self, item_id):
        if item_id not in self._items:
            raise ValueError(f"Объект с id={item_id} не найден")
        return self._items[item_id]
 
    def all(self) -> list:
        return list(self._items.values())

class CourseCreator(ABC):     
    @abstractmethod
    def create_course(self, course_id: int, title: str, subject: str, **kwargs) -> Course:
        pass
 
 
class OnlineCourseCreator(CourseCreator):
    def create_course(self, course_id, title, subject, **kwargs) -> Course:
        return OnlineCourse(course_id, title, subject,
            capacity=kwargs.get("capacity", 30),
            lessons=kwargs.get("lessons", 5), platform=kwargs.get('platform', 'Googlemeet'))

class OfflineCourseCreator(CourseCreator):
    def create_course(self, course_id, title, subject, **kwargs) -> Course:
        return OfflineCourse(course_id, title, subject,
            capacity=kwargs.get("capacity", 12),
            lessons=kwargs.get("lessons", 5),
            classroom=kwargs.get("classroom", "101"))

class CourseFactory:
    
 
    def __init__(self):
        self._creators = {"online": OnlineCourseCreator(),
                          "offline": OfflineCourseCreator()}
 
    def register(self, name: str, creator: CourseCreator):
        self._creators[name] = creator
 
    def create(self, course_id, title, subject, kind="offline", **kwargs) -> Course:
        if kind not in self._creators:
            raise ValueError(f"Unknown course format: {kind}")
        return self._creators[kind].create_course(course_id, title, subject, **kwargs)
 
class AttendanceService(ABC):
    @abstractmethod
    def mark(self, enrollment_id: int, lesson_number: int, attended: bool): pass

class AttendanceServiceConcrete(AttendanceService):
    def __init__(self, repo: Repository):
        self.repo = repo
    def mark(self, enrollment_id, lesson_number, attended):
        enrollment = self.repo.get(enrollment_id)
        enrollment.attendance[lesson_number] = attended
        return enrollment

class AllStrategy(ABC):
    @abstractmethod
    def calculate(self, grades: list, attendance: dict) -> float:
        pass

class AverageGradeStrategy(AllStrategy):
    def calculate(self, grades, attendance):
        if not grades:
            return 0
        return sum(grades) / len(grades)

class AttendancePenaltyStrategy(AllStrategy):
    def calculate(self, grades, attendance):
        if not grades:
            return 0

        avg = sum(grades) / len(grades)

        missed = sum(1 for a in attendance.values() if not a)
        penalty = missed * 5

        final = avg - penalty
        return final  




class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass
    
class ReportService(Subject):
    def __init__(self, strategy: AllStrategy, repo: Repository):
        self._observers = []
        self.strategy = strategy
        self.repo = repo
        self.last_report = None

 

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for obs in self._observers:
            obs.update(self)

    def generate_student_report(self, enrollment_id: int) -> str: 
        enrollment = self.repo.get(enrollment_id)
    
        final_score = self.strategy.calculate(enrollment.grades,enrollment.attendance)
        self.last_report = f"Final score: {final_score}"
        self.notify()

        return self.last_report

class EmailNotifier(Observer):
    def update(self, subject: ReportService):
        print(f"[EMAIL] Sending report: {subject.last_report}")

class CabinetNotifier(Observer):
    def update(self, subject: ReportService):
        print(f"[CABINET] New report available: {subject.last_report}")



repo = InMemoryRepository()
enroll_service = EnrollmentService(repo)

student = Student(1, "Alice", "a@mail.com", 123)
course_factory = CourseFactory()
course = course_factory.create(1, "Math", "Algebra", kind="offline")

e = enroll_service.enroll(student.id, course.id)
print(e)

enroll_service.complete(e.id)
print(e.status)

enroll_service.add_grade(e.id, 80)
enroll_service.add_grade(e.id, 90)
attendance = AttendanceServiceConcrete(repo)
attendance.mark(e.id, 1, True)
attendance.mark(e.id, 2, False)
report = ReportService(AverageGradeStrategy(), repo)
report.attach(EmailNotifier())
report.attach(CabinetNotifier())
print(report.generate_student_report(e.id))
s1 = Student(1, "Alice", "a@mail.com", 123)
s2 = Student(2, "Bob", "b@mail.com", 456)

c1 = course_factory.create(1, "Math", "Algebra", kind="offline")
c2 = course_factory.create(2, "Python", "Programming", kind="online")

e1 = enroll_service.enroll(s1.id, c1.id)
e2 = enroll_service.enroll(s2.id, c2.id)

enroll_service.add_grade(e1.id, 90)
enroll_service.add_grade(e2.id, 70)

print(report.generate_student_report(e1.id))
print(report.generate_student_report(e2.id))

    
 
  



 
    
