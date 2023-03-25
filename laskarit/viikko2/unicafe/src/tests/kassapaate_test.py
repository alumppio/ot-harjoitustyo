import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaate_luotu(self):
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, '100000')

    def test_alussa_maukkaat(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_alussa_edulliset(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateis_edullinen_onnistuu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240),0)

    
    def test_kateis_edullinen_epaonnistuu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(60),60)


    def test_kateis_maukas_onnistuu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400),0)

    
    def test_kateis_maukas_epaonnistuu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(60),60)


    def test_kortti_edullinen_onnistuu(self):
        kortti = Maksukortti(300)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),True)

    def test_kortti_edullinen_epaonnistuu(self):
        kortti = Maksukortti(200)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),False)
    
    def test_kortti_maukas_onnistuu(self):
        kortti = Maksukortti(400)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),True)

    def test_kortti_maukas_epaonnistuu(self):
        kortti = Maksukortti(300)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),False)
    

    def test_ladaataan_kassasta_rahaa_kortille(self):
        kortti = Maksukortti(300)
        self.kassapaate.lataa_rahaa_kortille(kortti,200)

        self.assertEqual(kortti.saldo, 500)

    def test_negatiivinen_rahanlataus_kassasta_kortille(self):
        kortti = Maksukortti(300)
        self.kassapaate.lataa_rahaa_kortille(kortti,-200)

        self.assertEqual(kortti.saldo, 300)
