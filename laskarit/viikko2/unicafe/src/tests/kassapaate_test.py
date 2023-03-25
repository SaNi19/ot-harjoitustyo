import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        

    def test_konstruktori_asettaa_kassassa_rahaa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
    
    def test_konstruktori_asettaa_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_konstruktori_asettaa_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat,0) 
        
    def test_jos_maksu_riittava_kassassa_rahamaara_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
        
    def test_jos_maksu_on_riittava_myytyjen_edullisten_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset,1)
        
    def test_jos_maksu_riittava_kassassa_rahamaara_kasvaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
        
    def test_jos_maksu_on_riittava_myytyjen_edullisten_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_jos_edulliset_maksu_ei_ole_riittava_kassassa_rahamaara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        
    def test_jos_maksu_ei_ole_riittava_myytyjen_edullisten_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset,0)
        
    def test_jos_maukkaat_maksu_ei_ole_riittava_kassassa_rahamaara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        
    def test_jos_maksu_ei_ole_riittava_myytyjen_edullisten_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_jos_kortilla_on_tarpeeksi_rahaa_edulliseen_veloitetaan_summa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        if self.maksukortti.saldo == 760:
            return True
        
    def test_jos_kortilla_on_tarpeeksi_rahaa_edulliseen_edullisten_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        return True
    
    def test_jos_kortilla_on_tarpeeksi_rahaa_maukkaaseen_veloitetaan_summa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        if self.maksukortti.saldo == 600:
            return True

    def test_jos_kortilla_on_tarpeeksi_rahaa_maukkaaseen_maukkaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        return True
    
    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_maukkaaseen_kortilta_ei_veloiteta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        if self.maksukortti.saldo == 1000:
            return False
        
    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_edulliseen_kortilta_ei_veloiteta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        if self.maksukortti.saldo == 1000:
            return False
        
    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_maukkaaseen_maukkaiden_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        return False
    
    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_maukkaaseen_maukkaiden_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        return False
    
    def test_kassassa_oleva_rahamaara_ei_muutu_kun_ostetaan_edullinen_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_oleva_rahamaara_ei_muutu_kun_ostetaan_maukas_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_jos_maksu_ei_ole_riittava_kahteen_edulliseen_myytyjen_edullisten_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_jos_maksu_ei_ole_riittava_kahteen_maukkaaseen_myytyjen_maukkaiden_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_kortille_voi_ladata_rahaa_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    def test_kortille_voi_ladata_negatiivisesti_rahaa_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_edulliseen_palautetaan_false(self):
        self.maksukortti.saldo = 200
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        return False
    
    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_maukkaaseen_palautetaan_false(self):
        self.maksukortti.saldo = 200
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        return False
            

    