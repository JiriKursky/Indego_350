"""Constants for Indego integration."""
DOMAIN = "indego"
DATA_UPDATED = f"{DOMAIN}_data_updated"
CONF_ATTR = "attributes"
CONF_SEND_COMMAND = "command"
CONF_SMARTMOWING = "enable"
CONF_DOWNLAD_MAP = "filename"
CONF_POLLING = "polling"
DEFAULT_NAME = "Indego"
DEFAULT_NAME_COMMANDS = None
DEFAULT_MAP_NAME = "indego_map"
SERVICE_NAME_COMMAND = "command"
SERVICE_NAME_SMARTMOW = "smartmowing"
SERVICE_NAME_UPDATE_STATE = "update_state"
SERVICE_NAME_DOWNLOAD_MAP = "download_map"
SENSOR_TYPE = "sensor"
BINARY_SENSOR_TYPE = "binary_sensor"
INDEGO_COMPONENTS = [SENSOR_TYPE, BINARY_SENSOR_TYPE]
ENTITY_ONLINE = "online"
ENTITY_UPDATE_AVAILABLE = "update_available"
ENTITY_ALERT = "alert"
ENTITY_MOWER_STATE = "mower_state"
ENTITY_MOWER_STATE_DETAIL = "mower_state_detail"
ENTITY_BATTERY = "battery_percentage"
ENTITY_LAWN_MOWED = "lawm_mowed"
ENTITY_LAST_COMPLETED = "last_completed"
ENTITY_NEXT_MOW = "next_mow"
ENTITY_MOWING_MODE = "mowing_mode"
ENTITY_RUNTIME = "runtime_total"
ENTITY_MOWER_ALERT = "mower_alert"
ENTITY_MOWER_POSITION = "mower_position"
