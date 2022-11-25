import wandb

wandb.login()
# wandb.init(project="aistages_level2_competition", entity="level2_3")
checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='WandbLoggerHook',interval=50,
            init_kwargs=dict(
                project='Object_Detection',
                entity = 'aitech4_cv3',
                name = "faster_rcnn_r50_fpn_1x_coco_resize_autoaug(YH)"),)
            #     log_checkpoint=True,
            # log_checkpoint_metadata=True,
            # num_eval_images=100,
            # bbox_score_thr=0.0),       

        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]

# disable opencv multithreading to avoid system being overloaded
opencv_num_threads = 0
# set multi-process start method as `fork` to speed up the training
mp_start_method = 'fork'

# Default setting for scaling LR automatically
#   - `enable` means enable scaling LR automatically
#       or not by default.
#   - `base_batch_size` = (8 GPUs) x (2 samples per GPU).
auto_scale_lr = dict(enable=False, base_batch_size=16)
