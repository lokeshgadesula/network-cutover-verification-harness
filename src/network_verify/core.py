def compare(a,b):
 def s(x,k,key,ok=lambda z:True): return {z[key] for z in x.get(k,[]) if ok(z)}
 r=sorted(s(a,"routes","prefix")-s(b,"routes","prefix"))
 i=sorted(s(a,"interfaces","name",lambda z:z["up"])-s(b,"interfaces","name",lambda z:z["up"]))
 g=sorted(s(a,"bgp","peer",lambda z:z["state"]=="Established")-s(b,"bgp","peer",lambda z:z["state"]=="Established"))
 m=sorted(s(a,"mac","mac")-s(b,"mac","mac"))
 return {"missing_routes":r,"down_interfaces":i,"dropped_bgp_neighbors":g,"missing_macs":m,"go":not(r or i or g)}
class NetmikoCollector:
 COMMANDS={"cisco_nxos":["show interface status","show ip route","show mac address-table","show bgp l2vpn evpn summary"],"arista_eos":["show interfaces status","show ip route","show mac address-table","show bgp evpn summary"]}
 def collect_raw(self,device):
  try: from netmiko import ConnectHandler
  except ImportError as e: raise RuntimeError("Install Netmiko for live SSH") from e
  c=ConnectHandler(**device)
  try: return {cmd:c.send_command(cmd) for cmd in self.COMMANDS[device["device_type"]]}
  finally: c.disconnect()
