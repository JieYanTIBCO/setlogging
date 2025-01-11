# manual_test.py

from setlogging.logger import get_logger
import sys
import os
import logging

# 将 src 目录添加到 Python 路径中，以便可以导入 setlogging 模块
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "src")))


def main():
    # 测试非 JSON 格式日志
    print("Testing non-JSON logger...")
    logger = get_logger(
        log_level=logging.NOTSET,  # 设置日志级别
        log_file="application.log",  # 日志文件路径
        max_size_mb=1,  # 日志文件最大大小（1MB）
        backup_count=3,  # 保留的备份文件数量
        console_output=True,  # 启用控制台输出
        json_format=False  # 非 JSON 格式
    )
    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")
    logger.critical("This is a CRITICAL message")

    # # 测试 JSON 格式日志
    # print("\nTesting JSON logger...")
    # json_logger = get_logger(
    #     log_level=logging.INFO,  # 设置日志级别
    #     log_file="application_log.json",  # 日志文件路径
    #     max_size_mb=1,  # 日志文件最大大小（1MB）
    #     backup_count=3,  # 保留的备份文件数量
    #     console_output=True,  # 启用控制台输出
    #     json_format=True,  # JSON 格式
    #     indent=2  # JSON 缩进
    # )
    # json_logger.debug("This DEBUG message will not be printed")  # 不会被打印
    # json_logger.info("This is an INFO message")
    # json_logger.warning("This is a WARNING message")
    # json_logger.error("This is an ERROR message")
    # json_logger.critical("This is a CRITICAL message")


if __name__ == "__main__":
    main()
