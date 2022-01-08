# 🚄 py12306 购票助手
该项目意在给普通的用户提供更简单的使用Py12306的方式，实现更简单的操作，不需要配置相应的开发和运行环境，实现拆包就可用，原有的项目是非常优秀的项目，我们尽在原有的项目上做了一些较小的改动，来实现用户更简单的操作

## 使用方式

这种方式适合于**不懂代码的用户**，直接解压运行，在右侧的`release`中下载对应的包版本，将文件解压出来，运行`run.bat`文件，会自动打开浏览器，如果没有自动打开可以再浏览器输入`http://localhost:8008`，打开后会进入登录界面，用户名：`admin`，密码：`password`，使用12306手机客户端扫描弹出的二维码然后确认登录，输入对应的信息，开始进行抢票

目前只支持Windows客户端，Windows客户端如果使用出现问题尝试使用`管理员权限`运行文件

## 更新
- 21-12-11
    - 释放Windows的包

## 截图
### Web 管理页面
![Web 管理页面图片](./data/images/web.png)

## Features

- [x] 支持Windows安装包
- [ ] 支持Mac Apple Silicon的安装包
- [ ] 支持Mac Intel的安装包
- [ ] 支持web管理界面配置配置文件

## Thanks

- 感谢大佬的https://github.com/pjialin/py12306，该包仅对大佬的这个包进行简单的修改和打包

## License

[Apache License.](https://github.com/Heliner/py12306/blob/master/LICENSE)

