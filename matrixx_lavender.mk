#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Disable EPPE for devices that don't support it
TARGET_DISABLE_EPPE := true

# Inherit some common LineageOS stuff
$(call inherit-product, vendor/matrixx/config/common_full_phone.mk)

# Inherit from lavender device
$(call inherit-product, $(LOCAL_PATH)/device.mk)

PRODUCT_BRAND := Xiaomi
PRODUCT_DEVICE := lavender
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_NAME := matrixx_lavender
PRODUCT_MODEL := Redmi Note 7

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

# Project_Matrixx stuff
MATRIXX_BUILD_TYPE := OFFICIAL
MATRIXX_MAINTAINER := Jyotishman_baruah(BULLA)
TARGET_FACE_UNLOCK_SUPPORTED := true
TARGET_CUSTOM_UDFPS := false
WITH_GMS := true
WITH_GMS_COMMS_SUITE := false
WITH_GMS_AICORE := true
TARGET_INCLUDE_PIXEL_LAUNCHER := true
TARGET_DEFAULT_PIXEL_LAUNCHER := true
WITH_BCR := false
PRODUCT_NO_CAMERA := true
TARGET_INCLUDE_MATLOG := false
TARGET_OPTIMIZED_DEXOPT := false
SURFACE_FLINGER_BOOST := false
HBM_SUPPORTED := false
USE_REALITY_ENGINE := true
