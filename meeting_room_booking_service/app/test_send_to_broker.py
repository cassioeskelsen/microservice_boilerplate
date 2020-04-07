from app.broker.broker_producer import BrokerProducer

broker = BrokerProducer()

broker.send_message('topico','{"campo":"valor"')