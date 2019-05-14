import unittest
import csvdata
import urllib2

data=urllib2.urlopen("https://www.ssb.no/eksport/tabell.csv?key=372475")
aa=data.read()
data.close()
class Testcsvdata(unittest.TestCase):

    def test_f(self):
        self.assertEqual(csvdata.getnames(aa),['\rAll households', '\rCouples without children, oldest person under 45 years'])
    def test_f2(self):
        self.assertEqual(csvdata.getvalue(aa),[510000, 604800])

if __name__=="__main__":
    unittest.main()


