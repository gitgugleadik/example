import wmi
class Programs:
    def __init__(self):
        self.po = []
    def add(self, item1, item2):
        self.po.append(item1)
        self.po.append(item2)
    def inspect(self):
        return self.po

def SetUp(Comp, po):
    c = wmi.WMI(Comp, user=fr'{Comp}\{username}', password=password)
    process_startup = c.Win32_ProcessStartup.new()
    process_id, result = c.Win32_Process.Create(CommandLine=fr"c:\{po} -silent -norestart", ProcessStartupInformation=process_startup)
def get_po(Comp):
    c = wmi.WMI(Comp, user=fr'{Comp}\{username}', password=password)
    my_programs = Programs()
    for p in c.Win32_Product():
        my_programs.add(item1=p.Caption, item2=p.Version)
    return my_programs

Comp = 'pc1'
username = 'la_gugl'
password = 'Ueukz008'
print(get_po(Comp).inspect())
# SetUp(Comp, 'cades.exe')


