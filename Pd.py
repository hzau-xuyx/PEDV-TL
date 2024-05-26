import subprocess

command = (
    f"python ./predict.py "
    f"--gpu 0 "
    #采用的数据集
    f"--test_path ./dataset/natural_product.csv "
    f"--features_path ./dataset/natural_product.npy "
    #保存名称
    f"--preds_path ./predict/natural_product.csv "
    #模型位置
    f"--checkpoint_dir ./model/PEDV_TL "
    f"--use_compound_names"
)

subprocess.run(command, shell=True)