from typing import Dict, Any

from api_integration.api_registry import APIRegistry
from api_integration.api_mapper import APIMapper
from api_integration.processing_strategy import ProcessingStrategy
from api_integration.authentication import APIAuthentication


class IntegrationController:

    @classmethod
    def build_integration_plan(cls) -> Dict[str, Any]:

        integration_plan = {}

        for api_name in APIRegistry.list_apis():

            integration_plan[api_name] = {
                "api": APIRegistry.get_api(api_name),
                "mapping": APIMapper.get_mapping(api_name),
                "processing": ProcessingStrategy.get_strategy(api_name),
            }

        return {
            "apis": integration_plan,
            "security": APIAuthentication.create_security_policy(),
            "status": "proposed",
        }