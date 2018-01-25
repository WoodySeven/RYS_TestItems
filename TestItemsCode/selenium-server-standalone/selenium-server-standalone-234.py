import time
from selenium.webdriver import Remote
import sys,traceback
import threading

IP = '192.168.1.100'

host_dict = {#'rs_ff':("http://%s:5555/wd/hub" % IP,'firefox'),
             'rs_ie':("http://%s:5555/wd/hub" % IP , 'internet explorer'),
             'rs_chrome':("http://%s:6666/wd/hub" % IP , 'chrome')}

desired_capabilities = {'platfrom': 'ANY',
                        'browserName': 'firefox',
                        'version':'',
                        'javascriptEnabled':True}

def run_browser(host,desired_capabilities):
    driver = Remote(command_executor=host,desired_capabilities=desired_capabilities)
    driver.get("https://www.baidu.com")
    time.sleep(5)
    driver.find_element_by_id("kw").send_keys("remote")
    driver.find_element_by_id("su").click()
    time.sleep(5)
    driver.quit()

def main():
    threads = []
    for i in host_dict.keys():
        host,browser = host_dict[i]
        print(host,browser)
        dc = desired_capabilities.copy()
        dc['browserName'] = browser
        threads.append(threading.Thread(target=run_browser,
                                        name=dc['browserName'],
                                        args=(host,dc)))
        for t in threads:
            print(t)
            t.start()

        for t in threads:
            print(t)
            t.join()
        print("ALL done")


if __name__ == '__main__':
    main()
