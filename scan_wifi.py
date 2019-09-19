import os
import subprocess


def getch(f):
    if f == '2412':
        channel = '1 '
    elif f == '2417':
        channel = '2 '
    elif f == '2422':
        channel = '3 '
    elif f == '2427':
        channel = '4 '
    elif f == '2432':
        channel = '5 '
    elif f == '2437':
        channel = '6 '
    elif f == '2442':
        channel = '7 '
    elif f == '2447':
        channel = '8 '
    elif f == '2452':
        channel = '9 '
    elif f == '2457':
        channel = '10'
    elif f == '2462':
        channel = '11'
    elif f == '2467':
        channel = '12'
    elif f == '2472':
        channel = '13'
    elif f == '2484':
        channel = '14'
    else:
        channel = '5G'

    return str(channel)


def getes(e):
    flag = 0
    essid = ""
    if "\\x" in e:
        ess = []
        strTobytes = []
        for i in e.split('\\\\x'):
            if flag == 0:
                ess.append(i)
                flag = 1
            else:
                if len(i) > 2:
                    number = int(i[:2], 16)
                    strTobytes.append(number)
                    # print(i)
                    ess.append(bytes(strTobytes).decode() + str(i[2:]))
                    strTobytes.clear()
                else:
                    number = int(i, 16)
                    strTobytes.append(number)
                    #print(strTobytes)

        if len(strTobytes) != 0:
            ess.append(bytes(strTobytes).decode())
        for e in ess:
            essid = essid + e

    else:
        essid = e
    return essid


def geten(en_way):
    if en_way == '[ESS]':
        return '       OPEN        '
    elif 'WPA2-PSK-CCMP+TKIP' in en_way:
        return 'WPA2/WPA2-CCMP/TKIP'
    elif 'WPA2-PSK-CCMP' in en_way:
        return '   WPA2/WPA-CCMP   '
    elif 'WEP' in en_way:
        return '       WEP         '
    else:
        return '      802.1x       '



def scan():
    global AP
    AP = {'signal': [], 'ESSID': [], 'TYPE': [], 'BSSID': [], 'Channel': [], 'WPS': []}
    os.system("wpa_cli -i wlan0 scan")
    proc = subprocess.Popen("wpa_cli -i wlan0 scan_resul", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    lines = str(proc.communicate()[0]).split('\\n')
    flag = 0
    for line in lines:
        if '\\t' in line:
            info = line.split('\\t')
            #print(info)
            AP['BSSID'].append(info[0])
            #print(info[1])
            AP['Channel'].append(getch(info[1]))
            AP['signal'].append(info[2])
            if len(info[4]) == 0:
                if flag == 0:

                    ess = "<隐藏wifi>"
                    flag = 1
                else:
                    ess = "<隐藏wifi>"
            else:
                ess = getes(info[4])
            AP['ESSID'].append(ess)

            AP['TYPE'].append(geten(info[3]))
            if 'WPS' in info[3]:
                AP['WPS'].append('YES')
            else:
                AP['WPS'].append('NO ')

    print("NO" + "        " + "BSSID" + "      " + "Ch" + "        " + "En-way" + "        " + "WPS"+" "+"Sig" + " "
          + "ESSID")
    for i in range(len(AP['ESSID'])):
        if i < 9:
            print(str(i + 1) + "  " + AP['BSSID'][i] + " " + AP['Channel'][i]
                  + " " + AP['TYPE'][i] + "  " + AP['WPS'][i]+" " + AP['signal'][i] + " " + AP['ESSID'][i])
        else:
            print(str(i + 1) + " " + AP['BSSID'][i] + " " + AP['Channel'][i]
                  + " " + AP['TYPE'][i] + "  " + AP['WPS'][i]+" " + AP['signal'][i] + " " + AP['ESSID'][i])
    print("AP个数为：" + str(len(AP['ESSID'])))


if __name__ == '__main__':
    scan()
