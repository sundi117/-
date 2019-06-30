'''
class LazyImport:  
    def __init__(self, module_name):  
        self.module_name = module_name  
        self.module = None  

    def __getattr__(self, funcname):  
        if self.module is None:  
            self.module = __import__(self.module_name)  
            print(self.module)  
        return getattr(self.module, funcname)  
u = LazyImport('urllib') 
'''

import time
print("请稍后....")
time.sleep(3)
# 使用exec
import_urllib_request = "import urllib.request"
import_urllib_parse = "import urllib.parse"
exec(import_urllib_request)
exec(import_urllib_parse)

# 1、保存网页到路径

url = "http://www.baidu.com"
content = urllib.request.urlopen(url=url).read().decode()
print(content)

with open("baidu.html", "w", encoding="utf8") as f:
    f.write(content)
