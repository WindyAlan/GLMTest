from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True, revision="v1.1.0")
model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True, revision="v1.1.0").half().cuda()
model = model.eval()

dialog = ['帮我查一下这个刚接单的这个货主',
 '是不是第一次下订单',
 '我到装货地，又叫我等半个小时多|我怕是假单',
 '经常有人估计下假单，到了装货地就取消，或者叫等一下',
 '这个货主有下过几次以上订单吗',
 '都是完成订单记录吗',
 '好吧！谢谢|我过来装货地半个小时，到了然后又叫我等半多个小时，我怕被放空|要是我过来等那么久，被货主放空了怎么办',
 '打电话怎么保留证据',
 '\\loc|\\img|发信息都发不了']

history = []

for i in dialog:
    response, history = model.chat(tokenizer, i, history=history)
    print(response)
