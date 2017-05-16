import numpy as np

# TODO: this can be put in the tf graph
class PriceBuffer(object):
    def __init__(self, batch_size=None, buffer_size=None, agents=None, default_val=None, init_price_batch=None):
        if init_price_batch is not None:
            self.agents = init_price_batch[:, 0]
            self.batch_size = init_price_batch.shape[0]
            self.data = init_price_batch[:, 1:].reshape(self.batch_size, 2, -1)
        else:
            # NOTE: 2 means buffer for self and partner
            self.data = np.full((batch_size, 2, buffer_size), default_val, dtype=np.float32)
            self.agents = np.array(agents)  # (batch_size,)
        self.batch_size, _, self.buffer_size = self.data.shape

    def add(self, price, mask, is_self):
        '''
        price: (batch_size,), a list of float prices
        mask: (batch_size,), False for paddings
        is_self: whether price is generated by the decoding agent
        '''
        d = self.data
        k = 0 if is_self else 1
        # Shift left rows to be updated
        d[mask, k, :-1] = d[mask, k, 1:]
        # Append new price
        d[mask, k, -1] = price[mask]

    def to_price_batch(self):
        # batch of one step
        return np.concatenate((self.agents.reshape(self.batch_size, 1, -1), self.data.reshape(self.batch_size, 1, -1)), axis=2)

