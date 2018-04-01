# -*- encoding: utf-8 -*-

import os
import logging
from gs_pipe.pipeline import PipeLine
from redis import Redis
from rq import Queue


LOG = logging.getLogger(__name__)

task_queue = Queue(connection=Redis())


class Task(object):

    def __init__(self, id, status, result=None, created_at=None, description=None):
        self.id = id
        self.status = status
        self.result = result
        self.created_at = created_at
        self.desrciption = description

    @classmethod
    def from_job(cls, job):
        return cls(
            id=job.id,
            status=job.status,
            created_at=job.enqueued_at,
            description=job.description,
            result = job.result
        )

    def as_dict(self):
        return dict(
            id=self.id,
            status=self.status,
            result=self.result,
            created_at=str(self.created_at),
            description=self.desrciption
        )


def create_task(input_argument, pipeline):
    # queue.enque
    job = task_queue.enqueue(evaluate_pipeline, input_argument, pipeline)

    return Task.from_job(job).as_dict()


def get_task(task_id):
    job = task_queue.fetch_job(task_id)
    return Task.from_job(job).as_dict()


def list_mod():
    mods_dir = os.path.join(os.path.dirname(__file__), "mods")
    # todo ....
    # iterate mods directory, find all funcs ..
    # def find_funcs(fpath):
    #     with open(fpath, "r") as f :
    #         lines = f.read()
    # for dirpath, _ , files in os.walk(mods_dir):
    #     fpaths = [os.path.join(dirpath,f) for f in files]
    # todo

    return [
        'gs_pipe.mods.example.square',
        'gs_pipe.mods.example.minus_one'
    ]


def evaluate_pipeline(input_argument, funcs):
    '''
        input_argument: 10
        funcs: [
            'mods.example.square',
            'mods.example.minus_one'
        ]
        result: minus_one(square(10)) -> 99

    '''
    import importlib

    def find_func(func_str):
        func_name = func_str.split('.')[-1]
        mod_str = '.'.join(func_str.split('.')[:-1])
        # import pdb 
        # pdb.set_trace()
        mod = importlib.import_module(mod_str)
        func = getattr(mod, func_name, None)
        if not callable(func):
            return None
        return func

    # invalid mod check
    # find mod func, remove none func
    # create pipeline
    # evaluate

    funcs = [find_func(func_str) for func_str in funcs]
    pipeline = PipeLine(*funcs)
    result = pipeline.evaluate(input_argument)
    return list(result)


# if __name__ == '__main__':
#     print(evaluate_pipeline(
#         10, ['mods.example.square', 'mods.example.minus_one']))

#     print(evaluate_pipeline(
#         [10, 11, 12, 13, 18, 100, 1112], [
#             'mods.example.square', 'mods.example.minus_one']
#     ))
