from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    priority_queue.enqueue({"qtd_linhas": 1})
    priority_queue.enqueue({"qtd_linhas": 10})
    priority_queue.enqueue({"qtd_linhas": 5})

    assert len(priority_queue) == 3
    assert priority_queue.dequeue() == {"qtd_linhas": 1}

    priority_queue.enqueue({"qtd_linhas": 2})
    assert priority_queue.search(0) == {"qtd_linhas": 2}

    with pytest.raises(IndexError):
        priority_queue.search(3)
