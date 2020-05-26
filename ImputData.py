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

#Todo 正規化
# def getInputaData(fo, mcep):
#     array = np.zeros(40,5)
#
#     return array

# def plotParam(fo, mcep):
#     pf.plot_1figure(fo)
#     # pf.save_animation(mcep)


if __name__ == '__main__':
    FilePath = "./Data/jvs001/VOICEACTRESS100_001.wav"

    fo, mcep = read_audio(FilePath)
    # plotParam(fo, mcep)