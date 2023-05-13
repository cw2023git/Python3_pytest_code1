import pytest

# @pytest.fixture(scope='',params='',autouse=,ids='',name='')
# @pytest.fixture(scope='function') #表示的是@pytest.fixture标记的方法的作用域，可写可不写
# @pytest.fixture(scope='function',autouse=True) #autouse=True,自动让每一条用例，使用此前后置函数
# @pytest.fixture(scope='class',autouse=True) #scope='class'，表示作用在‘类’级别，每个类前后执行
# @pytest.fixture(scope='module',autouse=True) #scope='module'，表示作用在‘模块’级别，在模块前后执行
def my_fix1():
    print('这是前置的方法，可以实现部分以及全部用例的前后置')

    yield
    print('这是后置的方法')

@pytest.fixture(scope='function',params=['成龙','甄子丹','菜10']) #params=['成龙','甄子丹','菜10']，参数化
def my_fix2(request): #通过传入的‘request’，会把['成龙','甄子丹','菜10']传到此前置函数
    # print('前置')
    # return request.param #返回每个的值，再传到每个用例中【注意：固定写法】
    # return 'aaa' #直接返回此字符串，再传到每个用例中

    print('前置')
    yield request.param #使用此方法，可实现前置、后置【采纳】
    print('后置') #代码

    #return 和 yield都表示返回的意思，return后面不能有代码，yield后面可以有代码

# @pytest.fixture(scope='function',params=['成龙','甄子丹','菜10'],ids=['cl','zzd','c10'])#当使用params参数化时，给每一个值设置一个变量名
# @pytest.fixture(scope='function',params=['成龙','甄子丹','菜10'],ids=['cl','zzd','c10'],name='aaa')#表示的是被@pytest.fixture标记的方法取一个别名
@pytest.fixture(scope='function',params=['成龙','甄子丹','菜10'])#表示的是被@pytest.fixture标记的方法取一个别名
def my_fix3(request):
    print('前置方法')
    yield request.param  #显示如下：test_day1.py::Test1::test_1[cl] 前置方法
    print('后置方法')

class Test1:
    age=18

    #在每个用例之前执行一次
    # def setup(self):
    #     print('在执行测试用例之前执行的代码：打开浏览器，加载网页')

    #在所有用例之前只执行一次
    # def setup_class(self):
    #     print('在每个类执行前初始化的工作，比如：创建日志对象、创建数据库的连接、创建接口的请求对象')

    def test_1(self,my_all,my_user): #此方法中直接使用此‘前置’函数 注意：无需每个测试用例都加上‘my_fix’，可使用autouse=True
    # def test_1(self,aaa): #直接使用‘别名’aaa即可【了解即可，意义不大】
        print('这是个用户管理')

        # print('------------'+str(my_user)+'--------------') #把前置函数打印出来
        # print('------------'+str(aaa)+'--------------') #直接使用‘别名’aaa即可【了解即可，意义不大】
        print('这是个全局前置',my_all)
        print('这是个全局前置',my_user)

        assert 1==2

    # @pytest.mark.smoke
    def test_2(self):
        print('这是此模块中的冒烟用例')

    # @pytest.mark.skip   #跳过，无条件跳过
    def test_3(self):
        print('这是此个要跳过的测试用例')

    # @pytest.mark.skipif(age>=18,'已成年') #跳过，有条件跳过
    def test_4(self):
        print('这是此模块中的冒烟用例')
        # raise Exception('自定义异常')

    # 在每个用例之后执行一次
    # def teardown(self):
    #     print('在执行测试用例之后的扫尾代码：关闭浏览器')

    # 在所有用例之后只执行一次
    # def teardown_class(self):
    #     print('在每个类执行后的扫尾工作，比如：销毁日志对象、销毁数据库的连接、销毁接口的请求对象')


if __name__ == '__main__':
    pytest.main()




























