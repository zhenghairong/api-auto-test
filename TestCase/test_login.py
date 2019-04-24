from Common import Request, Assert, read_excel
import allure
import  pytest

request = Request.Request()
assertions = Assert.Assertions()
idslist = []
excel_list = read_excel.read_excel_list('./document/test.xlsx')
url = 'http://192.168.1.137:8080/'
head = {}

@allure.feature("登录功能")
class Test_login:

     @allure.story("登录")
     def test_login(self):

         log_reps = request.post_request(url=url+'admin/login',
                                            json={"username": "admin", "password": "123456"})
         reps_text = log_reps.text
         print(type(reps_text))
         reps_dict = log_reps.json()
         print(type(reps_dict))
         assertions.assert_code(log_reps.status_code,200)
         assertions.assert_in_text(reps_dict['message'] ,'成功')

         data_dict = reps_dict['data']
         token = data_dict['token']
         tokenHead = data_dict['tokenHead']
         global head
         head = {'Authorization': tokenHead+token}
     @allure.story("获取用户信息")
     def test_info(self):
         info_resp = request.get_request(url=url + 'admin/info', headers= head)
         resp_dict = info_resp.json()
         assertions.assert_code(info_resp.status_code,200)
         assertions.assert_in_text(resp_dict['message'] ,'成功')

     @allure.story("测试登录")
     @pytest.mark.parametrize("username,password,msg",[['admin', '123456', '成功'], ['admin1', '123456', '错误'], ['admin', '123456a', '错误'],
                                                         ['admin', '123456', '成功'], ['admin1', '123456', '错误'], ['admin', '123456a', '错误']],
                                                        ids=['登录成功', '用户名错误', '密码错误', '登录成功1', '用户名错误1', '密码错误1']
                                                        )
     def test_login1(self,username,password,msg):
        login_resp = request.post_request(url=url + 'admin/login',
                              json={'username':username,'password':password})
        resp_text = login_resp.text
        print(type(resp_text))

        resp_dict  = login_resp.json()
        print(type(resp_dict))
        assertions.assert_code(login_resp.status_code,200)
        assertions.assert_in_text(resp_dict['message'],msg)

     @allure.story("测试登录1")
     @pytest.mark.parametrize ('username,password,msg',excel_list,ids=idslist)
     def test_login2(self,username,password,msg):
        test_login2 = request.post_request(url=url + 'admin/login',
                                           json={'username':username,'password':password})
