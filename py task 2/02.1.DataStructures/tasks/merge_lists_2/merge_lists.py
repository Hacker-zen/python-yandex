import typing as tp
import heapq


def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    result = list[int]()
    heap = [(sequence[0], 0, sequence) for sequence in seq if len(sequence) > 0]
    heapq.heapify(heap)

    while len(heap) > 0:
        first, index, sequence = heapq.heappop(heap)
        result.append(first)
        if len(sequence) > index + 1:
            heapq.heappush(heap, (sequence[index + 1], index + 1, sequence))

    return result
