#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common LineageOS stuff
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from lavender device
$(call inherit-product, $(LOCAL_PATH)/device.mk)

PRODUCT_BRAND := Xiaomi
PRODUCT_DEVICE := lavender
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_NAME := lineage_lavender
PRODUCT_MODEL := Redmi Note 7

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

# AxionAOSP stuff
AXION_MAINTAINER := Amrito_Karmokar
AXION_PROCESSOR := Snapdragon_660™
AXION_CAMERA_REAR_INFO := 48,5
AXION_CAMERA_FRONT_INFO := 13
GPU_FREQS_PATH := /sys/class/kgsl/kgsl-3d0/devfreq/available_frequencies
GPU_MIN_FREQ_PATH := /sys/class/kgsl/kgsl-3d0/devfreq/min_freq
PERF_DEFAULT_GOV := schedutil
PERF_GOV_SUPPORTED := true
TORCH_STR_SUPPORTED := true
PERF_ANIM_OVERRIDE := true
