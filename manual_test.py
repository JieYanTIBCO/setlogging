# manual_test.py
from setlogging.logger import get_logger
from tests.test_logger import LogCapture
import sys
import os
import logging
import time
from pathlib import Path
import json

# 将 src 目录添加到 Python 路径中，以便可以导入 setlogging 模块
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "src")))


def test_log_rotation():
    # 设置日志文件路径
    log_file = "test_application_log.json"

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
        max_size_mb=3,  # 日志文件最大大小（1MB）
        backup_count=2,  # 保留的备份文件数量
        console_output=True,  # 启用控制台输出
        json_format=True,  # 是否 JSON 格式
        indent=4  # JSON 缩进
    )

    # 写入日志，直到触发滚动
    message = "This is a test log message. " * 500  # 每条日志约 2 KB
    for i in range(1000):  # 写入足够多的日志以触发滚动
        logger.info(f"{i}: {message}")
        # print(f"Logged message {i}")
        # time.sleep(0.01)  # 稍微延迟，方便观察

    print("Logging complete. Check the log files.")


def test_file_rotation(tmp_path):
    """Test log file rotation"""
    log_file = tmp_path / "rotate.log"
    max_size_mb = 1  # 1MB
    backup_count = 3
    logger = get_logger(
        log_file=str(log_file),
        max_size_mb=max_size_mb,
        backup_count=backup_count
    )

    # Write enough data to trigger rotation
    for i in range(104):
        logger.info("x" * 1024 * 10)  # 10KB per log entry


def test_json_indent(tmp_path):
    """Test JSON indentation formatting"""
    log_file = tmp_path / "test_indent.json"
    indent = 4
    logger = get_logger(
        json_format=True,
        indent=indent,
        log_file=str(log_file)
    )

    # Generate some log entries
    test_message = "Test indent"
    logger.info(test_message)
    logger.info("Another message")

    # Validate the indentation of the log file
    with open(log_file) as f:
        for line in f:
            # Skip empty lines or lines that are not JSON objects
            if line.strip().startswith("{") or line.strip().startswith("}"):
                continue

            # Count the number of leading spaces
            print(line)
            print(f"line.lstrip(): {line.lstrip()}")  # Add this line
            print(f"len of line.lstrip(): {len(line.lstrip())}")
            leading_spaces = len(line) - len(line.lstrip())
            print(f"leading_spaces: {leading_spaces}")


def manual_test_json_structure(log_file_path):
    """Manually test JSON log entry structure and print results for verification."""
    required_fields = ["time", "level", "message", "name"]

    print(f"Manual testing of log file: {log_file_path}")
    with open(log_file_path, "r") as f:
        for line_number, line in enumerate(f, start=1):
            print(f"\nProcessing line {line_number}: {line.strip()}")

            try:
                # Parse the line as JSON
                log_entry = json.loads(line.strip())
                print(f"Parsed JSON: {json.dumps(log_entry, indent=4)}")

                # Check required fields
                missing_fields = [
                    field for field in required_fields if field not in log_entry]
                if missing_fields:
                    print(f"❌ Missing fields in line {
                          line_number}: {missing_fields}")
                else:
                    print(f"✅ All required fields are present in line {
                          line_number}")

                # Check custom_field
                if "custom_field" in log_entry:
                    print(f"✅ Custom field 'custom_field' found: {
                          log_entry['custom_field']}")
                else:
                    print(f"❌ Custom field 'custom_field' is missing in line {
                          line_number}")

            except json.JSONDecodeError as e:
                print(f"❌ Failed to parse line {line_number} as JSON: {e}")

    print("\nManual test complete.")


def test_json():
    # 测试 JSON 格式日志
    print("\nTesting JSON logger...")
    json_logger = get_logger(
        log_level=logging.DEBUG,  # 设置日志级别
        log_file="application_jason.log",  # 日志文件路径
        max_size_mb=1,  # 日志文件最大大小（1MB）
        backup_count=3,  # 保留的备份文件数量
        console_output=True,  # 启用控制台输出
        json_format=True,  # JSON 格式
        indent=2  # JSON 缩进
    )
    json_logger.debug("This DEBUG message will not be printed")  # 不会被打印
    json_logger.info("This is an INFO message")
    json_logger.warning("This is a WARNING message")
    json_logger.error("This is an ERROR message")
    json_logger.critical("This is a CRITICAL message")

    json_logger.info("Test extra customer field message!!!",
                     extra={"custom_field": "value"})


def manual_test_custom_log_format():
    """Test custom log format"""
    custom_format = "%(levelname)s - %(message)s"
    logger = get_logger(log_format=custom_format)
    print(f"Logger format: {custom_format}")
    with LogCapture() as capture:
        logger.info("Test message")
        print(str(capture.records[0]))


def main():
    # print("Manual testing started...")
    # # 测试非 JSON 格式日志
    # print("Testing non-JSON logger...")
    # logger = get_logger(
    #     log_level=logging.CRITICAL,  # 设置日志级别
    #     log_file="application.log",  # 日志文件路径
    #     max_size_mb=-1,  # 日志文件最大大小（1MB）
    #     backup_count=3,  # 保留的备份文件数量
    #     console_output=True,  # 启用控制台输出
    #     json_format=False  # 非 JSON 格式
    # )
    # logger.debug("This is a DEBUG message")
    # logger.info("This is an INFO message")
    # logger.warning("This is a WARNING message")
    # logger.error("This is an ERROR message")
    # logger.critical("This is a CRITICAL message")

    # test rotation
    # print("\nTesting Rotation ...")
    # test_log_rotation()

    # test file rotation
    # temp_path = Path("/tmp/")
    # # test_file_rotation(temp_path)

    # test_json_indent(temp_path)

    # logfilepath = "/Users/jieyan/Projects/setlogging/application_jason.log"
    # manual_test_json_structure(logfilepath)
    manual_test_custom_log_format()


if __name__ == "__main__":
    main()
