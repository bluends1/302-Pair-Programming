import unittest, tax

class testtax(unittest.TestCase):

    def test_tax1(self):
        r = tax.cal(2, [745693, 438638])[-1]
        self.assertEqual(r, 114336)

    def test_tax2(self):
        r = tax.cal(2, [579376, 971651])[-1]
        self.assertEqual(r, 176674)

    def test_tax3(self):
        r = tax.cal(2, [236228, 386173])[-1]
        self.assertEqual(r, 25694)

    def test_tax4(self):
        r = tax.cal(2, [242491, 873310])[-1]
        self.assertEqual(r, 108864)

    def test_tax5(self):
        r = tax.cal(2, [501972, 324731])[-1]
        self.assertEqual(r, 54544)

    def test_tax6(self):
        r = tax.cal(2, [745505, 742744])[-1]
        self.assertEqual(r, 166002)

    def test_tax7(self):
        r = tax.cal(2, [398493, 961401])[-1]
        self.assertEqual(r, 144181)

    def test_tax8(self):
        r = tax.cal(2, [351009, 672727])[-1]
        self.assertEqual(r, 87111)

    def test_tax9(self):
        r = tax.cal(2, [224021, 300713])[-1]
        self.assertEqual(r, 12364)

    def test_tax10(self):
        r = tax.cal(2, [682626, 783577])[-1]
        self.assertEqual(r, 162254)

    def test_tax11(self):
        r = tax.cal(2, [163300, 282063])[-1]
        self.assertEqual(r, 8058)

    def test_tax12(self):
        r = tax.cal(2, [82093, 557859])[-1]
        self.assertEqual(r, 40472)

    def test_tax13(self):
        r = tax.cal(2, [567641, 514420])[-1]
        self.assertEqual(r, 96950)

    def test_tax14(self):
        r = tax.cal(2, [116033, 523318])[-1]
        self.assertEqual(r, 40375)

    def test_tax15(self):
        r = tax.cal(2, [450604, 512674])[-1]
        self.assertEqual(r, 76757)

    def test_tax16(self):
        r = tax.cal(2, [550598, 140513])[-1]
        self.assertEqual(r, 48734)

    def test_tax17(self):
        r = tax.cal(2, [935166, 651119])[-1]
        self.assertEqual(r, 182668)

    def test_tax18(self):
        r = tax.cal(2, [391338, 331695])[-1]
        self.assertEqual(r, 36663)

    def test_tax19(self):
        r = tax.cal(2, [870059, 621064])[-1]
        self.assertEqual(r, 166490)

    def test_tax20(self):
        r = tax.cal(2, [208734, 326526])[-1]
        self.assertEqual(r, 14925)