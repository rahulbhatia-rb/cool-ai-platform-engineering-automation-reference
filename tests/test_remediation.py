import sys,unittest
sys.path.append("src")
from remediation import Signal,recommend
class T(unittest.TestCase):
 def test_safe_signal(self):self.assertTrue(recommend(Signal("platform",True,True,True))[0])
 def test_missing_runbook(self):self.assertIn("approved runbook required",recommend(Signal("p",False,True,True))[1])
 def test_nonreversible(self):self.assertFalse(recommend(Signal("p",True,True,False))[0])
if __name__=="__main__":unittest.main()
