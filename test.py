'''
this is the test file in which we are going to check out the py file with the help of unittest
'''
import unittest
import capitalizeText

class testPrimeNumber(unittest.TestCase):
    def testOne(self):
        result = capitalizeText.capText("anmol noor")
        self.assertEqual(result,"Anmol Noor") 
    def testSecond(self):
        result = capitalizeText.capText("this is a text string to test the unittest on a file")
        self.assertEqual(result,"This Is A Text String To Test The Unittest On A File")
        
if __name__ == "__main__":
    unittest.main()
