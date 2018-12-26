import unittest

from gameserver_response_parser import *

# query string, source: [https://developer.valvesoftware.com/wiki/Server_queries#A2S_INFO]

#"ÿÿÿÿI.game2xs.com Counter-Strike Source #1.de_dust.cstrike.Counter-Strike: Source......dl..1.0.0.22."
css = b"\xFF\xFF\xFF\xFF\x49\x02\x67\x61\x6D\x65\x32\x78\x73\x2E\x63\x6F"\
b"\x6D\x20\x43\x6F\x75\x6E\x74\x65\x72\x2D\x53\x74\x72\x69\x6B\x65"\
b"\x20\x53\x6F\x75\x72\x63\x65\x20\x23\x31\x00\x64\x65\x5F\x64\x75"\
b"\x73\x74\x00\x63\x73\x74\x72\x69\x6B\x65\x00\x43\x6F\x75\x6E\x74"\
b"\x65\x72\x2D\x53\x74\x72\x69\x6B\x65\x3A\x20\x53\x6F\x75\x72\x63"\
b"\x65\x00\xF0\x00\x05\x10\x04\x64\x6C\x00\x00\x31\x2E\x30\x2E\x30"\
b"\x2E\x32\x32\x00"

class NewFormatTest(unittest.TestCase):

    def setUp(self):
        self.output = parse_srcds(css, ("10.0.0.10",27015))

    def test_ip_port(self):
        self.assertEqual(self.output["_ip"],"10.0.0.10")
        self.assertEqual(self.output["_port"],27015)

    def test_metadata(self):
        self.assertEqual(self.output["_parser"],"SRCDS")
        self.assertEqual(self.output["_parser_subversion"],"srcds")

    def test_headerdata(self):
        self.assertEqual(self.output["header"],int.from_bytes(b"I", byteorder="little"))

    def test_protocoldata(self):
        self.assertEqual(self.output["protocol"],0x02)

    def test_strings(self):
        self.assertEqual(self.output["name"],"game2xs.com Counter-Strike Source #1")
        self.assertEqual(self.output["map"],"de_dust")
        self.assertEqual(self.output["folder"],"cstrike")
        self.assertEqual(self.output["game"],"Counter-Strike: Source")

    def test_appid(self):
        self.assertEqual(self.output["id"],240)

    def test_serverdata(self):
        self.assertEqual(self.output["players"],0x05)
        self.assertEqual(self.output["max. players"],0x10)
        self.assertEqual(self.output["bots"],0x04)
        self.assertEqual(self.output["server type"],"d")
        self.assertEqual(self.output["environment"],"l")
        self.assertEqual(self.output["visibility"],0)
        self.assertEqual(self.output["vac"],0)

    def test_version_string(self):
        self.assertEqual(self.output["version"],"1.0.0.22")

    def test_edf_existence(self):
        self.assertFalse("edf" in self.output.keys())





if __name__ == "__main__":
    unittest.main()
