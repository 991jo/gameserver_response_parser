import unittest

from gameserver_response_parser import parse_q3

q3 = b'\xff\xff\xff\xffstatusResponse\n\\sv_maxclients\\32\\server_freezetag\\1\\sv_hostname\\{CROM} FREEZE\\sv_maxRate\\25000\\sv_minPing\\0\\sv_maxPing\\0\\sv_floodProtect\\1\\dmflags\\0\\fraglimit\\20\\timelimit\\20\\capturelimit\\8\\version\\Q3 1.32c linux-i386 May  8 2006\\sv_punkbuster\\0\\protocol\\68\\g_gametype\\3\\mapname\\pro-q3dm6\\sv_privateClients\\0\\sv_allowDownload\\0\\bot_minplayers\\2\\.Administrator\\Kal\\.E-mail\\admin@cromctf.com\\.IRC\\#crom @ irc.enterthegame.com\\.Location\\Chicago, IL\\.Website\\www.cromctf.com\\g_needpass\\0\\gamename\\freeze\\gameversion\\OSP v1.03a\\Score_Blue\\4 \\Score_Red\\3 \\Players_Blue\\0 2 \\Players_Red\\1 3 \\Score_Time\\Waiting for Players\\server_ospauth\\0\\server_promode\\0\n0 27 "Frankfurt"\n3 0 "Xaero"\n0 33 "^3Razzle^7.^1Dazzle"\n0 18 "DAMN!"\n0 50 "DiRTY"\n0 34 "^1noob.Jr"\n2 0 "Uriel"\n6 0 "Bitterman"\n0 72 "pork.chop"\n5 0 "Sarge"\n0 61 "crunk"\n'
# 216.86.155.162:27960 
q3_dict = { "_ip": "216.86.155.162",
        "_port" : 27960,
        "_parser": "q3",
        "header" : b"\xFF\xFF\xFF\xFFstatusResponse",
        b"sv_maxclients" : b"32",
        b"sv_hostname" : b"{CROM} FREEZE",
        b"server_promode" : b"0"
    }
q3_players = [{"score" : 0, "ping" : 27, "name" :  "Frankfurt"},
    {"score" : 3, "ping" : 0 , "name" :  "Xaero"},
    {"score" : 0, "ping" : 33, "name" :  "^3Razzle^7.^1Dazzle"},
    {"score" : 0, "ping" : 18, "name" :  "DAMN!"},
    {"score" : 0, "ping" : 50, "name" :  "DiRTY"},
    {"score" : 0, "ping" : 34, "name" :  "^1noob.Jr"},
    {"score" : 2, "ping" : 0 , "name" :  "Uriel"},
    {"score" : 6, "ping" : 0 , "name" :  "Bitterman"},
    {"score" : 0, "ping" : 72, "name" :  "pork.chop"},
    {"score" : 5, "ping" : 0 , "name" :  "Sarge"},
    {"score" : 0, "ping" : 61, "name" :  "crunk"}]

class Q3Test(unittest.TestCase):

    def setUp(self):
        self.output = parse_q3(q3,("216.86.155.162",27960 ))

    def test_keys(self):
        for key, value in q3_dict.items():
            self.assertTrue(key in self.output.keys(), "key '%s' is missing." % key)
            self.assertEqual(self.output[key], value, "Value missmatch, key '%s' is %s, should be %s" % (key, self.output[key], value))

    def test_players(self):
        for i, player in enumerate(q3_players):
            p = self.output["players"][i]
            for key, value in player.items():
                self.assertTrue(key in p.keys(), "key '%s' is missing in player dict for player %d" % (key, i))
                self.assertEqual(p[key], value, "Value missmatch for player %d, key '%s' is %s, should be %s" % (i, key, p[key], value))


if __name__ == "__main__":
    unittest.main()
