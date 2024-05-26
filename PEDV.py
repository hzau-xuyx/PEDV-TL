import subprocess
command = (
    f"python ./train.py "
    f"--gpu 0 "
    f"--data_path ./dataset4/output1.csv "
    f"--features_path ./dataset4/output1.npy "
    f"--no_features_scaling "
    #每次更改COVIDVS目录
    f"--save_dir ./PEDV_0_YSX/ "
    f"--dataset_type classification "
    f"--split_sizes 0.8 0.1 0.1 "
    f"--num_folds 20 "
    #更改对应超参数
    f"--config_path ./hyperopt_it20_0.json "
)
subprocess.run(command, shell=True)