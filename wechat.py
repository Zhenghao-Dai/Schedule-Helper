from __future__ import absolute_import, unicode_literals
import os
from flask import Flask
from flask import request, make_response, jsonify
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message
from wechatpy.replies import TextReply, ImageReply
import schedule_api as api
TOKEN = os.getenv('WECHAT_TOKEN', 'lucasdai1998')
app = Flask(__name__)
storage = []
@app.route("/connect", methods=['GET'])
def on_get():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    encrypt_type = request.args.get('encrypt_type', 'raw')
    msg_signature = request.args.get('msg_signature', '')
    try:
        check_signature(TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException:
        pass
    if request.method == 'GET':
        echo_str = request.args.get('echostr', '')
        return echo_str


@app.route('/connect', methods=['POST'])
def on_post():
    xml = request.stream.read()

    msg = parse_message(xml)
    if msg.type == 'text':
        a = api.schedule_api()
        try:
            msg_content=msg.content.lower()
            if 'help' in msg_content:
                result="Enter 'list (course id) to see all section under the course \n Ex: list csci-102 \n \n Enter course to see course availability \n Ex:csci-102"
                reply = TextReply(content=result, message=msg)
                xml = reply.render()
                resp = (xml)
                return resp
            if 'list ' in msg_content:
                course_id=msg_content.split("list ", 1)[1]
                
                course_dict = a.get_list_course(course_id)
                result="Your request of "+ course_id +" has those sections: \n"
                for i in course_dict:
                    result+=(course_dict[i]['type'] + " section " + i +" has " + course_dict[i]['remain']+" spots \n")
            else:
                num = a.get_course_remain(msg_content, 0, "Lecture")
                result = msg_content+" \n current has " + \
                    str(num)+" spots available"
        except:
            result = "Please enter correct information or type 'help' for help"

        reply = TextReply(content=result, message=msg)
        xml = reply.render()
        resp = (xml)
    return resp


if __name__ == "__main__":
    app.run()
