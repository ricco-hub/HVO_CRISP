import requests
import shutil
import os
import time

shutil.rmtree("Download")
os.mkdir("Download")
m =int(time.strftime('%m'))
d =int(time.strftime('%d'))

shutil.copy("ForceFieldPHI.root",time.strftime('Download/ForceField_PHI_'+str(m)+'-'+str(d)+'-'+'%Y.root'))
shutil.copy("ForceFieldJMOD.root",time.strftime('Download/ForceField_JMOD_'+str(m)+'-'+str(d)+'-'+'%Y.root'))
