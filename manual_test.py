# manual_test.py

from setlogging.logger import get_logger
import sys
import os
import logging
import time

# 将 src 目录添加到 Python 路径中，以便可以导入 setlogging 模块
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "src")))


def test_log_rotation():
    # 设置日志文件路径
    log_file = "test_application.log"

    # 删除旧的日志文件（如果存在）
    if os.path.exists(log_file):
        for i in range(10):  # 删除可能存在的备份文件
            backup_file = f"{log_file}.{i}"
            if os.path.exists(backup_file):
                os.remove(backup_file)
        os.remove(log_file)

    # 配置日志
    logger = get_logger(
        log_level=logging.INFO,  # 设置日志级别
        log_file=log_file,  # 日志文件路径
        max_size_mb=1,  # 日志文件最大大小（1MB）
        backup_count=3,  # 保留的备份文件数量
        console_output=True,  # 启用控制台输出
        json_format=False  # 非 JSON 格式
    )

    # 写入日志，直到触发滚动
    message = "This is a test log message. " * 500  # 每条日志约 2 KB
    for i in range(1000):  # 写入足够多的日志以触发滚动
        logger.info(f"{i}: {message}")
        print(f"Logged message {i}")
        time.sleep(0.01)  # 稍微延迟，方便观察

    print("Logging complete. Check the log files.")


def main():
    print("Manual testing started...")
    # 测试非 JSON 格式日志
    # print("Testing non-JSON logger...")
    # logger = get_logger(
    #     log_level=logging.CRITICAL,  # 设置日志级别
    #     log_file="application.log",  # 日志文件路径
    #     max_size_mb=1,  # 日志文件最大大小（1MB）
    #     backup_count=3,  # 保留的备份文件数量
    #     console_output=True,  # 启用控制台输出
    #     json_format=False  # 非 JSON 格式
    # )
    # logger.debug("This is a DEBUG message")
    # logger.info("This is an INFO message")
    # logger.warning("This is a WARNING message")
    # logger.error("This is an ERROR message")
    # logger.critical("This is a CRITICAL message")

    # 测试 JSON 格式日志
    print("\nTesting JSON logger...")
    json_logger = get_logger(
        log_level=logging.INFO,  # 设置日志级别
        log_file="application_log.json",  # 日志文件路径
        max_size_mb=1,  # 日志文件最大大小（1MB）
        backup_count=3,  # 保留的备份文件数量
        console_output=True,  # 启用控制台输出
        json_format=True,  # JSON 格式
        indent=4  # JSON 缩进
    )
    json_logger.debug("This DEBUG message will not be printed")  # 不会被打印
    json_logger.info("This is an INFO message")
    json_logger.warning("This is a WARNING message")
    json_logger.error("This is an ERROR message")
    json_logger.critical("This is a CRITICAL message")

    # test rotation
    # test_log_rotation()


if __name__ == "__main__":
    main()
