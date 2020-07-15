import allure

from tools.api import request_tool

#用户注册
@allure.feature("用户注册")#一级分类
@allure.story("用户注册登录模块") #二级分类
@allure.title("注册正常流")
with allure.step("第一步，准备请求数据"):
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
