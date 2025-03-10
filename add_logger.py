from loguru import logger as loguru_logger


def customize_loguru_logger():
    # UNIT_DEBUG
    loguru_logger.level("UNIT_DEBUG", no=16, color="<green>",
                        icon="🧪")  # 单元测试的调试信息
    loguru_logger.add("logs/unit_debug.log",
                      filter=lambda record: record[
                                                "level"].name == "UNIT_DEBUG",
                      level="UNIT_DEBUG")
    loguru_logger.log("UNIT_DEBUG", "This is a unit test debug message.")
    # MODEL DEBUG
    loguru_logger.level("MODEL_DEBUG", no=15, color="<blue>",
                        icon="🤖")  # 测试模型的调试信息
    loguru_logger.add("logs/model_debug.log",
                      filter=lambda record: record[
                                                "level"].name == "MODEL_DEBUG",
                      level="MODEL_DEBUG")
    loguru_logger.log("MODEL_DEBUG", "This is a model debug message.")


# 定义一个装饰器
def setup_logger_decorator(func):
    @wraps(func)  # 用于保留原函数的名称和文档字符串
    def wrapper(*args, **kwargs):
        customize_loguru_logger()  # 在被装饰函数执行前调用 customize_loguru_logger
        return func(*args, **kwargs)  # 执行原函数

    return wrapper
