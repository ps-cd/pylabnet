import rpyc


class ServiceBase(rpyc.Service):
    # FIXME: do not require the module to have log client

    _module = None
    log = None

    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        self.log.info('Client connected')

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        self.log.info('Client disconnected')

    def assign_module(self, module):
        self._module = module
        self.log = module.log