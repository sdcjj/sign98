# 签到适配



## config.json说明
```
{
    "98domin":"域名",
    "account":{
        "uid":"账号",
        "pwd":"密码",
        "qid":"问题id",
        "answer":"问题答案"
    },
    // 会随机取一条回帖内容
    "replyList":["回帖内容1","回帖内容2"],
    // 定时执行 建议改掉
    "cron":"55 20 */1 * *",
    "chrome":"chrome docker 的地址http://192.168.x.x:4444"
}
```

## 本地构建
```
docker build -t sign98-demo:0.0.1 .

```

## 新建conf文件夹 config.json复制进去 并配置好账号信息
## 依赖chrome容器
## compose
```

sign98:
    container_name: sign98
    image: sign98-demo:0.0.1
    environment:
      - TZ=Asia/Shanghai
    volumes:
      - /conf:/src/conf
    restart: unless-stopped

chrome:
    container_name: chrome
    image: selenium/standalone-chrome
    ports:
      - "4444:4444"

```




