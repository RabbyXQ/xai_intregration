# Android Permissions with Numerical Priority by Grok 3 (xAI)
# Date: March 15, 2025

# Define permission categories as dictionaries with numerical priorities
normal_permissions = {
    25: "ACCESS_NETWORK_STATE",
    24: "ACCESS_WIFI_STATE",
    23: "BLUETOOTH",
    22: "BLUETOOTH_ADMIN",
    21: "CHANGE_NETWORK_STATE",
    20: "CHANGE_WIFI_STATE",
    19: "EXPAND_STATUS_BAR",
    18: "FOREGROUND_SERVICE",
    17: "INTERNET",
    16: "KILL_BACKGROUND_PROCESSES",
    15: "MODIFY_AUDIO_SETTINGS",
    14: "NFC",
    13: "READ_SYNC_SETTINGS",
    12: "READ_SYNC_STATS",
    11: "RECEIVE_BOOT_COMPLETED",
    10: "REORDER_TASKS",
    9: "REQUEST_COMPANION_RUN_IN_BACKGROUND",
    8: "REQUEST_COMPANION_USE_DATA_IN_BACKGROUND",
    7: "SET_WALLPAPER",
    6: "SET_WALLPAPER_HINTS",
    5: "TRANSMIT_IR",
    4: "USE_BIOMETRIC",
    3: "USE_FINGERPRINT",
    2: "VIBRATE",
    1: "WAKE_LOCK"
}

dangerous_permissions = {
    55: "ACCEPT_HANDOVER",
    54: "ACCESS_BACKGROUND_LOCATION",
    53: "ACCESS_COARSE_LOCATION",
    52: "ACCESS_FINE_LOCATION",
    51: "ACCESS_MEDIA_LOCATION",
    50: "ACTIVITY_RECOGNITION",
    49: "ADD_VOICEMAIL",
    48: "ANSWER_PHONE_CALLS",
    47: "BODY_SENSORS",
    46: "CALL_PHONE",
    45: "CAMERA",
    44: "GET_ACCOUNTS",
    43: "PROCESS_OUTGOING_CALLS",
    42: "READ_CALENDAR",
    41: "READ_CALL_LOG",
    40: "READ_CONTACTS",
    39: "READ_EXTERNAL_STORAGE",
    38: "READ_PHONE_NUMBERS",
    37: "READ_PHONE_STATE",
    36: "READ_SMS",
    35: "RECEIVE_MMS",
    34: "RECEIVE_SMS",
    33: "RECEIVE_WAP_PUSH",
    32: "RECORD_AUDIO",
    31: "SEND_SMS",
    30: "USE_SIP",
    29: "WRITE_CALENDAR",
    28: "WRITE_CALL_LOG",
    27: "WRITE_CONTACTS",
    26: "WRITE_EXTERNAL_STORAGE"
}

special_permissions = {
    65: "MANAGE_EXTERNAL_STORAGE",
    64: "SYSTEM_ALERT_WINDOW",
    63: "WRITE_SETTINGS",
    62: "REQUEST_INSTALL_PACKAGES",
    61: "POST_NOTIFICATIONS",
    60: "NEARBY_WIFI_DEVICES",
    59: "BLUETOOTH_SCAN",
    58: "BLUETOOTH_CONNECT",
    57: "BLUETOOTH_ADVERTISE",
    56: "UWB_RANGING"
}

signature_permissions = {
    113: "ACCESS_CHECKIN_PROPERTIES",
    112: "ACCOUNT_MANAGER",
    111: "BATTERY_STATS",
    110: "BIND_ACCESSIBILITY_SERVICE",
    109: "BIND_APPWIDGET",
    108: "BIND_DEVICE_ADMIN",
    107: "BIND_INPUT_METHOD",
    106: "BIND_NFC_SERVICE",
    105: "BIND_NOTIFICATION_LISTENER_SERVICE",
    104: "BIND_VPN_SERVICE",
    103: "BIND_WALLPAPER",
    102: "BROADCAST_SMS",
    101: "BROADCAST_WAP_PUSH",
    100: "CHANGE_COMPONENT_ENABLED_STATE",
    99: "CLEAR_APP_CACHE",
    98: "CONTROL_LOCATION_UPDATES",
    97: "DELETE_CACHE_FILES",
    96: "DELETE_PACKAGES",
    95: "DEVICE_POWER",
    94: "DIAGNOSTIC",
    93: "DUMP",
    92: "FACTORY_TEST",
    91: "FORCE_BACK",
    90: "GET_PACKAGE_SIZE",
    89: "INSTALL_LOCATION_PROVIDER",
    88: "INSTALL_PACKAGES",
    87: "MANAGE_ACCOUNTS",
    86: "MANAGE_APP_TOKENS",
    85: "MASTER_CLEAR",
    84: "MEDIA_CONTENT_CONTROL",
    83: "MODIFY_PHONE_STATE",
    82: "MOUNT_UNMOUNT_FILESYSTEMS",
    81: "READ_LOGS",
    80: "REBOOT",
    79: "SET_ACTIVITY_WATCHER",
    78: "SET_ALWAYS_FINISH",
    77: "SET_ANIMATION_SCALE",
    76: "SET_DEBUG_APP",
    75: "SET_PREFERRED_APPLICATIONS",
    74: "SET_PROCESS_LIMIT",
    73: "SET_TIME",
    72: "SET_TIME_ZONE",
    71: "SIGNAL_PERSISTENT_PROCESSES",
    70: "STATUS_BAR",
    69: "UPDATE_DEVICE_STATS",
    68: "WRITE_APN_SETTINGS",
    67: "WRITE_GSERVICES",
    66: "WRITE_SECURE_SETTINGS"
}

other_permissions = {
    118: "PACKAGE_USAGE_STATS",
    117: "MANAGE_MEDIA",
    116: "READ_PRECISE_PHONE_STATE",
    115: "USE_FULL_SCREEN_INTENT",
    114: "SCHEDULE_EXACT_ALARM"
}

deprecated_permissions = {
    136: "ACCESS_MOCK_LOCATION",
    135: "AUTHENTICATE_ACCOUNTS",
    134: "BRICK",
    133: "BROADCAST_PACKAGE_REMOVED",
    132: "BROADCAST_STICKY",
    131: "CHANGE_WIFI_MULTICAST_STATE",
    130: "DISABLE_KEYGUARD",
    129: "GLOBAL_SEARCH",
    128: "INSTALL_SHORTCUT",
    127: "READ_PROFILE",
    126: "READ_SOCIAL_STREAM",
    125: "READ_USER_DICTIONARY",
    124: "SUBSCRIBED_FEEDS_READ",
    123: "SUBSCRIBED_FEEDS_WRITE",
    122: "UNINSTALL_SHORTCUT",
    121: "WRITE_PROFILE",
    120: "WRITE_SOCIAL_STREAM",
    119: "WRITE_USER_DICTIONARY"
}

# Priority weights for categories
priority_weights = {
    "Dangerous": 5,
    "Special": 4,
    "Signature": 3,
    "Normal": 2,
    "Other": 1,
    "Deprecated": 0
}

# Combine all permissions into a prioritized list
all_permissions = [
    ("Dangerous", dangerous_permissions),
    ("Special", special_permissions),
    ("Signature", signature_permissions),
    ("Normal", normal_permissions),
    ("Other", other_permissions),
    ("Deprecated", deprecated_permissions)
]

# Function to calculate global priority and display permissions
def display_prioritized_permissions():
    print("Android Permissions with Numerical Priority (Generated on March 15, 2025)\n")
    for category, perms in all_permissions:
        print(f"{category} Permissions (Category Weight: {priority_weights[category]})")
        # Sort by priority in descending order
        sorted_perms = sorted(perms.items(), key=lambda x: x[0], reverse=True)
        for priority, perm in sorted_perms:
            # Calculate global priority: category weight * 1000 + individual priority
            global_priority = (priority_weights[category] * 1000) + priority
            print(f"  {global_priority:04d} - {perm}")
        print()

# Execute the display function
if __name__ == "__main__":
    display_prioritized_permissions()