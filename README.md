# 多个域名的跳转服务

目标：当用户在浏览器里输入符合正则表达式
`https?://(www\.)?(newfairs|niuzhanwang)\.(com|cn|net)(/some/path)?`的域名时，
能自动跳转到统一的目标地址`https://wwww.newfairs.com/some/path`.

## Redirect实现

portal_py2.py是Python 2.7版本的redirect服务，
portal.py是Python 3.x版本的redirect服务。

手工在remote host上启动服务：

```
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt
python dserver.py
```

或者使用fabric在remote host上部署redirect服务：
`fab -H <host1>,<host2> deploy`

查看日志：`tail -f server.log`

停止服务：`pkill python`（请先使用`pgrep python`确认进程号正确）

## 域名解析

redirect服务将任何 HTTP 请求通过301 redirect 到目标地址。
定义哪些URL应该被转发，则是负载均衡器（或者nginx/apache）的职责。

# Discussions

## redirect cache问题

使用Firefox调试时，由于Firefox默认缓存了redirect目标，导致代码更新时，
浏览器中看不到效果，关闭Firefox对redirect缓存的方法请参考
[Firefox 5 'caching' 301 redirects](http://stackoverflow.com/questions/6980192/firefox-5-caching-301-redirects)

## fabric 与 Python 3.x 不兼容问题

fabric 没有Python 3.x 版本导致如果在fabfile.py中`import portal`，
会运行portal.py中的`from http.server import ...`从而报包未找到错误。
解决方法是把服务监听端口写死在fabfile里，手工保证其与portal.py中的PORT一致。

## with cd 中 put 参数的特殊要求

当在`with cd...`内使用`put`时，第二个参数（目标目录）不能省略，
否则`cd`所指定的目录将失效，这是fabric的一个bug:
https://github.com/fabric/fabric/issues/1373

## daemon启动失败

启动daemon后要等待一段时间再退出shell，否则会导致daemon启动失败，原因不清楚。
对应到代码，就是`run('. venv/bin/activate && python dserver.py && sleep 5')`中
` && sleep 5`是必须的，当然值不一定是5。

## 其他参考资源

* http://stackoverflow.com/questions/2506932/how-do-i-forward-a-request-to-a-different-url-in-python

* https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler

* http://xlsxwriter.readthedocs.io/example_http_server3.html

* http://stackoverflow.com/questions/11146128/python-daemon-and-stdout

* https://pypi.python.org/pypi/python-daemon/
