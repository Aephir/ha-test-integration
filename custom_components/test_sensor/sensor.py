
import logging
from collections.abc import Callable

from homeassistant import config_entries, core
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.typing import (
    ConfigType,
    DiscoveryInfoType,
    HomeAssistantType,
)

from .const import (
    DOMAIN,
    CONF_ENTITY,
    CONF_NAME
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: core.HomeAssistant,
    config_entry: config_entries.ConfigEntry,
    async_add_entities,
) -> None:
    """Setup sensors from a config entry created in the integrations UI."""
    config = hass.data[DOMAIN][config_entry.entry_id]
    sensors = [TestSensor(hass, config)]
    async_add_entities(sensors, update_before_add=True)


async def async_setup_platform(
    hass: HomeAssistantType,
    config: ConfigType,
    async_add_entities: Callable,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""
    sensors = [TestSensor(hass, config)]
    async_add_entities(sensors, update_before_add=True)


class TestSensor(Entity):

    def __init__(self, hass: HomeAssistantType, config):
        """Initialize the sensor"""
        super().__init__(config)
        self.hass = hass
        self._name = config[CONF_NAME]
        self._sensor_entity = config[CONF_ENTITY]

        self._state = None
        self.attrs = {}

        self.config = config

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the name of the sensor."""
        return self._state

    @property
    def unique_id(self):
        unique_id = "test_integration_unique_id"
        _LOGGER.debug("Unique ID is: " + unique_id)
        return unique_id

    @property
    def extra_state_attributes(self):
        return self.attrs

    async def async_update(self) -> None:
        """Update all sensors."""
        self._state = 100
        self.attrs["dummy_attribute"] = "dummy"
        self.attrs["input_sensor_state"] = self._sensor_entity
        self.attrs["input_sensor_state"] = self._sensor_entity.state
