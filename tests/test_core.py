from network_verify.core import compare
def s(r=("10/8",),i=("Eth1",),b=("1",),m=("aa",)): return {"routes":[{"prefix":x} for x in r],"interfaces":[{"name":x,"up":True} for x in i],"bgp":[{"peer":x,"state":"Established"} for x in b],"mac":[{"mac":x} for x in m]}
def test_same(): assert compare(s(),s())["go"]
def test_route(): assert compare(s(r=("10/8","20/8")),s())["missing_routes"]==["20/8"]
def test_interface(): assert compare(s(i=("Eth1","Eth2")),s())["down_interfaces"]==["Eth2"]
def test_bgp(): assert compare(s(b=("1","2")),s())["dropped_bgp_neighbors"]==["2"]
def test_mac(): assert compare(s(m=("aa","bb")),s())["missing_macs"]==["bb"]
