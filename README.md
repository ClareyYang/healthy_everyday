### Github Action 自动报平安

1. fork 本项目到自己的仓库。

2. 在 Settings-Secrets-Actions secrets 下添加两个变量 `ACTION_USERNAME` 和 `ACTION_PASSWORD` 分别为数字北林/校园网的账号和密码。
3. fork后的Workflow默认是禁用的，需要在Actions下点击healthy_everyday，点击右上角的Enable workflow。![image-20210126222607171](https://my-image-hosting.oss-cn-beijing.aliyuncs.com/uPic/image-20210126222607171.png)

4. 每日默认执行时间为每日2点，可以修改 [healthy_everyday.yml](https://github.com/Supremesir/healthy_everyday/blob/action/.github/workflows/healthy_everyday.yml)中的`cron`参数来修改时间（注意crontab为UTC, 比北京时间晚8小时）

> ⚠️ 经测试 GitHub Action Schedule 会有时间不定的延迟，尚不清楚原因，可以将执行时间调整为凌晨，避免延迟带来的影响


本项目基于 [quaeast/healthy_everyday](https://github.com/quaeast/healthy_everyday)

