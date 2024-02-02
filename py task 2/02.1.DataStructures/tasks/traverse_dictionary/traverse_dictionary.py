import typing as tp


def traverse_dictionary_immutable(
        dct: tp.Mapping[str, tp.Any],
        prefix: str = "") -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param prefix: prefix for key used for passing total path through recursion
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    result = list[tuple[str, int]]()
    traverse_dictionary_mutable(dct, result)
    return result


def traverse_dictionary_mutable(
        dct: tp.Mapping[str, tp.Any],
        result: list[tuple[str, int]],
        prefix: str = "") -> None:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param result: list with pairs: (full key from root to leaf joined by ".", value)
    :param prefix: prefix for key used for passing total path through recursion
    :return: None
    """
    for key, value in dct.items():
        object_key = f"{prefix}.{key}" if prefix != "" else key
        if isinstance(value, dict):
            traverse_dictionary_mutable(value, result, object_key)
        else:
            result.append((object_key, value))


def traverse_dictionary_iterative(
        dct: tp.Mapping[str, tp.Any]
        ) -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    result = list[tuple[str, int]]()
    stack: list[tuple[str, tp.Any]] = [(key, value) for key, value in dct.items()]

    while len(stack) > 0:
        key, value = stack.pop()

        if isinstance(value, int):
            result.append((key, value))
            continue

        for subkey, subvalue in value.items():
            stack.append((f"{key}.{subkey}", subvalue))

    return result
