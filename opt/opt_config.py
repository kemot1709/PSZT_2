from opt.opt_parser import OptConfig


def get_opt_config():
    return [
        OptConfig("sel_type", "S", str, "roulette", lambda s: validate_value_in_enum(s, SelectionType)),
        OptConfig("rep_type", "r", str, "generation+", lambda s: validate_value_in_enum(s, ReplacementType)),
        OptConfig("iterations", "i", int, 100, lambda x: 10 <= x <= 5000),
        OptConfig("function", "f", str, "cigar", lambda s: validate_value_in_enum(s, FunctionType)),
        OptConfig("dimensions", "d", int, 2, lambda x: 2 <= x <= 10),
        OptConfig("crossover_p", "C", float, 0.5, lambda x: 0.01 <= x <= 1.0),
        OptConfig("cardinality", "n", int, 200, lambda x: 50 <= x <= 1000 and x % 2 == 0),
        OptConfig("attempts", "a", int, 1, lambda x: 1 <= x <= 50),
        OptConfig("mut_sigma", "s", float, 5, lambda x: 0 <= x <= 100),
        OptConfig("x_min", "m", float, -100, lambda x: -100 <= x <= 0),
        OptConfig("x_max", "M", float, 100, lambda x: 0 <= x <= 100)
    ]


def validate_value_in_enum(value, enum):
    return value in map(lambda e: e.value, list(enum))
