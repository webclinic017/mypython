from jnpr.junos import Device
import sys
import threading
import time
import win32com.client
from jnpr.junos.utils.start_shell import StartShell


class JNPRdevops:
    def __init__(self,):
        self.healthcheck_list=[]
        self.err_list = []

    def sendmail(self,to, title, body):
        olMailItem = 0
        ol = win32com.client.Dispatch("Outlook.Application")
        msg = ol.CreateItem(olMailItem)
        msg.To = to
        msg.Subject = title
        msg.Body = body
        msg.Send()

    def filecopy(self, server_name,filepath,users,password):
        return 


    def healthcheck(self, A,users,password):
        if not A:
            print "not valid"
        dev = Device(host=A, user=users, passwd=password)
        try:
            dev.open()
        except Exception as err:
            self.err_list.append([A,err])
            print err
            sys.exit(1)
        print dev.facts
        self.healthcheck_list.append(dev.facts)
        ss=StartShell(dev)
        ss.open()
        ss.run('cli -c "request support information | save /var/tmp/information.txt" &')
        ss.close()
        dev.close()

def show(arg,a):
    time.sleep(1)
    print('thread '+str(arg)+" running....")
    print a


def main():
    return

if __name__ == "__main__":
    main()
    k=JNPRdevops()
    l1=["10.85.173.179","10.85.173.178","10.85.173.177"]
    print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    for i in l1:
        t = threading.Thread(target=k.healthcheck, args=(i,"labroot","lab123",))
        t.start()
    t.join()
    str_list=""
    for i in  k.healthcheck_list:
        str_list+=" "+str(i["hostname"])+"\n"
    k.sendmail("owenyang@juniper.net", "replication", str_list)
    print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
