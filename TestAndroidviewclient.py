#easy_install --upgrade androidviewclient
#https://forum.xda-developers.com/general/xda-university/guide-python-automation-using-dtmilanos-t3274345
from com.dtmilano.android.viewclient import ViewClient
device, serialno = ViewClient.connectToDeviceOrExit()
vc = ViewClient(device=device, serialno=serialno)

print "################## Settings application test ####################"
device.startActivity('com.android.settings/.Settings')
print 'TEST : PASS'

