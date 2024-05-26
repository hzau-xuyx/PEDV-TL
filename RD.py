import subprocess

command = (
    f"python ./generatorFeatures_2.py "
    f"./dataset/natural_product.csv "
    f"./dataset/natural_product.npy "
    f"1"#有名1，无名0
)
subprocess.run(command, shell=True)

