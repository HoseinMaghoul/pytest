import unittest
from person import Person


class PersonTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Person('hosein', 'maghoul')
        self.p2 = Person('nillo', 'kermani')

    def tearDown(self):
        print('Done....')


    def test_full_name(self):

        self.assertEqual(self.p1.fullname(), 'hosein maghoul')
        self.assertEqual(self.p2.fullname(), 'nillo kermani')


    def test_email(self):

        self.assertEqual(self.p1.email(), 'hoseinmaghoul@email.com')
        self.assertEqual(self.p2.email(), 'nillokermani@email.com')


if __name__ == '__main__':
    unittest.main()