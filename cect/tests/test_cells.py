import unittest


class TestCellMethods(unittest.TestCase):
    def test_contralaterals(self):
        from cect.Cells import get_contralateral_cell, is_one_of_bilateral_pair

        assert get_contralateral_cell("AVAL") == "AVAR"
        assert get_contralateral_cell("AVAR") == "AVAL"
        assert get_contralateral_cell("ALA") == "ALA"
        assert get_contralateral_cell("AQR") == "AQR"
        assert get_contralateral_cell("AVL") == "AVL"

        assert is_one_of_bilateral_pair("AVAL")
        assert not is_one_of_bilateral_pair("ALA")
        assert not is_one_of_bilateral_pair("RMED")


if __name__ == "__main__":
    unittest.main()
