# encoding=UTF-8
# https://gist.github.com/anonymous/7568323
import telnetlib
import sys
import PttAccount #My file. It contains Account.id, Account.password 
import time
tn = telnetlib.Telnet('ptt.cc')
time.sleep(1)
content = tn.read_very_eager().decode('big5','ignore')
print("首頁顯示...")
if "請輸入代號" in content:
    print("輸入帳號...")
    tn.write((PttAccount.account+"\r\n").encode('big5') )
    time.sleep(1)
    content = tn.read_very_eager().decode('big5','ignore')
 
    print("輸入密碼...")
    tn.write((PttAccount.password+"\r\n").encode('big5'))
    time.sleep(2)
    content = tn.read_very_eager().decode('big5','ignore')
    
    if "密碼不對" in content:
        print("密碼不對或無此帳號。程式結束")
        sys.exit()
    if "您想刪除其他重複登入的連線嗎" in content:
        print("發現重複連線,刪除他...")
        tn.write("y\r\n".encode('big5') ) 
        time.sleep(7)
        content = tn.read_very_eager().decode('big5','ignore')
    #print(content)
    while "任意鍵" in content:
        print("資訊頁面，按任意鍵繼續...")
        tn.write("\r\n".encode('big5') )
        time.sleep(2)
        content = tn.read_very_eager().decode('big5','ignore')
        
    if "要刪除以上錯誤嘗試" in content:
        print("發現嘗試登入卻失敗資訊，是否刪除?(Y/N)：",end= "")
        anser = input("")
        tn.write((anser+"\r\n").encode('big5') )
        time.sleep(1)
        content = tn.read_very_eager().decode('big5','ignore')
    print("----------------------------------------------")
    print("----------- 登入完成，顯示操作介面--------------")
    print("----------------------------------------------")
    print(content)
 
    print("\n\n\n\n\n\n\n")
    print("----------------------------------------------")
    print("------------------- 登出----------------------")
    print("----------------------------------------------")
    tn.write("qqqqqqqqqg\r\ny\r\n".encode('big5') )
    time.sleep(1)
    content = tn.read_very_eager().decode('big5','ignore')
    print(content)
    tn.write("\r\n".encode('big5') )
        
else:
    print("沒有可輸入帳號的欄位，網站可能掛了")
