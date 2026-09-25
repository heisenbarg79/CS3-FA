
class AssignmentSubmission:
    
    def __init__(self,student_name = None, student_id = None, assignment_title = None, due_date = None):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__submitted_files = []
        self.__grades = "Not Graded"
        self.__is_submitted = False
        
    def get_grade(self):
        return str(self.__grades)
    
    def __check_submission_status(self):
        
        if len(self.__submitted_files) <= 0:
            self.__is_submitted = "Missing"
            
            return False
        else:
           
            self.__is_submitted = f"Submitted {len(self.__submitted_files)} files"
            
            return True
    
        
    def remove_file(self,file):
        self.__check_submission_status()
        if self.get_grade() != "Not Graded" and len(self.__submitted_files) <= 1:
            print(f"[Warning] {self.student_name} cannot remove files. Assignment already graded")
            return
        
        for i in range(len(self.__submitted_files)):
            if file == self.__submitted_files[i]:
                self.__submitted_files.remove(file)
        print(f"[Success] {self.student_name} removed {file}")
        return
        
    def assign_grade(self,grade):
        self.__check_submission_status()
        if self.__check_submission_status() == False:
            print(f"[Error] Cannot grade. No files submitted for {self.student_name}")
            return
        print(f"[Success] Grade {grade} officially assigned to {self.student_name}")
        self.__grades = grade
        self.validate_grade(grade)
        return 
    def __is_duplicate(self,filename):
        temp_array = []
        for i in range(len(self.__submitted_files)):
            if filename == self.__submitted_files[i]:
                temp_array.append(filename)
        
        if len(temp_array) >= 1:
            return True
        return False
    def view_files(self):
        result = ""
        for i in range(len(self.__submitted_files)):
            if i == len(self.__submitted_files) - 1:
                result += self.__submitted_files[i]
            else:
                result += self.__submitted_files[i] + ", "
        
        return result
    def get_status_report(self):
        # print("---STATUS REPORT---")
        # print(f"Student Name: {self.student_name}")
        # print(f"Student ID: {self.student_id}")
        # print(f"Title of Assignment: {self.assignment_title}")
        # print(f"Due Date: {self.due_date}")
        # print(f"Files uploaded: {self.files}")
        # print(f"Grade: {self.grades}")
        # print(f"Has a submission: {self.is_submitted}")
        return f"ID: {self.student_id} | Name: {self.student_name} | Status: {self.__is_submitted} | Grade: {self.get_grade()}"
    def add_file(self,file):
        self.__check_submission_status()
        if self.__is_duplicate(file) == True:
            print(f"[Warning] {file} is already attached!")
            return
        self.__submitted_files.append(file)
        print(f"[Success] {self.student_name} attached {file}. Total files {len(self.__submitted_files)}")
    def validate_grade(self, score):
        if score == self.__grades:
            return True
        return False
def main():
    # instantiate 
    student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101","2026-10-01")
    student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-101","2026-10-01")
    student3 = AssignmentSubmission("Juan dela Cruz", "pshs-1033-x", "CS-101","2026-10-01")
    student4 = AssignmentSubmission("Maria Santos", "pshs-1044-x", "CS-101","2026-10-01")
    student5 = AssignmentSubmission("Jose Reyes", "pshs-1055-x", "CS-101","2026-10-01")

    print("--- TEST SCENARIO 1: Multiple Files via List ---")
    student1.add_file("main.py")
    student1.add_file("report.pdf")
    student1.assign_grade(95)
    print(f"Alex's Files: {student1.view_files()}\n")

    print("--- TEST SCENARIO 2: Removing Files from List")
    student2.add_file("wrong_homework.docx")
    student2.remove_file("wrong_homework.docx")
    student2.add_file("correct_project.py")
    student2.assign_grade(88)
    print(f"Adelle's Files: {student2.view_files()}\n")

    print("--- TEST SCENARIO 3: Preventing Duplicate Files")
    student3.add_file("script.py")
    student3.add_file("script.py")
    print(f"Juan's Files: {student3.view_files()}\n")
    
    print("--- TEST SCENARIO 4: Removing file after being graded")
    student4.add_file("exam_answers.pdf")
    student4.assign_grade(75)
    student4.remove_file("exam_answers.pdf")
    print("\n")

    print("--- TEST SCENARIO 5: Empty List Handling")
    student5.add_file("draft.txt")
    
    student5.remove_file("draft.txt")
    student5.assign_grade(100)
    print("\n")

    print("--- FINAL SYSTEM REPORT ---")
    
    print(student1.get_status_report())
    print(student2.get_status_report())
    print(student3.get_status_report())
    print(student4.get_status_report())
    print(student5.get_status_report())

main()
