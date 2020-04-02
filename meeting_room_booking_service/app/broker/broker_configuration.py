from app.broker.rabbit.rabbit_provider import RabbitMQProvider
from app.broker.rabbit.rabbit_configuration import RabbitConfiguration

# TODO: get this configuration from env variables or something like that
DEFAULT_BROKER_PROVIDER_CLASS = RabbitMQProvider
DEFAULT_BROKER_CONFIGURATION_CLASS = RabbitConfiguration
