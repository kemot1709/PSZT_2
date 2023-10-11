from opt.opt_parser import OptConfig


def get_opt_config():
    return [
        OptConfig("generations", "i", int, 1000, lambda x: 100 <= x <= 10000),
        OptConfig("ph_min", "m", float, 0.1, lambda x: 0 <= x <= 2),
        OptConfig("ph_res", "r", float, 0.75, lambda x: 0.1 <= x <= 0.999),
        OptConfig("demand", "d", int, -1, lambda x: -1 <= x <= 649),
        OptConfig("source", "s", str, ""),
        OptConfig("target", "t", str, ""),
        OptConfig("requirement", "c", int, 64, lambda x: 1 <= x <= 200),
        OptConfig("elimination", "e", int, 0, lambda x: 0 <= x <= 1),
    ]


def validate_value_in_enum(value, enum):
    return value in map(lambda e: e.value, list(enum))
