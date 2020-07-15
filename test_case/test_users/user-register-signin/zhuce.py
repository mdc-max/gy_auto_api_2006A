from tools.api import request_tool

#用户注册
def test_signup(pub_data):
    pub_data["username"] = "自动生成 字符串 3 数字 mdc"
    pub_data["phone"] = "自动生成 手机号"
    pub_data["pwd"] = "自动生成 字符串 5 数字 dc"
    pub_data["npwd"] = "自动生成 字符串 5 数字 ddc"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': 'ip=222.67.190.141; addr=%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%97%B5%E8%A1%8C%E5%8C%BA; Stu-Token=fa543eb1e3ab4e258d409686b5158f80; StuID=462'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "phone": "${phone}",
  "pwd": "${pwd}",
  "rePwd": "${pwd}",
  "userName": "${username}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
    '''
    自动生成 数字 20,80   #生成20到80之间的数字 例：56
    自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
    自动生成 地址
    自动生成 姓名
    自动生成 手机号
    自动生成 邮箱
    自动生成 身份证号
    '''
#用户登录
def test_login(pub_data):
    json_path = [{"cstId": '$.data.cstId'}]
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {'Host': '192.168.1.151:8084',"token":"pub_data[token]", 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': 'ip=222.67.190.141; addr=%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%97%B5%E8%A1%8C%E5%8C%BA; Stu-Token=fa543eb1e3ab4e258d409686b5158f80; StuID=462'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "pwd": "${pwd}",
  "userName": "${username}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data,json_path = json_path)

#修改密码
def test_changepwd(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/changepwd"  # 接口地址
    headers = {"token":pub_data['token'],'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': 'ip=222.67.190.141,"token":"pub_data["token"]"; addr=%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%97%B5%E8%A1%8C%E5%8C%BA; Stu-Token=fa543eb1e3ab4e258d409686b5158f80; StuID=462'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "newPwd": "${npwd}",
  "oldPwd": "${pwd}",
  "reNewPwd": "${npwd}",
  "userName": "${username}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
