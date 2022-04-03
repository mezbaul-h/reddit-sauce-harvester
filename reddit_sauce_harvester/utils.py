from functools import reduce
from typing import Any, Dict


def deep_get(dictionary: Dict[str, Any], keys: str, default: Any = None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)
