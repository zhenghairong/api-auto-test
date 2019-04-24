import allure

@allure.feature("测试功能 一")
class Test_py:

    @allure.story("测试小组1")
    def test_demo(self):
        a = 2
        b = 2
        assert  a == b

    @allure.story("测试小组2")
    def test_demo1(self):
         a = 1
         b = 1
         assert a == b