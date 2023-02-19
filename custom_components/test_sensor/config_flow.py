"""
Set up a config flow that asks for one entity_id and one name as input
"""

import logging
from typing import Any, Dict

from homeassistant import config_entries
import homeassistant.helpers.config_validation as cv
from homeassistant import data_entry_flow
import voluptuous as vol

from .const import (
    DOMAIN,
    CONF_ENTITY,
    CONF_NAME
)

_LOGGER = logging.getLogger(__name__)

TEST_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ENTITY): cv.string,
        vol.Required(CONF_NAME): cv.string
    }
)


class TestConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> data_entry_flow.FlowResult:
        """Invoked when user initiates adding integration from UI"""
        errors: Dict[str, str] = {}
        if user_input is not None:
            self.data = user_input
            _LOGGER.debug(user_input.get(CONF_ENTITY))
            _LOGGER.debug(user_input.get(CONF_NAME))
            return self.async_create_entry(title="TestIntegration", data=self.data)

        return self.async_show_form(
            step_id="user", data_schema=TEST_SCHEMA, errors=errors
        )
