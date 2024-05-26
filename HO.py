import subprocess

command = (
    f"python ./hyperparameter_optimization.py "
    f"--gpu 0 "
    f"--data_path ./dataset/Human_CoV.csv "
    f"--features_path ./dataset4/Human_CoV.npy "
    f"--no_features_scaling "
    f"--dataset_type classification  "
    #可更改迭代次数 原始是20
    f"--num_iters 50 "
    #每次更改超参数的命名
    f"--config_save_path ./hyperopt_it20_0.json"
)
subprocess.run(command, shell=True)

