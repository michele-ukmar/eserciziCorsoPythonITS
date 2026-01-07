import unittest

def add(x, y):
    pass

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()

# F
# ======================================================================
# FAIL: test_add (__main__.TestAdd)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "./tdd_basic.py", line 8, in test_add
#     self.assertEqual(add(1, 2), 3)
# AssertionError: None != 3

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (failures=1) 

import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK