import os
import time

source = ['"\\home\\ivan"', '\\Code']

target_dir = '\\home\\ivan\\Backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

print(zip_command)

if os.system(zip_command) == 0:
    print('Sicces', target)
else:
    print("Error")
