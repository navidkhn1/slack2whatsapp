# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class EntityList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid):
        """
        Initialize the EntityList

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.

        :returns: twilio.rest.preview.authy.service.entity.EntityList
        :rtype: twilio.rest.preview.authy.service.entity.EntityList
        """
        super(EntityList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/Entities'.format(**self._solution)

    def create(self, identity):
        """
        Create a new EntityInstance

        :param unicode identity: Unique identity of the Entity

        :returns: Newly created EntityInstance
        :rtype: twilio.rest.preview.authy.service.entity.EntityInstance
        """
        data = values.of({'Identity': identity, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return EntityInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def stream(self, limit=None, page_size=None):
        """
        Streams EntityInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.authy.service.entity.EntityInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists EntityInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.authy.service.entity.EntityInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of EntityInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EntityInstance
        :rtype: twilio.rest.preview.authy.service.entity.EntityPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return EntityPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EntityInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EntityInstance
        :rtype: twilio.rest.preview.authy.service.entity.EntityPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return EntityPage(self._version, response, self._solution)

    def get(self, identity):
        """
        Constructs a EntityContext

        :param identity: Unique identity of the Entity

        :returns: twilio.rest.preview.authy.service.entity.EntityContext
        :rtype: twilio.rest.preview.authy.service.entity.EntityContext
        """
        return EntityContext(self._version, service_sid=self._solution['service_sid'], identity=identity, )

    def __call__(self, identity):
        """
        Constructs a EntityContext

        :param identity: Unique identity of the Entity

        :returns: twilio.rest.preview.authy.service.entity.EntityContext
        :rtype: twilio.rest.preview.authy.service.entity.EntityContext
        """
        return EntityContext(self._version, service_sid=self._solution['service_sid'], identity=identity, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Authy.EntityList>'


class EntityPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the EntityPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Sid.

        :returns: twilio.rest.preview.authy.service.entity.EntityPage
        :rtype: twilio.rest.preview.authy.service.entity.EntityPage
        """
        super(EntityPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EntityInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.authy.service.entity.EntityInstance
        :rtype: twilio.rest.preview.authy.service.entity.EntityInstance
        """
        return EntityInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Authy.EntityPage>'


class EntityContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, identity):
        """
        Initialize the EntityContext

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.
        :param identity: Unique identity of the Entity

        :returns: twilio.rest.preview.authy.service.entity.EntityContext
        :rtype: twilio.rest.preview.authy.service.entity.EntityContext
        """
        super(EntityContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'identity': identity, }
        self._uri = '/Services/{service_sid}/Entities/{identity}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a EntityInstance

        :returns: Fetched EntityInstance
        :rtype: twilio.rest.preview.authy.service.entity.EntityInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return EntityInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Authy.EntityContext {}>'.format(context)


class EntityInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, service_sid, identity=None):
        """
        Initialize the EntityInstance

        :returns: twilio.rest.preview.authy.service.entity.EntityInstance
        :rtype: twilio.rest.preview.authy.service.entity.EntityInstance
        """
        super(EntityInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'identity': payload['identity'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'identity': identity or self._properties['identity'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: EntityContext for this EntityInstance
        :rtype: twilio.rest.preview.authy.service.entity.EntityContext
        """
        if self._context is None:
            self._context = EntityContext(
                self._version,
                service_sid=self._solution['service_sid'],
                identity=self._solution['identity'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Entity.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def identity(self):
        """
        :returns: Unique identity of the Entity
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: Service Sid.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def date_created(self):
        """
        :returns: The date this Entity was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Entity was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: Nested resource URLs.
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a EntityInstance

        :returns: Fetched EntityInstance
        :rtype: twilio.rest.preview.authy.service.entity.EntityInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Authy.EntityInstance {}>'.format(context)
