from hello.hello import hello
from shared.logger import logger

# Using the 'hello' module
hello()

# Using the 'logger' module
logger.debug("This is a DEBUG log message")
logger.info("This is an INFO log message")
logger.error("This is an ERROR log message")
