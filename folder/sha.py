import os
import hashlib
sha1 = hashlib.sha1(os.urandom(256)).hexdigest()
