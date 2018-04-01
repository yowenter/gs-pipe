# -*-encoding : utf-8 -*-

import logging

LOG = logging.getLogger(__name__)


class PipeLine(object):

    def __init__(self, *functions):
        self.functions = functions

    def evaluate(self, data):
        """Evaluate pipeline

        Arguments:
            data {iterator data or object} -- input data 

        Returns:
            iterator data 
        """

        if hasattr(data, "__iter__"):
            return self.evaluate_iter_element(data)
        else:
            # return iterator result
            return [self.evaluate_single_element(data)]

    def evaluate_single_element(self, element):
        data = element
        result = None
        for func in self.functions:
            result = func(data)
            data = result
        return result

    def __repr__(self):
        return "Pipe: {} ".format("-+>".join([str(f.__name__) for f in self.functions]))

    def evaluate_iter_element(self, data):
        result = None
        for element in data:
            try:
                for func in self.functions:
                    result = func(element)
                    element = result

            except Exception as e:
                LOG.warn("Evaluate pipeline error, %s %s %s ",
                         self, element, str(e))
                result = None

            yield result