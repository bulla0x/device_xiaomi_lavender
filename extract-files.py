#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/lavender',
    'hardware/qcom-caf/common/libqti-perfd-client',
    'hardware/qcom-caf/sdm660',
    'hardware/qcom-caf/wlan',
    'hardware/xiaomi',
    'vendor/xiaomi/lavender',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/data-ipa-cfg-mgr-legacy-um',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'vendor/lib64/vendor.qti.hardware.alarm@1.0.so',
        'vendor/lib64/vendor.qti.data.factory@2.0.so',
        'vendor/lib64/vendor.qti.data.factory@2.1.so',
        'vendor/lib64/vendor.qti.data.factory@2.2.so',
        'vendor/lib64/vendor.qti.data.factory@2.3.so',
        'vendor/lib64/vendor.qti.data.mwqem@1.0.so',
        'vendor/lib64/vendor.qti.data.slm@1.0.so',
        'vendor/lib64/vendor.qti.hardware.data.cne.internal.api@1.0.so',
        'vendor/lib64/vendor.qti.hardware.data.cne.internal.constants@1.0.so',
        'vendor/lib64/vendor.qti.hardware.data.cne.internal.server@1.0.so',
        'vendor/lib64/vendor.qti.hardware.data.connection@1.0.so',
        'vendor/lib64/vendor.qti.hardware.data.connection@1.1.so',
        'vendor/lib64/vendor.qti.hardware.data.dynamicdds@1.0.so',
        'vendor/lib64/vendor.qti.hardware.data.dynamicdds@1.1.so',
        'vendor/lib64/vendor.qti.hardware.data.flow@1.0.so',
        'vendor/lib64/vendor.qti.hardware.data.iwlan@1.0.so',
        'vendor/lib64/vendor.qti.hardware.data.latency@1.0.so',
        'vendor/lib64/vendor.qti.hardware.data.lce@1.0.so',
        'vendor/lib64/vendor.qti.hardware.data.qmi@1.0.so',
        'vendor/lib64/vendor.qti.hardware.slmadapter@1.0.so',
        'vendor/lib64/vendor.qti.latency@2.0.so',
        'vendor/lib64/vendor.qti.latency@2.1.so',
        'vendor/lib/com.qualcomm.qti.dpm.api@1.0.so',
        'vendor/lib64/com.qualcomm.qti.dpm.api@1.0.so',
        'vendor/lib/vendor.qti.hardware.tui_comm@1.0.so',
        'vendor/lib64/vendor.qti.hardware.tui_comm@1.0.so',
        'vendor/lib/vendor.qti.hardware.qseecom@1.0.so',
        'vendor/lib64/vendor.qti.hardware.qseecom@1.0.so',
        'vendor/lib/vendor.qti.hardware.mwqemadapter@1.0.so',
        'vendor/lib64/vendor.qti.hardware.mwqemadapter@1.0.so',
        'vendor/lib64/vendor.qti.hardware.radio.am@1.0.so',
        'vendor/lib64/vendor.qti.hardware.radio.lpa@1.0.so',
        'vendor/lib64/vendor.qti.hardware.radio.lpa@1.1.so',
        'vendor/lib64/vendor.qti.hardware.radio.lpa@1.2.so',
        'vendor/lib64/vendor.qti.hardware.radio.qtiradio@1.0.so',
        'vendor/lib64/vendor.qti.hardware.radio.qtiradio@2.0.so',
        'vendor/lib64/vendor.qti.hardware.radio.qtiradio@2.1.so',
        'vendor/lib64/vendor.qti.hardware.radio.qtiradio@2.2.so',
        'vendor/lib64/vendor.qti.hardware.radio.qtiradio@2.3.so',
        'vendor/lib64/vendor.qti.hardware.radio.qtiradio@2.4.so',
        'vendor/lib64/vendor.qti.hardware.radio.qtiradio@2.5.so',
        'vendor/lib64/vendor.qti.hardware.radio.qtiradio@2.6.so',
        'vendor/lib64/vendor.qti.hardware.radio.qtiradio@2.7.so',
        'vendor/lib64/vendor.qti.hardware.radio.uim@1.0.so',
        'vendor/lib64/vendor.qti.hardware.radio.uim@1.1.so',
        'vendor/lib64/vendor.qti.hardware.radio.uim@1.2.so',
        'vendor/lib64/vendor.qti.hardware.radio.uim_remote_client@1.0.so',
        'vendor/lib64/vendor.qti.hardware.radio.uim_remote_client@1.1.so',
        'vendor/lib64/vendor.qti.hardware.radio.uim_remote_client@1.2.so',
        'vendor/lib64/vendor.qti.hardware.radio.uim_remote_server@1.0.so',
        'vendor/lib64/com.qualcomm.qti.imscmservice@2.0.so',
        'vendor/lib64/com.qualcomm.qti.imscmservice@2.1.so',
        'vendor/lib64/com.qualcomm.qti.imscmservice@2.2.so',
        'vendor/lib64/com.qualcomm.qti.uceservice@2.0.so',
        'vendor/lib64/com.qualcomm.qti.uceservice@2.1.so',
        'vendor/lib64/com.qualcomm.qti.uceservice@2.2.so',
        'vendor/lib64/com.qualcomm.qti.uceservice@2.3.so',
        'vendor/lib64/vendor.qti.hardware.radio.ims@1.0.so',
        'vendor/lib64/vendor.qti.hardware.radio.ims@1.1.so',
        'vendor/lib64/vendor.qti.hardware.radio.ims@1.2.so',
        'vendor/lib64/vendor.qti.hardware.radio.ims@1.3.so',
        'vendor/lib64/vendor.qti.hardware.radio.ims@1.4.so',
        'vendor/lib64/vendor.qti.hardware.radio.ims@1.5.so',
        'vendor/lib64/vendor.qti.hardware.radio.ims@1.6.so',
        'vendor/lib64/vendor.qti.hardware.radio.ims@1.7.so',
        'vendor/lib64/vendor.qti.hardware.radio.ims@1.8.so',
        'vendor/lib64/vendor.qti.ims.callcapability@1.0.so',
        'vendor/lib64/vendor.qti.ims.callinfo@1.0.so',
        'vendor/lib64/vendor.qti.ims.factory@1.0.so',
        'vendor/lib64/vendor.qti.ims.factory@1.1.so',
        'vendor/lib64/vendor.qti.ims.rcsconfig@1.0.so',
        'vendor/lib64/vendor.qti.ims.rcsconfig@1.1.so',
        'vendor/lib64/vendor.qti.ims.rcsconfig@2.0.so',
        'vendor/lib64/vendor.qti.ims.rcsconfig@2.1.so',
        'vendor/lib64/vendor.qti.imsrtpservice@3.0.so',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/lib/soundfx/libdirac.so': blob_fixup()
        .add_needed('liglog.so'),
    ('vendor/lib64/hw/consumerir.lirc.sdm660.so', 'consumerir.spi.sdm660.so'): blob_fixup()
        .fix_soname(),
    'system_ext/lib64/libqxrsplitauxservice.qti.so': blob_fixup()
        .replace_needed('android.media.audio.common.types-V3-cpp.so', 'android.media.audio.common.types-V4-cpp.so')
        .add_needed('libaudioclient_shim.so')
        .add_needed('libwfdservice_shim.so'),
    ('vendor/lib/libts_face_beautify_hal.so', 'vendor/lib/libts_detected_face_hal.so', 'vendor/lib/lib_lowlight.so'): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    ('vendor/lib64/libvendor.goodix.hardware.interfaces.biometrics.fingerprint@2.1.so', 'vendor/lib64/hw/fingerprint.fpc.default.so', 'vendor.qti.hardware.fingerprint@1.0.so'): blob_fixup()
        .remove_needed('libhidltransport.so')
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    ('vendor/lib64/hw/camera.qcom.so', 'vendor/lib64/libFaceDetectpp-0.5.2.so', 'vendor/lib64/libfacedet.so'): blob_fixup()
        .binary_regex_replace(b'libmegface.so', b'libfacedet.so')
        .binary_regex_replace(b'libMegviiFacepp-0.5.2.so', b'libFaceDetectpp-0.5.2.so')
        .binary_regex_replace(b'megviifacepp_0_5_2_model', b'facedetectpp_0_5_2_model'),
    'vendor/lib/libmmcamera_faceproc.so': blob_fixup()
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    'vendor/bin/mm-pp-dpps': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2_1.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'lavender',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
