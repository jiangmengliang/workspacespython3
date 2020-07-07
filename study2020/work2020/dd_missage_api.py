import time
import hmac
import hashlib
import base64
import urllib.parse
import subprocess

key_word = '监控报警'
# text_msg = '我就是我, 是不一样的烟火'
text_msg = 'this is my test!...'
timestamp = str(round(time.time() * 1000))
secret = 'SEC41526abf388543beac7ff3894781052efec88bb10910230dc38b10b083936414'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)
api = '''https://oapi.dingtalk.com/robot/send?access_token=a33d118e3cbd0ed21d6a8fcbbade8c2ae99ad9b6cbee89ec2e1534c5b0d683b8'''
sign_api = '''curl '%s&timestamp=%s&sign=%s' '''%(api,timestamp,sign)
msg = '''-H 'Content-Type: application/json' -d '{"msgtype": "text","text": {"content": "%s：%s"}}' '''%(key_word,text_msg)
send_msg = '''%s %s'''%(sign_api,msg)
print(send_msg)

(status, output) = subprocess.getstatusoutput(send_msg)
# print(status,output)


