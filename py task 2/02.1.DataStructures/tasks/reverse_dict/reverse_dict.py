import typing as tp
from collections import defaultdict


def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    res: dict[str, list[str]] = defaultdict(list[str])

    # reversing
    for key, value in dct.items():
        res[value].append(key)

    return dict[str, list[str]](res)
