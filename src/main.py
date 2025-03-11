from config import load_config
from selenium import webdriver
from sign import do_login, do_reply, do_sign, do_sleep
from apscheduler.schedulers.blocking import BlockingScheduler
from croniter import croniter
from datetime import datetime

def main():
    # start_sign()
    print("启动程序")
    scheduler = BlockingScheduler()

    config = load_config()
    cron= config.get("cron")
    print("cron表达式：", cron)
    next_run_time = croniter(config.get("cron"), datetime.now()).get_next(datetime)
    print(f"下一次执行时间: {next_run_time}")

    try:
        cron_fields = parse_cron_expression(cron)
        scheduler.add_job(start_sign, 'cron',**cron_fields)
        scheduler.start()
        print("添加定时任务成功")
    except:
        scheduler.shutdown()
        print("添加定时任务失败")

def parse_cron_expression(cron_expression):
    fields = cron_expression.split()
    if len(fields) != 5:
        raise ValueError("Invalid cron expression")
    
    minute, hour, day_of_month, month, day_of_week = fields
    
    return {
        'minute': minute,
        'hour': hour,
        'day': day_of_month,
        'month': month,
        'day_of_week': day_of_week
    }

def start_sign():
    print("start_sign")
    config = load_config()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome=f'{config.get("chrome")}/wd/hub'
    browser = webdriver.Remote(command_executor=chrome,options=chrome_options)

    # browser = webdriver.Edge()
    browser.implicitly_wait(30)

    try:
        print("开始登录")
        do_login(browser,config)
        print("登录完毕")
        do_sleep(5)

        print("开始回复")
        do_reply(browser,config)
        print("回复完毕")
        do_sleep(5)

        print("开始签到")
        do_sign(browser,config)
        print("签到完毕")
        do_sleep(5)

        print("end_sign，关闭浏览器")
    except:
        print("sign 异常 等待重试")

    browser.quit()
    # 计算下一次执行时间
    next_run_time = croniter(config.get("cron"), datetime.now()).get_next(datetime)
    print(f"下一次执行时间: {next_run_time}")


if __name__ == "__main__":
    main()