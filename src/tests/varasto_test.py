import unittest
from varasto import Varasto

# comment

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_tilavuus_nolla(self):
        v = Varasto(0)
        self.assertAlmostEqual(v.tilavuus, 0)
    
    def test_saldo_alle_nolla(self):
        v = Varasto(10, -1)
        self.assertAlmostEqual(v.saldo, 0)
    
    def test_saldo_enemmän_kuin_tilavuus(self):
        v = Varasto(10, 20)
        self.assertAlmostEqual(v.saldo, v.tilavuus)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)
    
    def test_lisaa_varastoon_negatiivinen_luku(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_lisaa_varastoon_enemmän_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ota_varastosta_negatiivinen_luku(self):
        self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_ota_varastosta_enemman_mita_voi(self):
        self.varasto.lisaa_varastoon(10)
        maara = self.varasto.ota_varastosta(20)
        self.assertAlmostEqual(maara, 10)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_printtaus_toimii_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
