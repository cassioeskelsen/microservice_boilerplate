from app.broker.broker_configuration import DEFAULT_BROKER_CONFIGURATION_CLASS
from app.broker.broker_configuration import DEFAULT_BROKER_PROVIDER_CLASS
from app.broker.broker_provider import BrokerProvider


class BrokerProviderFactory(object):
    _BROKER_PROVIDER = None

    @classmethod
    def get_instance(self, db_provider_class=DEFAULT_BROKER_PROVIDER_CLASS, db_configuration=DEFAULT_BROKER_CONFIGURATION_CLASS):
        """
        Gets a default db provider instance.
        Creates one if it hasn't been created yet.
        :returns: DbProvider
        """
        if not db_provider_class or not issubclass(db_provider_class, BrokerProvider):
            raise TypeError('The db provider class must be of a subclass of {0}'.format(BrokerProvider.__name__))
        if not BrokerProviderFactory._DB_PROVIDER:
            BrokerProviderFactory._DB_PROVIDER = db_provider_class(db_configuration)
            BrokerProviderFactory._DB_PROVIDER.connect()
        return BrokerProviderFactory._DB_PROVIDER
