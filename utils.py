import os
from omegaconf import OmegaConf
from hydra import compose


from modular_rollouts.IsaacGymEnvs.isaacgymenvs.utils.reformat import (
    omegaconf_to_dict,
)


def get_isaac_cfg(task_name):
    # hydra must have been initialized already.
    cfg = compose(config_name="config.yaml", overrides=[f"task={task_name}"])
    print("Num_Envs : ", cfg.task.env.numEnvs)
    task_cfg = omegaconf_to_dict(cfg.task)
    return task_cfg
