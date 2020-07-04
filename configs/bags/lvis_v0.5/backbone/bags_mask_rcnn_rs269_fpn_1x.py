_base_ = [
    '../../../_base_/models/bags/mask_rcnn_rs269_fpn.py',
    '../../../_base_/datasets/lvis_instance.py',
    '../../../_base_/schedules/schedule_1x.py', '../../../_base_/default_runtime.py'
]
data = dict(samples_per_gpu=1)