import sys


class OptParser:

    def __init__(self, config):
        self._args = {}
        self._abbrev_to_full_name = {}
        for arg_config in config:
            self._args[arg_config._full_name] = (arg_config._arg_type, arg_config._default_value, arg_config._predicate)
            self._abbrev_to_full_name[arg_config._abbrev] = arg_config._full_name

    def parse(self, sys_args):
        parsed = {}
        for sysArg in sys_args:
            if sysArg.startswith("--"):
                # parse long name with value after '='
                if sysArg.find("=") >= 0:
                    name, value = sysArg[2:].split("=")
                    arg_type, _, predicate = self._args[name]
                    value = self._parse_value(value, arg_type, predicate)
                    parsed[name] = value
                # parse long name without value
                else:
                    parsed[sysArg[2:]] = ""
            elif sysArg.startswith("-"):
                # parse short name with value after '='
                if sysArg.find("=") >= 0:
                    abbrev, value = sysArg[1:].split("=")
                    name = self._abbrev_to_full_name[abbrev]
                    arg_type, _, predicate = self._args[name]
                    value = self._parse_value(value, arg_type, predicate)
                    parsed[name] = value
                else:
                    first = sysArg[1]
                    first_name = self._abbrev_to_full_name[first]
                    arg_type, _, predicate = self._args[first_name]
                    # parse short name with value without '='
                    if arg_type is not None:
                        parsed[first_name] = OptParser._parse_value(sysArg[2:], arg_type, predicate)
                    # parse short names without values
                    else:
                        for c in sysArg[1:]:
                            name = self._abbrev_to_full_name[c]
                            parsed[name] = ""
        self._fill_defaults(parsed)
        return parsed

    @staticmethod
    def _parse_value(value, arg_type, predicate):
        if arg_type is None:
            raise ValueError("Value without argument type cannot be parsed")
        elif predicate is None:
            return arg_type(value)
        else:
            if predicate(arg_type(value)):
                return arg_type(value)
            else:
                raise ValueError("Validation predicate failed for value:", value)

    def _fill_defaults(self, parsed):
        for name in self._args:
            _, default_value, _ = self._args[name]
            if name not in parsed and default_value is not None:
                parsed[name] = default_value


class OptConfig:

    def __init__(self, full_name, abbrev, arg_type=None, default_value=None, validate_predicate=None):
        self._full_name = full_name
        self._abbrev = abbrev
        self._arg_type = arg_type
        self._default_value = default_value
        self._predicate = validate_predicate
