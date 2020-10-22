from win10toast import ToastNotifier
import time


def new_push(list1,no,c):
    toaster=ToastNotifier()
    if no==0:
        toaster.show_toast(f"{c} ",f"{list1[0]} New Cases have been Reported ", threaded=True,icon_path="corona.ico", duration=8)
    elif no==1:
        toaster.show_toast(f"{c}  ",f"{list1[0]} New Cases and {list1[2]} New Deaths have been Reported", threaded=True,icon_path="corona.ico", duration=8)

    while toaster.notification_active():
        time.sleep(0.1)



def empty_notification(c):
    toaster=ToastNotifier()
    toaster.show_toast(f"{c}",f" No New Cases to Report ", threaded=True,icon_path="corona.ico", duration=8)
    while toaster.notification_active():
        time.sleep(0.1)

def total_cases(dict1,c):
    toaster=ToastNotifier()
    toaster.show_toast(f"{c}",f"{dict1['Coronavirus Cases']} Total Cases , {dict1['Deaths']} Total Deaths and {dict1['Recovered']} Recoveries have been Reported ", threaded=True,icon_path="corona.ico", duration=8)
    while toaster.notification_active():
        time.sleep(0.1)
