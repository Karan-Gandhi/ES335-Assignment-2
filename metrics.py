import numpy as np

def calculate_rmse(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    rmse = np.sqrt(mse)
    return rmse

def calculate_psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = np.max(original)
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

