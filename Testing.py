import urllib3
from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.model import fv
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

apicUrl = 'https://10.10.20.14'
LoginSession = LoginSession(apicUrl,  'admin', 'C1sco12345')
moDir = MoDirectory(LoginSession)
moDir.login()

print("Login successful")

#User the connected moDir queries and configuraiton ...
moDir.logout()
