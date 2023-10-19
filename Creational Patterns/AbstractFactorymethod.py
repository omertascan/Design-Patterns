import random

class Kurslar :  
    
    """ Kurslar"""
    
    def __init__(self,course_factory=None):
        """abstract factory kullanılarak kurslar oluştulur."""
        self.course_factory = course_factory 
    def show_course(self):
        """abstract factory kullanılarak kurslar oluştulur ve gösterilir .""" 
        
        course = self.course_factory() 
        print(f'Kurs İsimleri Bunlardır {course}')
        print(f'Fiyatları ise {course.Fee()}') 
        
        
class JavaKurslar :  
    """Java Kurslar Sinif """
    def Fee(self): 
        return 10000 
    def __str__(self):
        return "Java Kurslar" 
    
class AndrodidKurslar : 
   
    def Fee(self):
        return 20000
    def __str__(self):
        return "Android Kurslar"

class PyhtonKurslar : 
    
    
    def Fee(self):
        return 30000
    def __str__(self):
    
        return "Python Kurslar"  
    
def random_courses():  
    """Kursu seçmek için rastegele seçim """ 
    
    return  random.choice([JavaKurslar, AndrodidKurslar, PyhtonKurslar])()
                
if __name__ == "__main__" : 
    
    course = Kurslar(random_courses) 
    
    for i in range(5): 
        
        course.show_course()