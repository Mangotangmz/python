import random
from datetime import datetime


def get_order_sn():
    """
    生成随机订单号
    """
    sn = ''
    s = '1234567890qwertyuiopasdfghjklzxcvbnm'
    for i in range(10):
        sn += random.choice(s)
    sn += datetime.now().strftime('%Y%m%d%D%M%S')