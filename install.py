import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 ipkitty2.py')
    run('mkdir /usr/share/ipkitty2')
    run('cp ipkitty2.py /usr/share/ipkitty2/ipkitty2.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/ipkitty2/ipkitty2.py "$@"')
    with open('/usr/bin/ipkitty2','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/ipkitty2 & chmod +x /usr/share/ipkitty2/ipkitty2.py')
    print('''\n\ncongratulation ipkitty2 is installed successfully \nfrom now just type \x1b[6;30;42mipkitty2\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/ipkitty2 ')
    run('rm /usr/bin/ipkitty2 ')
    print('[!] now ipkitty2 has been removed successfully')
