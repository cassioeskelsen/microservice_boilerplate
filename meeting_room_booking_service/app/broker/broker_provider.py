from abc import ABC, abstractmethod

class BrokerProvider(ABC):

    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def declare_channels(self, channel_names):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get_next_message(self):
        pass
    
    @abstractmethod
    def send_message(self, topic):
        pass

    @abstractmethod
    def send_message(self, topic, routing_key):
        pass

    