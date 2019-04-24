from Common import Request, Assert
import allure

request = Request.Request()
assertions = Assert.Assertions()


@allure.feature("登录功能")
class Test_login:

    @allure.story("登录")
    def test_login(self):
         log_reps = request.post_request(url='http://192.168.1.137:8080/admin/login',
                                            json={"username": "admin", "password": "123456"})
         reps_text = log_reps.text
         print(type(reps_text))
         reps_dict = log_reps.json()
         print(type(reps_dict))
         assertions.assert_code(log_reps.status_code,200)
         assertions.assert_in_text(reps_dict['message'] ,'成功')