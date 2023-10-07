import shutil
import win32wnet
import wmi

def pusk():
    win32wnet.WNetAddConnection2(0, None, '\\\\192.168.0.106', None, r"pc1\la_gugl", "Ueukz008")
    shutil.copy('cadesplugin.exe', r'\\192.168.0.106\C$')
    win32wnet.WNetCancelConnection2(r'\\192.168.0.106', 0, 0)
    return 0

def start():  # Запускаем программу или комманду на удаленном ПК
    try:
        c = wmi.WMI('pc1', user=r"pc1\la_gugl", password="Ueukz008")
        process_startup = c.Win32_ProcessStartup.new()
        process_id, result = c.Win32_Process.Create(CommandLine=r"c:\cadesplugin.exe -silent -norestart", ProcessStartupInformation=process_startup)
    except wmi.x_wmi:
        print(' Ошибка (логин\пароль) функция start ')
    return 0

def checkPo():
    c = wmi.WMI("192.168.0.106", user=r"pc1\la_gugl", password="Ueukz008")
    for oss in c.Win32_OperatingSystem():
        print(oss.Caption, oss.OSArchitecture)
    for p in c.Win32_Product():
        print(p.Caption, '-------------', p.Version)

def func():
    p = 90
    print(locals())

func()
#pusk()
# start()
# checkPo()