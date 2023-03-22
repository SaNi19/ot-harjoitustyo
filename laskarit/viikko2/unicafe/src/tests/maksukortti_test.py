import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikei(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(250)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.50 euroa",)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(400)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.ota_rahaa(300)

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    
   