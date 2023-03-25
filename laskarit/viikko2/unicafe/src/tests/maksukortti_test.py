import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(200)

        self.assertEqual(str(self.maksukortti.saldo), '1200')

    def test_riittavasti_rahaa_raha_vahenee_oikein(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200),True)

    def test_liian_vahan_rahaa_raha_vahenee_oikein(self):
        self.assertNotEqual(self.maksukortti.ota_rahaa(3000),True)
