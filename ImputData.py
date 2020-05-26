import numpy as np
import scipy
import pysptk
import pyworld as pw

from utils import SignalProcessingTools as spt
from utils import PlotFigure as pf

def read_audio(FilePath):
    data, fs = spt.read_data(FilePath)
    fo, sp, ap = spt.get_para(data, fs)
    mcep = spt.sp2mc(sp)

    return fo, mcep

def standardization(x, axis=None, ddof=0):
    x_mean = x.mean(axis=axis, keepdims=True)
    x_std = x.std(axis=axis, keepdims=True, ddof=ddof)
    return (x - x_mean) / x_std

def check_silent(val):
    if val != 0:
        status = 1
    else:
        status = 0
    return status

def getInputaData(fo, mcep):
    mcep_array = np.zeros((5, 39))
    fo_array = np.zeros(5)

    mcep_array[2, :] = mcep[0, 1:40]
    mcep_array[3, :] = mcep[1, 1:40]
    mcep_array[4, :] = mcep[2, 1:40]
    mcep_array_std = standardization(mcep_array)
    mcep_array_std_flat = mcep_array_std.flatten()

    # check silent
    fo_array[2] = check_silent(fo[0])
    fo_array[3] = check_silent(fo[1])
    fo_array[4] = check_silent(fo[2])

    return mcep_array_std_flat, fo_array

# def plotParam(fo, mcep):
#     pf.plot_1figure(fo)
#     # pf.save_animation(mcep)


if __name__ == '__main__':
    FilePath = "./Data/jvs001/VOICEACTRESS100_001.wav"

    fo, mcep = read_audio(FilePath)
    getInputaData(fo, mcep)
    # plotParam(fo, mcep)