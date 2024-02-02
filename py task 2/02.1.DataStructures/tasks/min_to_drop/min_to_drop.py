import typing as tp
from collections import Counter


def get_min_to_drop(seq: tp.Sequence[tp.Any]) -> int:
    """
    :param seq: sequence of elements
    :return: number of elements need to drop to leave equal elements
    """
    if len(seq) == 0:
        return 0

    counter = Counter(seq)
    max_count = max(counter.values())
    result = len(seq) - max_count
    return result
