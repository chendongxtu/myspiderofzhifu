import urllib2
content = urllib2.urlopen('http://www.baidu.com').read()
print(content)

#使用代理服务器，这在某些情况下比较有用，比如IP被封了，或者比如IP访问的次数受到限制等等
#proxy_support = urllib2.ProxyHandler({'http':'http://XX.XX.XX.XX:XXXX'})
#opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
#urllib2.install_opener(opener)
#content = urllib2.urlopen('http://XXXX').read()
