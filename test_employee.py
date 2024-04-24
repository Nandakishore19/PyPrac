import unittest
from unittest.mock import patch
from employee import Employee
# print(unittest.TestCase.assertEquals.__doc__)
class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('SetupClass')
    
    @classmethod
    def tearDownClass(cls) -> None:
        print('TearDownClass')
    def setUp(self) -> None:
        print('\nSetUp')
        self.emp_1 = Employee('Nanda','Kishore',50000)
        self.emp_2 = Employee('Gorenka','Kishore',60000)
    def tearDown(self) -> None:
        print('TearDown\n')
    def test_email(self):
        
        self.assertEqual(self.emp_1.email, 'Nanda.Kishore@email.com')
        self.assertEqual(self.emp_2.email, 'Gorenka.Kishore@email.com')
        self.emp_1.first = 'ABC'
        self.assertEqual(self.emp_1.email, 'ABC.Kishore@email.com')
    def test_apply_raise(self):
        # self.asser
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
    
        self.assertEqual(self.emp_1.pay,52500)
        self.assertEqual(self.emp_2.pay,63000)
    def test_montly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Kishore/May')
            self.assertEqual(schedule, 'Success')   

            mocked_get.return_value.ok = False
            
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Kishore/June')
            self.assertEqual(schedule,'Bad Response!!')

if __name__ == '__main__':
    unittest.main()