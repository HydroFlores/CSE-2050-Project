import Main
import unittest

class Test_Course(unittest.TestCase):

    def test_obj_creation(self):
        """Tests all parameters of object Course to test its creation"""
        st1 = 1
        st2 = 2
        tc1 = Main.Course("CSE 4300", 3, [st1, st2])
        
        self.assertEqual(tc1.course_code, "CSE 4300")
        self.assertEqual(tc1.credits, 3)
        self.assertEqual(len(tc1.students), 2)
        self.assertIn(st1, tc1.students)
        self.assertIn(st2, tc1.students)

    def test_add_student(self):
        "Test if students gets updated when a student is added"
        st3 = 3
        st4 = 4
        tc2 = Main.Course("ECE 2001", 4, [st3])

        self.assertEqual(len(tc2.students), 1)
        
        tc2.add_student(st4)

        self.assertEqual(len(tc2.students), 2)
        self.assertIn(st4, tc2.students)
    
    def test_duplicate_obj_in_students(self):
        
        st5 = 5

        tc3 = Main.Course("CSE 1010", 3, [])

        tc3.add_student(st5)
        tc3.add_student(st5)

        self.assertEqual(len(tc3.students), 1)
        self.assertIn(st5, tc3.students)

    def test_student_count(self):
        
        st6 = 6
        st7 = 7
        st8 = 8

        tc4 = Main.Course("CSE 2050", 3, [st6, st7, st8])

        self.assertEqual(tc4.get_student_count(), 3)
        self.assertIn(st6, tc4.students)
        self.assertIn(st7, tc4.students)
        self.assertIn(st8, tc4.students)

class Test_Student(unittest.TestCase):

    def test_obj_creation(self):
        """Tests all parameters of object Student to test its creation"""
        ct1 = 1
        ct2 = 2
        tc1 = Main.Student("ID1", "Charlie Kuryluk", {ct1: "A+", ct2: "B+"})
        
        self.assertEqual(tc1.student_id, "ID1")
        self.assertEqual(tc1.name, "Charlie Kuryluk")
        self.assertEqual(len(tc1.courses), 2)
        self.assertIn(ct1, tc1.courses)
        self.assertIn(ct2, tc1.courses)

    def test_enroll(self):
        "Test if students gets updated when a student is added"
        ct3 = 3
        ct4 = 4
        tc2 = Main.Student("ID2", "Gudio Van Rossum", {ct3: "A+"})

        self.assertEqual(len(tc2.courses), 1)
        
        tc2.enroll(ct4, "B+")

        self.assertEqual(len(tc2.courses), 2)
        self.assertIn(ct4, tc2.courses)

if __name__ == "__main__":
    unittest.main()