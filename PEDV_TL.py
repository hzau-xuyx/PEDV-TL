import subprocess
for i in range(20):
    # 构建命令行命令
    command = (
        f"python ./finetune.py "
        f"--gpu 0 " 
        f"--data_path ./dataset/PEDV_train.csv "
        f"--features_path ./dataset/PEDV_train.npy "
        # 每次更改PEDV目录
        f"--save_dir ./model/PEDV_TL/ftmodel_ffnlayer_fold_{i} "
        f"--seed {i} "
        # 更改对应COVIDVS目录
        f"--checkpoint_path ./model/COVIDVS/fold_{i}/model_0/model.pt "
        f"--split_sizes 0.8 0.1 0.1 "
        #更改对应超参数
        f"--config_path ./hyperopt_it20_0.json "
        f"--dataset_type classification "
        #学习率
        f"--init_lr 1e-6 "
        #数据集被分成多个较小的批次，每个批次包含一定数量的样本
        f"--batch_size 20 "
        #一个epoch指的是整个训练数据集完整地通过神经网络一次的过程
        f"--epochs 30"
    )
    
    # 使用subprocess.run执行命令
    subprocess.run(command, shell=True)
