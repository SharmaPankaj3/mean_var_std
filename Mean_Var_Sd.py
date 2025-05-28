import numpy as np

# Step1 : create function

def calculate(Data):
    if len(Data) != 9:
        raise ValueError("List must contain nine numbers")
    matrix = np.array(Data).reshape(3,3)

    Stats_Summary = {
        'mean':[matrix.mean(axis = 0).tolist(),matrix.mean(axis = 1).tolist(),matrix.mean().item()],
                     'variance':[matrix.var(axis = 0).tolist(),matrix.var(axis = 1).tolist(),matrix.var().item()],
                     'SD':[matrix.std(axis = 0).tolist(),matrix.std(axis = 1).tolist(),matrix.std().item()],
                     'max':[matrix.max(axis = 0).tolist(),matrix.max(axis = 1).tolist(),matrix.max().item()],
                     'min':[matrix.min(axis = 0).tolist(),matrix.min(axis = 1).tolist(),matrix.min().item()],
                     'sum':[matrix.sum(axis = 0).tolist(),matrix.sum(axis = 1).tolist(),matrix.sum().item()]

                     }
    return Stats_Summary

    # Step2: Compute Stats Summary
