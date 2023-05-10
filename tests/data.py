from sag_py_cache_decorator.lru_cache import lru_cache

counter: int = 0


def reset_counter() -> None:
    global counter
    counter = 0


@lru_cache(maxsize=3)
def sync_func(str: str, str2: str) -> str:
    global counter
    counter = counter + 1
    return f"{str}-{str2}-{counter}"


@lru_cache(maxsize=3)
def sync_func_use_cache(
    str: str,
    str2: str,
    lru_use_cache: bool = True,
) -> str:
    global counter
    counter = counter + 1
    return f"{str}-{str2}-{counter}"


@lru_cache(maxsize=3)
def sync_func_clear_cache(
    str: str,
    str2: str,
    lru_clear_cache: bool = False,
) -> str:
    global counter
    counter = counter + 1
    return f"{str}-{str2}-{counter}"


@lru_cache(maxsize=3)
def sync_func_clear_arg_cache(
    str: str,
    str2: str,
    lru_clear_arg_cache: bool = False,
) -> str:
    global counter
    counter = counter + 1
    return f"{str}-{str2}-{counter}"


@lru_cache(maxsize=3)
async def async_func(str: str, str2: str) -> str:
    global counter
    counter = counter + 1
    return f"{str}-{str2}-{counter}"


@lru_cache(maxsize=3)
async def async_func_use_cache(
    str: str,
    str2: str,
    lru_use_cache: bool = True,
) -> str:
    global counter
    counter = counter + 1
    return f"{str}-{str2}-{counter}"


@lru_cache(maxsize=3)
async def async_func_clear_cache(
    str: str,
    str2: str,
    lru_clear_cache: bool = False,
) -> str:
    global counter
    counter = counter + 1
    return f"{str}-{str2}-{counter}"


@lru_cache(maxsize=3)
async def async_func_clear_arg_cache(
    str: str,
    str2: str,
    lru_clear_arg_cache: bool = False,
) -> str:
    global counter
    counter = counter + 1
    return f"{str}-{str2}-{counter}"
