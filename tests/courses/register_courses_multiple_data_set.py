from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
from pages.home.navigation_page import NavigationPage
import unittest, pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "4111111111111", "1222", "123", "12345"), ("Learn Python 3 from scratch", "41111111111111", "1222", "456", "12345"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, ccPostal):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV, zip=ccPostal)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
        self.nav.navigateToHome()