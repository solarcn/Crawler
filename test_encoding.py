import unittest
from bs4 import BeautifulSoup
from encoding import get_encoding

class Test_testGetEncoding(unittest.TestCase):
    def test_1(self):
        soup = BeautifulSoup('''<html><head>
<title>第7424章_校花的贴身高手_八一中文网</title>
<meta http-equiv="content-type" content="text/html; charset=gbk" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta http-equiv="Cache-Control" content="no-transform" />
<meta http-equiv="mobile-agent" content="format=html5; url=http://m.81xsw.com/book/169/10088024.html" />
<meta http-equiv="mobile-agent" content="format=xhtml; url=http://m.81xsw.com/book/169/10088024.html" />
<meta name="keywords" content="校花的贴身高手,第7424章" />
<meta name="description" content="八一中文网提供了鱼人二代创作的都市言情《校花的贴身高手》干净清爽无错字的文字章节：第7424章在线阅读。" />
<link rel="stylesheet" href="/css/xiaoshuo.css" />
<script type="text/javascript" src="http://libs.baidu.com/jquery/1.4.2/jquery.min.js"></script>
<script type="text/javascript" src="/js/bqg.js"></script>
<script type="text/javascript" src="/js/cookies.js"></script>
<script type="text/javascript"> 
var mobileAgent = new Array("iphone", "ipod", "ipad", "android", "mobile", "blackberry", "webos", "incognito", "webmate", "bada", "nokia", "lg", "ucweb", "skyfire"); 
var browser = navigator.userAgent.toLowerCase(); 
var isMobile = false; 
for (var i=0; i<mobileAgent.length; i++){ if (browser.indexOf(mobileAgent[i])!=-1){ isMobile = true; 
//alert(mobileAgent[i]); 
location.href = 'http://m.81xsw.com/book/169/10088024.html'; 
break; } } 
</script> 
</head></html>''')
        self.assertEqual('gbk', get_encoding(soup))

    def test_2(self):
        soup = BeautifulSoup('''<html><Head>
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta http-equiv="Cache-Control" content="no-transform" />
<meta http-equiv="mobile-agent" content="format=html5; url=http://m.liushuba.com/files/article/html/60/60186/23554540.html" />
<meta http-equiv="mobile-agent" content="format=xhtml; url=http://m.liushuba.com/files/article/html/60/60186/23554540.html" />
<meta http-equiv="Content-Type" content="text/html; charset=gbk" />
<title>修真聊天群最新章节- 第2431章 您好，您的半身已关机-55小说网</title> 
<meta http-equiv="Content-Type" content="text/html; charset=gbk" />
<meta name="keywords" content="修真聊天群最新章节,小说修真聊天群TXT下载,修真聊天群全文阅读,圣骑士的传说作品" /> 
<meta name="description" content="《修真聊天群》的最新章节《 第2431章 您好，您的半身已关机》无弹窗广告" /> 
<meta name="author" content="圣骑士的传说" />
<Link rel="stylesheet" href="/heibing/css/style.css" type="text/css"/>
<script src="/js/tz.js" type="text/javascript"></script>
<script type="text/javascript">uaredirect("http://m.liushuba.com/files/article/html/60/60186/23554540.html");</script>
<script language="javascript" type="text/javascript" src="/heibing/js/xiaoshuo.js"></script>
<script type="text/javascript">var preview_page = "23552272.html",next_page = "23554733.html",index_page = "index.html",article_id = "60186",chapter_id = "23554540";function jumpPage(event){var evt =event?event:window.event;if(evt.keyCode==37) location=preview_page;if (evt.keyCode==39) location=next_page;if (evt.keyCode==13) location=index_page;}document.onkeydown=jumpPage;</script>
</Head></html>''')
        self.assertEqual('gbk', get_encoding(soup))


    #   def tearDown(self):
    #    # 每个测试用例执行之后做操作
    #    print('111')

    #def setUp(self):
    #    # 每个测试用例执行之前做操作
    #    print('22222')

    #@classmethod
    #def tearDownClass(self):
    ## 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
    #     print('4444444')
    #@classmethod
    #def setUpClass(self):
    ## 必须使用@classmethod 装饰器,所有test运行前运行一次
    #    print('33333')

    #def test_a_run(self):
    #    self.assertEqual(1, 1)  # 测试用例
        
    #def test_b_run(self):
    #    self.assertEqual(2, 2)  # 测试用例

     #assertEqual(a, b)     a == b      
     #   assertNotEqual(a, b)     a != b      
     #   assertTrue(x)     bool(x) is True      
     #   assertFalse(x)     bool(x) is False      
     #   assertIsNone(x)     x is None     
     #   assertIsNotNone(x)     x is not None   
     #   assertIn(a, b)     a in b    
     #   assertNotIn(a, b)     a not in b

if __name__ == '__main__':
    unittest.main()
