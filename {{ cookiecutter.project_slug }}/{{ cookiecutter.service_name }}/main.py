import sys

from loguru import logger

from .log import DevelopFormatter, JsonSink
from .settings import settings

logger.remove()
if settings.env == "development":
    develop_fmt = DevelopFormatter(settings.component_name)
    logger.add(sys.stdout, format=develop_fmt)
else:
    json_sink = JsonSink(settings.component_name)
    logger.add(json_sink)
