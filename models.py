from django.db import models

# Create your models here.
class Teacher(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    telephone = models.IntegerField()
    '''
    python manage.py migrate --fake teachers
    para resolver el error de 'table already exist'
    '''
    class Meta:
        db_table = 'teachers'
        
        
class Student(models.Model):
    id_student = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'students'
        
        
class Level(models.Model):
    
    id_level = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'levels'
        
        
class Course(models.Model):
    
    id_course = models.AutoField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE, db_column='levels_id_level')
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, db_column='teachers_id_teacher')
     
    class Meta:
        db_table = 'courses'
        
        
class StudentCourse(models.Model):
    
    id_student_course = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               db_column='courses_id_course')
    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE,
                                db_column='students_id_student')
    start_date = models.DateField()
    end_date = models.DateField()
    
    class Meta():
        
        db_table = 'students_courses'