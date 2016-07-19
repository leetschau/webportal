# 多个域名的跳转服务

目标：当用户在浏览器里输入符合正则表达式
`https?://(www\.)?(newfairs|niuzhanwang)\.(com|cn|net)(/some/path)?`的域名时，
能自动跳转到统一的目标地址`https://wwww.newfairs.com/some/path`.

## Redirect实现

使用`python portal_py2.py`启动Python 2.7版本的redirect服务，
使用`python3 portal.py`启动Python 3.x版本的redirect服务。

## 域名解析

redirect服务将任何 HTTP 请求通过301 redirect 到目标地址。
定义哪些URL应该被转发，则是负载均衡器（或者nginx/apache）的职责。
