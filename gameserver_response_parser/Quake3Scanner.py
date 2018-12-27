def parse_q3(data, addr):
    # general packet format:
    # <header>0x0A<keypairs>[0x0A<playerdata>]*0x0A
    # the keypairs are seperated by \
    # [\<key>\<value>]+
    # Source: http://int64.org:80/docs/gamestat-protocols/quake3.html
    # the source is no longer available but archive.org has it.

    server_dict = { "_ip": addr[0], "_port": addr[1], "_parser" : "q3"}

    data = data.split(b"\x0A")

    # check the header
    header = data[0]
    if header == "\xFF\xFF\xFF\xFFstatusResponse":
        server_dict["header"] = header

        keypairs = data[1][1:].split(b"\\") # remove the first /
        pos = 0
        while pos < len(keypairs-1):
            key = keypairs[pos]
            value = keypairs[pos+1]
            server_dict[key] = value
            pos+=2

        players = data[2:]
        # format is <score> <ping> "<name>"
        # for Soldier of Fortune 2 it is
        # <score> <ping> <deaths> "<name>"
        # i am not sure about the quotes

        player_data = [{"score": int(d[0]), "ping": int(d[1]), "name": d[2][1:-1]} for d in players]
        server_dict["players"] = player_data

        return server_dict
