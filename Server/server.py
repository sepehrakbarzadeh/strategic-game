from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from uuid import uuid4
import json

class MyProtocol(Protocol):
    states = ("hello", "wait", "ready","run")
    msg_type = ("hello", "change_state")

    def __init__(self, factory):
        self.factory = factory
        self.state = self.states[0]
        self.remote_nodeid = str(uuid4())

    def get_peers(self):
        return self.transport.getPeer()

    def connectionMade(self):
        self.factory.register(self)
        print("Connection from {}".format(self.get_peers()))
        print("Number of connections: {}".format(self.factory.num_connections))
        self.dispatch()

    def connectionLost(self, reason):
        self.factory.unregister(self)
        print("{} disconnected".format(self.get_peers()))
        print("Number of connections: {}".format(self.factory.num_connections))

    def send_hello(self):
        hello_wait = json.dumps({'MSG': self.msg_type[0], 'ID': self.remote_nodeid})
        self.transport.write(hello_wait.encode('utf-8') + "\n".encode('utf-8'))
    
    def send_change_state(self, msg_type, state):
        state_change = json.dumps({'MSG': msg_type, 'STATE': state})
        self.transport.write(state_change.encode('utf-8') + "\n".encode('utf-8'))

    def change_state_to_wait(self):
        self.send_hello()
        self.state = self.states[1]
        self.send_change_state(self.msg_type[1], self.state)
    
    def change_state_to_ready(self):
        self.state = self.states[2]
        self.send_change_state(self.msg_type[1], self.state)
    
    def change_state_to_run(self):
        self.state = self.states[3]
        self.send_change_state(self.msg_type[1], self.state)

    def chenge_state(self, state):
        if state in self.states:
            if self.state == self.states[0] and state == self.states[1]:
                self.change_state_to_wait()
            elif self.state == self.states[0] and state == self.states[2]:
                self.send_hello()
                self.change_state_to_ready()
            elif self.state == self.states[1] and state == self.states[2]:
                self.change_state_to_ready()
            elif self.state == self.states[2] and state == self.states[3]:
                self.change_state_to_run()

    def initial_game_space(self):
        #FIXME
        pass

    def dispatch(self):
        if self.factory.num_connections <= 1:
            self.chenge_state(self.states[1])
        else:
            for peer_class in self.factory.peers.values():
                peer_class.chenge_state(self.states[2])
            self.initial_game_space()
            for second_peer_class in self.factory.peers.values():
                second_peer_class.chenge_state("run")

    def dataReceived(self, data):
        for line in data.splitlines():
            line = line.strip()
            try:
                json.loads(line)
                #FIXME
            except:
                #FIXME
                pass

class MyFactory(Factory):
    def __init__(self):
        # number of connection
        self._num_connections = 0
        # uuid of peers in connection
        self._peers = {}
    
    # property of connections
    @property
    def num_connections(self):
        return self._num_connections
    
    # property of peers
    @property
    def peers(self):
        return self._peers
    
    # register one connection
    def register(self, agent):
        self._num_connections += 1
        if agent.remote_nodeid not in self._peers:
            self._peers[agent.remote_nodeid] = agent
    
    # unregister one connection
    def unregister(self, agent):
        self._num_connections -= 1
        if agent.remote_nodeid in self._peers:
            self._peers.pop(agent.remote_nodeid)
    
    def startFactory(self):
        # uuid for factory class
        self.nodeid = str(uuid4())

    def buildProtocol(self, addr):
        # dont accsept connection if two peer are active
        if self.num_connections == 2:
            return
        # accsept connection if number of connection below 2
        return MyProtocol(self)

# create TCP connection on port 2345
endpoint = TCP4ServerEndpoint(reactor, 2345)
# listen port for recive connection
endpoint.listen(MyFactory())
# run protocol
reactor.run()
