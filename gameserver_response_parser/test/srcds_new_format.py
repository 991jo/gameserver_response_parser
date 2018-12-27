import unittest

from gameserver_response_parser import *

# query string, source: [https://developer.valvesoftware.com/wiki/Server_queries#A2S_INFO]

# "ÿÿÿÿI.game2xs.com Counter-Strike Source #1.de_dust.cstrike.Counter-Strike: Source......dl..1.0.0.22."
css = b"\xFF\xFF\xFF\xFF\x49\x02\x67\x61\x6D\x65\x32\x78\x73\x2E\x63\x6F"\
b"\x6D\x20\x43\x6F\x75\x6E\x74\x65\x72\x2D\x53\x74\x72\x69\x6B\x65"\
b"\x20\x53\x6F\x75\x72\x63\x65\x20\x23\x31\x00\x64\x65\x5F\x64\x75"\
b"\x73\x74\x00\x63\x73\x74\x72\x69\x6B\x65\x00\x43\x6F\x75\x6E\x74"\
b"\x65\x72\x2D\x53\x74\x72\x69\x6B\x65\x3A\x20\x53\x6F\x75\x72\x63"\
b"\x65\x00\xF0\x00\x05\x10\x04\x64\x6C\x00\x00\x31\x2E\x30\x2E\x30"\
b"\x2E\x32\x32\x00"

css_dict = { "_ip": "10.0.0.10",
        "_port": 27015,
        "_parser": "SRCDS",
        "_parser_subversion": "srcds",
        "header": int.from_bytes(b"I", byteorder="little"),
        "protocol": 0x02,
        "name": "game2xs.com Counter-Strike Source #1",
        "map": "de_dust",
        "folder": "cstrike",
        "game": "Counter-Strike: Source",
        "id": 240,
        "players": 0x05,
        "max. players": 0x10,
        "bots": 0x04,
        "server type": "d",
        "environment": "l",
        "visibility": 0,
        "vac": 0,
        "version": "1.0.0.22"}

# "ÿÿÿÿI.Ship Server.batavier.ship.The Ship.`....lw.....1.0.0.4."
the_ship = b"\xFF\xFF\xFF\xFF\x49\x07\x53\x68\x69\x70\x20\x53\x65\x72\x76\x65"\
b"\x72\x00\x62\x61\x74\x61\x76\x69\x65\x72\x00\x73\x68\x69\x70\x00"\
b"\x54\x68\x65\x20\x53\x68\x69\x70\x00\x60\x09\x01\x05\x00\x6C\x77"\
b"\x00\x00\x01\x03\x03\x31\x2E\x30\x2E\x30\x2E\x34\x00"

the_ship_dict =  { "_ip": "10.0.0.10",
        "_port": 27015,
        "protocol" : 0x07,
        "name": "Ship Server",
        "id": 2400,
        "mode": 0x01,
        "witnesses": 0x03,
        "duration": 0x03}

class CSSTest(unittest.TestCase):

    def setUp(self):
        self.output = parse_srcds(css, ("10.0.0.10",27015))

    def test_keys(self):
        for key, value in css_dict.items():
            self.assertTrue(key in self.output.keys(), "key %s is missing." % key)
            self.assertEqual(self.output[key], value, "Value missmatch, is %s, should be %s" % (self.output[key], key))


class TheShipTest(unittest.TestCase):

    def setUp(self):
        self.output = parse_srcds(the_ship, ("10.0.0.10",27015))

    def test_keys(self):
        for key, value in the_ship_dict.items():
            self.assertTrue(key in self.output.keys(), "key %s is missing." % key)
            self.assertEqual(self.output[key], value, "Value missmatch, is %s, should be %s" % (self.output[key], key))

if __name__ == "__main__":
    unittest.main()
