
ok = 200
SUCCESS = {'code': 200, 'msg': '请求成功'}

USER_REGISTER_EXIST = {'code': 1001, 'msg': '用户已存在'}
USER_REGISTER_PHONE = {'code': 1002, 'msg': '输入电话号码不正确'}
USER_REGISTER_PWD = {'code': 1003, 'msg': '密码少于6位'}
USER_REGISTER_CODE = {'code': 1004, 'msg': '验证码不正确'}

USER_LOGIN_EXIST = {'code': 1005, 'msg': '用户不存在'}
USER_LOGIN_PWD = {'code': 1006, 'msg': '密码错误'}

USER_AUTH_INFO = {'code': 1007, 'msg': '身份证号码格式不正确'}
USER_AUTH_ID_EXIST = {'code': 1008, 'msg': '该身份证已经验证过了'}

HOME_NO_ID_CARD = {'code': 1009, 'msg': '未实名认证'}