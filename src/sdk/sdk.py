"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .appentitlementowners import AppEntitlementOwners
from .appentitlements import AppEntitlements
from .appentitlementsearch import AppEntitlementSearch
from .appentitlementuserbinding import AppEntitlementUserBinding
from .appowners import AppOwners
from .appreport import AppReport
from .appreportaction import AppReportAction
from .appresource import AppResource
from .appresourceowners import AppResourceOwners
from .appresourcesearch import AppResourceSearch
from .appresourcetype import AppResourceType
from .apps import Apps
from .appsearch import AppSearch
from .appusagecontrols import AppUsageControls
from .appuser import AppUser
from .attributes import Attributes
from .attributesearch import AttributeSearch
from .auth import Auth
from .awsexternalidsettings import AWSExternalIDSettings
from .connector import Connector
from .directory import Directory
from .personalclient import PersonalClient
from .policies import Policies
from .policysearch import PolicySearch
from .policyvalidate import PolicyValidate
from .requestcatalogmanagement import RequestCatalogManagement
from .requestcatalogsearch import RequestCatalogSearch
from .roles import Roles
from .sdkconfiguration import SDKConfiguration
from .sessionsettings import SessionSettings
from .task import Task
from .taskactions import TaskActions
from .tasksearch import TaskSearch
from .user import User
from .usersearch import UserSearch
from .webhooks import Webhooks
from sdk import utils
from sdk._hooks import SDKHooks
from sdk.models import shared
from typing import Callable, Dict, Optional, Union

class SDK:
    r"""ConductorOne API: The ConductorOne API is a HTTP API for managing ConductorOne resources."""
    apps: Apps
    connector: Connector
    app_entitlements: AppEntitlements
    app_entitlement_user_binding: AppEntitlementUserBinding
    app_entitlement_owners: AppEntitlementOwners
    app_owners: AppOwners
    app_report: AppReport
    app_report_action: AppReportAction
    app_resource_type: AppResourceType
    app_resource: AppResource
    app_resource_owners: AppResourceOwners
    app_usage_controls: AppUsageControls
    app_user: AppUser
    attributes: Attributes
    auth: Auth
    request_catalog_management: RequestCatalogManagement
    directory: Directory
    personal_client: PersonalClient
    roles: Roles
    policies: Policies
    policy_validate: PolicyValidate
    app_resource_search: AppResourceSearch
    app_search: AppSearch
    attribute_search: AttributeSearch
    app_entitlement_search: AppEntitlementSearch
    policy_search: PolicySearch
    request_catalog_search: RequestCatalogSearch
    task_search: TaskSearch
    user_search: UserSearch
    aws_external_id_settings: AWSExternalIDSettings
    session_settings: SessionSettings
    task: Task
    task_actions: TaskActions
    user: User
    webhooks: Webhooks

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: Union[shared.Security,Callable[[], shared.Security]] = None,
                 tenant_domain: str = None,
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[utils.RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :type security: Union[shared.Security,Callable[[], shared.Security]]
        :param tenant_domain: Allows setting the tenantDomain variable for url substitution
        :type tenant_domain: str
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
        server_defaults = [
            {
                'tenantDomain': tenant_domain or 'example',
            },
        ]

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server_idx,
            server_defaults,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration._hooks = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.apps = Apps(self.sdk_configuration)
        self.connector = Connector(self.sdk_configuration)
        self.app_entitlements = AppEntitlements(self.sdk_configuration)
        self.app_entitlement_user_binding = AppEntitlementUserBinding(self.sdk_configuration)
        self.app_entitlement_owners = AppEntitlementOwners(self.sdk_configuration)
        self.app_owners = AppOwners(self.sdk_configuration)
        self.app_report = AppReport(self.sdk_configuration)
        self.app_report_action = AppReportAction(self.sdk_configuration)
        self.app_resource_type = AppResourceType(self.sdk_configuration)
        self.app_resource = AppResource(self.sdk_configuration)
        self.app_resource_owners = AppResourceOwners(self.sdk_configuration)
        self.app_usage_controls = AppUsageControls(self.sdk_configuration)
        self.app_user = AppUser(self.sdk_configuration)
        self.attributes = Attributes(self.sdk_configuration)
        self.auth = Auth(self.sdk_configuration)
        self.request_catalog_management = RequestCatalogManagement(self.sdk_configuration)
        self.directory = Directory(self.sdk_configuration)
        self.personal_client = PersonalClient(self.sdk_configuration)
        self.roles = Roles(self.sdk_configuration)
        self.policies = Policies(self.sdk_configuration)
        self.policy_validate = PolicyValidate(self.sdk_configuration)
        self.app_resource_search = AppResourceSearch(self.sdk_configuration)
        self.app_search = AppSearch(self.sdk_configuration)
        self.attribute_search = AttributeSearch(self.sdk_configuration)
        self.app_entitlement_search = AppEntitlementSearch(self.sdk_configuration)
        self.policy_search = PolicySearch(self.sdk_configuration)
        self.request_catalog_search = RequestCatalogSearch(self.sdk_configuration)
        self.task_search = TaskSearch(self.sdk_configuration)
        self.user_search = UserSearch(self.sdk_configuration)
        self.aws_external_id_settings = AWSExternalIDSettings(self.sdk_configuration)
        self.session_settings = SessionSettings(self.sdk_configuration)
        self.task = Task(self.sdk_configuration)
        self.task_actions = TaskActions(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
        self.webhooks = Webhooks(self.sdk_configuration)
