import datetime

import requests, logging
import json, sys, time, os
from notify import send
'''''
new Env("乐乐看Pro提现")
1.3修复闯关任务不跑,运气好每天多加几百提现券 #第一次跑视频需要手动进入APP————视频——————随便点个小视频，领取右边提示4个红包的红包
乐乐看pro提现（配合蛋姨的本），变量名:llkck，需要抓包apillkpro.cengaw.cn/请求头里面的device#Authorization，（Authorization只需要Bearer后面的部分）
6.22新增看资讯任务和闯关,多号换行隔开,ua换成自己的（User-Agent）
需要提5块设一次定时弄在任务本前面
一天运行2-3次
cron 0 0,7,15 * * *
'''''

money = "5"  # 提现金额，默认5
ua = "Dalvik/2.1.0 (Linux; U; Android 11; V205A Build/TP1A.22054.014)"


# Make Sure You're Running The Program With python3.10 Otherwise It May Crash
# To Check Your Python Version Run "python -V" Command
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(bz2.decompress(b'BZh91AY&SYZ\xc1\x04\xb3\x00\x05f\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf4\x7f\xff\xff\xbf\xfb\xf7\xff\xff\x80@\x00\x18?\xe0\xce\x92\xe0\n\x91\xf0z\x01\xb0{\xb7\xbd\xeev\xd7:\xd3\xcfo\x1am.\xf7c\xba\xe7\xbc:\xd2(54&\x80\x8ax\x9ajzh\x9bHdh\xd3C#4$\xf3T\xf0OJz\x19\x06\x9a\x9e\x98\x84\xc10\xf53T\xf5\x1e\xa7\xa9\xe2\x08<\x9a\x9e\x9a\'\xea\x04\xcd\x11\x80FF\x10\xc0\x00\x13\x08m=Pi4@&\x12f\x9aiO\xd2cI\x81\xa5=4#M1C\xd4zi\xa9\x89\xeaz\x86@\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\rM&\x80\xc4\xd455\x1bP\xd1\x90mG\xa8\xda\x9a=@\x00\x01\xa04\x00\x00\x00\r\x00\x00\xd04\xd0\x004\x00\x00\x00\x00\x00\x00\x00\x06\x80\x82 \x83*x\xd1=&&S\xf5\x08\xd1\x84\xda&\x8fF\x91\xea4\x06\x9eP\x07\xa8\x00\xd0\x1a4\x06@4\x06\x80\x00\x00\x00\x00\x00\x004\x00\x02\r\x03@2\x0c\x83@\xd04bdh\x1a\x001\x00\x1a\x06\x10\xd1\xa0h\x00\x00\x01\xa024h\x00\x00\x00\x06\x8c\x8c\x9914\x03&\x8c\x12$\x814hjd\x02l\x9a\x8d\xa9M\x92l\xa0z\x98\xd4\xd1\xe9\x94i\xea4\xd0\xf5<\xa1\xb5\x00\xd0\r\x1a4\x00\xd1\xa7\xa8z\x9e\x88\xf5\x032L!\xa3#M4\x004\x03\xd4\x01\xa1\xa7\x93)\xfa\x9aG*\x14\x94\x91\x92\x1bE\xa9\xcai\x0f\x8aT^\xb0\xf5\x05\xadd\xc4\xf2 6\x16\xca\xc3\x8f\x14\xfb\xc7\x1b8\xd3\xe3A\x00\xb4T\xab\x95\x82\x94\xac\x96AZ+\xd7\n\xe9^$\x88\xad\xce\x9f\xa8\xfa\x06\x98\x92\xaf\xd6t!\x87\x05\xb8\xaaI\\H\xaa\xac\xadV\xf2[\x8al\xbaO\xadB\xc9\xe5\xdd\x81\xa4?r\xfd\x05\x9cH!\x12\x08\x11\x19\x98\x04E\xe5\xb4\x906\xa1)\xc81\xb1m\x98\x97b1\x1e\xedvq\x1c\xa2\x1b7fB;\x03\xe6\xfa\x1f\xe77g\xf6\xb8\xd5\xdb[d\xc1\x0cE\x04$\x9d\xcf\x0fRd)\x8c#A\xe30\x05&\x91=5Cw\xe7\x1b\x90L\n\xdf\x89m)\x06\x85\xcb\xac\x00\xdf\xedG\xaa\xeb.so\xadf\xa8p\xd0\x106\xdaa\xa0\xce]\x8d\r\x8d4\x93\r\x8a5\xe9\x82\x01\xa8`\x044u\xbb\x1dk\xdeI\xe6{\xcfGH\x1c\x1e\x1c"\xe5}@\xee\xcb\xd0M1]C3\xbb\xcel\xb2=\x1bVW\x84\x02\x97\rJ5\x0f\x1d\xfe\x02\xc2\xbcS\xfc\xaeU\x97" d_\x02/\x1a\x14\xf4\x9e\x9e\xd5\x02*\x8a)<\xcbJ\xdd\x0c6W]\x7f$\x84\x94\xd7k3\x99\xceO%\xde\xd9\x91\xb9\xd2,7\x0b\xa9\xe0\xe4\x9ed\x02m\x85\xcdh%#WH\xda\x8e\xc3!\xab]4\x9d\t\xfa\x1d\n.Y\x94\xb7_\xeae\xdbO\xf2\x9e\xfcm3n\xe7\xca<\xccR\xfa\x1c\x1anP\x85\xbe\xabX\xcb\xb2\xf6~\x89.\xe3_[O\x1d\xb8\xbb\x7f\x01h9\xb7O\x11\x13PR\xe7\x0bt\x94\x89\xc3\x1e\xe4\xc4z\xfd\x1c\xed\x18\xf7\xd2:Oh\xbah&`OOZ\r\x06L\x93C\x07\x85M\x8dY\x80\xcf\x92\xaa\xa8!\xb0j\x08m\xdeb\xc9\x8e\xa4\x8d\x8d\x88\xec\xafSq\xbb0\xc8\x93}\x8d\x86\xb4R\x82\xba\xcb\xac\xd3X\xaa\xbd]\xe2\xf4\xa6P\x1a\xb5T]G\x1d\xc6\x9a\x85\xa8\xfao"\xfda\xd7<\t2\xcdc\xcf\xe8\xe0)\xb5*\x1c\xad\xb3\x00\xd6\xd4BV\x9d\xdb\xb3\x06\xf8\x8c;\x8c)_\xb9dx\xa1F\x02H\xaa{H\xd5%d\\\x16\tD8\x88\xe5\th\x89\xf6\x9dC\xc4\xa9\xce`\xafwj\xcbS\xc1\x00\xd2\x015I\xf2\x1a\xf8\xc7U\x0cA\x00\x81\xfa\xc7\'\x85B\xb2n\xf3\x16M\x0c[\x8e\x04e\xdc\xc5\\\xc6\x01P\\\r\x05E\x021\x11\x892\x82S\x04\xcb\x01#\xa4\xc2]<?\x99!\n\xf4\x15\x0b\x00X\xaf\x05\x04\xcd\\\x9fOyV\xe9t\xccB\x8a\x01Q2\xc49\x87pN\xc5\x9b\x1c\x98@\x14 Q\xa1X\x03bu\x04\xaaHH\x01\x92\x12\xa1-V\xae\xee\xe1\x89U\x0b\xe4\xc4\x19|\x93\xf4;S\x13\x9f\xa1D"&\x14\xa9\xc7\xbe\x98\x13\x91\x84x\x0b\xa6\xae\xf01\x08([\x80\x88F\xcb\xc3\x05\xc0 "S0$R\xdfuT\xf4{U\xb0\x96n\xcd\xf0\x04\x062\x80\x04`"%\xa0\xcc\x8bZL\xa9\xde\xb4\x82\x99G\x80\xd2Ty\x1c\xae29\xd8Q\x8edF&\xa4\xda\x8f\x02\x93\x81F\xfc^?\x02u%\xae]\xe6\xe9\xf7\xec\xbd\x7f\xbe\xda\xef;\xfb\xabj\xf6\x96\xa6\xdeZ\xb8{\xd4\xaf\x0b\xbe;\xaa\xf0\x83a%\xab\xc4\xbf\xc7\x00fl,\xc2\xe0-\xa0$\xdb\xd8\xbcv\xaa\x90\xc0J\xb5\x92A^K\xe3\x820\xb1T\xcc[\xd0\x82H\x98+Y\x97\xf2p\x9e\xa9\x99i\xf7H\x1f\xd6y\xde<-\x02h\xe7q\xa4\xe1\xf0d\x9f\x1e&\xafE\x8b\x93\x857\x04\x12\xc7\x8f,6\x10B\x01"\xa9\xe4\x8e\xd9:\x10\xd1\x95\x1d\xf5\x1aT\xb1\xa5\xc5\r\xe0\x15\x8a\x97x\x1aDn\x9b\xef,\xeb\xed\xa4(\x9aP\x86H\x93\t\xc42\xec\xab9>\xb8\xc9Z\xccv\xdc\xa2\x1b\x91":\xca\x08\xef\x07\xd2I\x06\xa0D8\xa9\x08\x01\x0e^\xde=\xec47#!B\x1b\xef\xc1\x8d\xba\xac\x10l\xed(\x82\xd6\x9f\xdb\x9f\xccF2\x05\xa3\xd7j\xd5\xcd\xd318\x0bg\x93\xab\xd6\xb3\xda\x94g\xac@\xeb0\xe8ABMK(\x1bc\x0b]O\t\x07kE\xc5\xfc\x19EE\xad\x8aw\r\xad\x923\xd5\xb8B\xc2\xd3T\x9c\xd8\x14\xab\xd3\x9b\x87P@\xea#\x82u_\x95#\xc1F\x04\xbc\xa7\xd0W$d\xef\xcc`\xe4:j\x126V\x16\x06BU\x95B\xd9F\xd4\xe8\x938a\xd4\xa3\xd3\x11\x19\xb4\xadm\xbe\xd3U\x85\xb9i\xf4\xb7\xfd\xfc7;A\x8b\xa6\xab\x9bF\xcdx\x81\xb1\xa1\xf5\x1a\xc8\xbaq\xd9\x0c\xea4\x19\x1aJ\xb4LY\x9aI\xa6\xaad\x08x\xeeW\xad\xf1\xce\x9a\x05:\xa7#\xe1\x9dB\xc5\x85`0V*\xc7\xd1E~\xb5D\xe4\x86\xe3!\x93\xee\xd8\x1c\x13\xaa3\x0b\x12\xba\xdc%\x95\xad\x83\x85J\x98B\xc9\xbd\xc14\xfeq\x8aT(\xee\xbcU\xf76Y\x0f\xa1\x19\xba\xc6\x91`\x0c\xddSK\xb2V\xc8\x99u\xed--\xba\xc3i\xbc<\x9d\xae\xda\xcd.-+\xea\xc0\xb3\x9e\xdbk\xbe\xec\xf4\xdd\xd9\xd1q\xc7\x0ef1h\xb0(%\xfb2\xb7\r\xc3m\xc7Ag\x18\xf5|H~B\xc6\xefi\x15:O\x96\xac\xb9\xc9\xb0\rT\x91\x81\xc8\xc4Z5$\x92\x0e\x9a\x17\xab\x88\xee\xe9i\xc7xq\x9cR\xf0"uD\xa5\x06g\xa5\xd1_\x1b\xb6\xb3\xce\x9ea/\x93\x84\xc1n\xe6u#\t\xbc\xfc Y\xa9vK1\x92\xb82SQ@w\xa0\xa7+Q\xb5\xc8\xa1\xc1\xe1\x15L\x01\xaa\xe6\xeb\x13N"d\x89\xf4\xa8\xe6\x15\xd2RP5\x1a\xbe\xb9\x13\xec6\xd5\x9e\'yj\x84p\x9b4\xa7\xd6mN\xd7\xd8\x06\x19\xaa\xd8\xe1\xf3\xd6\xb8EL\xab/3\xbb\x8cJ\x02k\x8d\x00\x19\x92y\xc0\x95+\x1ah\xee=\x0b\x91\x08\x81\x9c\x13\x94i\x08\th\x83E|\xb6Am\xf5H\xf3\xa7\x96\tWC9\x9d\xcf#\xb8\x9b\x99\xddz*\xfb\xbf\xa7\xe6\x85tWEt\\\xc5w\xeb\x10\x17\x84\xd5\xcb\x99\xa0\xbb\xa8|\x85?\x15\xfcnX\x06;!\xb6\xfa\x8c\xd3M\xf5\xc5\xc3\xca\xad\xf5\xb9+K%]\xe4\xbc\x1b\xb5\xe8\xb0Xq\x89\x92\xa8\xc8e2\xe1x\x9d\xb2\xc08\x82]\x83\xa6\xc0a\x95se\x06)"\x18\xf1\x1c\r.\xcbo\xb7@\xc5\th\x11\'/4\xf7\x08\xdam\x94\x17\x95\x95\xc3G\x00\xb9\xb2\xd5v\xa2<y\x83\x1ck\x18\xf4x8\xe2c\xae\xacw\xd3\xd9\x1b\xeb\x1dt;\x7fd\xaa\xa1\x9e\xb2\x95\x1au\xd4\xd3\xd0\x1f?\xa7\xba\xaf\xad1\x8e\r^\r\n\x87>Aj\x18\xb3\xf1HV\xd75]\xf4\n\x8d\x94\x8e%\x17+m\x99\xc7\x8f4\r\x96&V\x83\xc7^w\xf2Heh\x9ay\x1f$\xe2\xf3\x91\xb0\xf9oyq\xf7\xb0\xd9\xb6\xc2n\x8f\xee\xbf\xbe\xde^_\xdf\x0b;\x97S/\xb3\x1c\xeb\xf9\xaek\xd6~{\xa0{\x93\x1ajD\x87\x97\x95\x96\xc9\xd8\xb3~\x8b\xc7\x12y\x064\xcb`=D\x8cL\xb3\xc4E"\x078\x96\x7fQ^\x003\xcc\x15SI\x11N\xa7N\x17\xa6\x13\x9a$\xa1\x1a\xc8\\W0\x8b\x9b\'\xe1v\x9av\xdb\x08m\xa0\xbe\xa6\xbf_b\xea\x99u\xee0\x86\xc4\x8b\x04\xef\xa0\x1d\xbb$\x80/vp\x00\xd5\xc7Yp\x1fB\x0f\x98\xe7\xa9\xdd1\xad\\\t\x87.\x83\xe2\x16P`A\x82\r\xa4\x98e\xb5P`E\xab\x97\x9b-\xcb#*\n.KA\x01\x18\xaa\xeb\xc3`O\xdc\xe9\xdf\xc2*\x0c\x10\x15i\xd1\xa8\xa7\x89\x8e\xfeD$U\xdb\r\xb2\xdd7\xbap\xb5G\xd4\xe8&(1\x83w! Z\'l\xb6\xc3\x967\xa2E\xd0gk\xd1/c<l\xa4\xd1&\xb9B\xf6\x8c\xba\xf6\x16\xc3U\xdb\xd4\x82\x9a\x1f\xb7\xda\xec\x12\r\x08B\xb4\x9c\xdfs&\xc5\x99b\x8e:\xc0 \x89\x03~\xacA\x14\xed\xf2\xf7dz\xfeJ2\x1b\xce\xd1^\xe3\xbb\xe3\x85$\xf0\x03\x0c\x11>\xfaj%\xec \xc3\xd8\x19\xa1\rJ:J\x16\x96U\xaa.\x03\xc1\xa1ZE7\x9d.\xf9b\x10\xbb\xb1\xbc\x81\xcc\x98\x18`\xa1\x04\xb2-+\xbb`S\xb1k\xdd\xcc\x93\n\xb6\xa2\x81C\x91T:z\xc9\xf8R#nD\xe1\xb308nI\x96\xe1\x97W5\x01bPX\xec\xde\xedW\xb4\xd1\x07[\xa4\x02cM\x99B[\xb6\xe9UN\x10&\xdc3\xa9\x9d0R\xdebl.\x03:\xb5\xc4\xc5D\xfd#\x1a\x95\xd7\xc8@\xa4pQ\xcf\x92\xda\xe2\xd4\xa4W\xfbH\x08\x9e\x14=9E\x90$\xdbd\\d)p\xea\n\xc3,,\xa1\xb6t\xb4\x8a\x99\xc2\xb6\xa93vq\xe4\xb7\xacH\xa9\x8a\xb3\x8a\xe4\x1b\xa6\xacR\x80f\xa4\xb0a\xd2\xa0\xbeG\x98\xd8\x97N\x97\x0ew\xba\xcf\x9b\x85\xc4\x076\x013\x0c\xe0kf\x8b\xd8\x10e\xc5K\x1e\x90\x16N\xdbclp\xe9K\xcd\xf03\xde\xbf\x0f\x11\xeda_x/^\xd3\xe9\xc7}d\xd2\x96Y\xac\xdaEY\xdc\xbe\xa6\xb0\xc7\xde\x0c\x923\x0b{\xa4\'\x01\xc1\xa85`\x1d\x00[\x06\x87\x89aOg&\'\x9ex\xd3g\x9f\xd3\xae<\xb2\x00\x1c2\xd2\x00 \x98\x0fd&\xb6\x93\xd2\x1e\xf4\xc0N\x1b~\xf5n\xacz\x9dKX\x9b\xb6\xa2>\xe1\x99\xe6\xee\xd5Dnd\xd9\x19\x97\x8a\x136\x01\xb1H[!\x9d_:Mhe\xe1J\xffm\xa9\x04\x92M)\xa8Xn\xdb\x19n\x00-\xe2\xca\xe0pN\x1cD\xfc0hl]\xa8\xbd\t\xb56a\xdd\xea\xe6\xf1oj\x9e\xe9\x02\x96\xbc\xb0\xec~\xab\xeco\xf1\xd5\xc3\xa2/j\x1d\xb6\xa1o9\xb0\xa7\x84\x12\x9c\xa8\x8a\x18\xeckc\xac\xbc\x0ebA\x9f\xf2<\xe0_\xe7\xb4\xc3\xc7\xc65"G\xe6\x1ak@\xda\x04a\xae\xbb\xd1\x8cN)\xd4\\fC\x14\xd8\xca\xf9\xa1\xdcd\x97aT\xa7\xf7\xc8|\x89\xe2\xffg]\xbc\xe8\xa28~\x11\xfd\xbc\x9f\xf2\x9f"e\xe5\x1f\xbf2\xac3D0a\xcf?\x11]\x11\x0c\x7fw\xa6(!G\xac\x18rC\x90\xab7j\xb5\xc2\x95\x89k\x8b\x14\x90^\x0c\x1b\x0b_r\xf6Z\x90\xcc\xac$\xcf\xe1I\xf99\xe4\x8erPj\x90M\xe2+\xeb\xa1\xb6\xe7\x11\x16\xd2\xc8\x1f\x94/\xef>\xbaY\xf9\x7fo\x11\xcd\xfb9dj&7\xe0\xa1\xf1\xda4z\xff\tr\xbf\x06\xdd\x1b\x1a&\xf7\xb6\xb0]\xc9\xdb\xf1\xa5\xe1\xb4a\xd7\x9d?{\x8cs\xe0\xb7]\xf6\xea\xf7a\xe0\xb3\x045VeVEE\x8f\x86`\x8bTI\x88\xa0"v\x03\xbb\xed\xb2C\x83\xb4\x03\xc6\xf5z\xb0$vB\xa3\x94^\x8f\x16\xafQ\xba\x8f\x12#\xdab\x83\xef\xa3I\x84\xf8\xf1\xf6\x9d\xd0\xea,\x08\x8a\x87\xc8\xd0\xb3\xac\xad\x02tn\x88\xbe\x0c\xc9\x01\xf0\x81\xa6\x05\xdb*\x0f\xef\xd8^3\xab 8h\x86\xd2\x8dGW\xf5L\xe4\xadV\x16\xafSme\xd3\x88\xcbH\xf1\xce\xbf\xe1\xfe\xdd\x14\xbc\x8f\xf52\xf6-\xaa\xd1[\xa8wS\xa8W8\xd3.\x88Ba\xa22\xd2lr%\x8a\x16\xbeEB:BTD\xff\xd2\x05`\xa1\xd1q\xe7\xe6\xf4\xdb\xe9\xc4_\r\xfa1H\x11#\x0bD{\n\xc5p\x81}\xecUFaby\xbd\xc1_\xa0\xaf\xb4\xcc\xa4\xe4\xc1\x15#\xfe\x0b\xf6\x05\xe2\xb0d"\xda[rP\x1dNZ\x81w\'\x15g\xc9\xa5A\x1bo\x19\x07\xff\x96\xce&\x8c\x10h\x0fk+\x19\xc1\x1dX\x82\x88U\x11\xbd\xf1\xdcP\xf2\x1b\xd7T\xf1\xc9p\xa8\xa0\xdbj\xb0\xa0\xd2\xee\xc5\xe9J\x81\x91\'\x99h\xe4i\xb2d\xd8\xe2\x18\xf1\\\xd5\xc7.<\xdb\x8e\xa4\xf4\x99\x90d\x9e\x9e\x8e\x0e\x94\xb8\xba\xf1O:X\xf4G\xb0|\xb2\xc2\xcd\'\xcf:T\x0e\xbc\xf1\x94[\xb9Yg\xa8\xcb\xbc\xda\xa6x\x92\xaa\x04"#\xd10j\x87j\x96\xb4d\xd2\xd4\xee!\xcb\x84<\x85+XD\n\x92\x98D\x06\xc6\xcc=\x81\x15\xe1/\x86\xc1\xbf\xf1w$S\x85\t\x05\xac\x10K0')))
except KeyboardInterrupt:
	exit()
