##########################################################################
##                      DUBLIN CONVERTER SCRIPT                         ##
##                                                                      ##
##      SCRIPT TO CONVERT THE OSCILLOSCOPE .dat FILES IN TTRE           ##
##   Works converting and merging all the file inside the input folder  ##
##########################################################################

import time
#import matplotlib.pyplot as plt # https://matplotlib.org/
import ROOT
import numpy as np # http://www.numpy.org/
import os,sys
import ctypes
import optparse
import argparse

from root import TFile, TTree
from array import array
from root_numpy import array2tree
from root_numpy import array2root
import re
import os
# from ROOT import TFile, TTree



# The code requires the complete input folder directory to run
parser = argparse.ArgumentParser(description='Run info.')
parser.add_argument('--path', metavar='path', type=str, help='Path to the input file',required=True)
args = parser.parse_args()

# Declare Input folder
in_folder = str(args.path)

# Open input folder
os.chdir(in_folder)

# Declare the output file name and path


for filename in os.listdir(in_folder):
        # Parsing the info of the input file's name
    if filename.endswith(".txt"):
        Position, RunNumber, MU, TotTime, energy, beamSize, attenuator, HV = filename.split("_")

    out_folder = "tree_produced"
    out_name = Position + ("_") + energy + ("_") + HV + ("_") + MU + ("_") + TotTime ("_") + beamSize ("_") + attenuator + ("_v1")
    outputfile = in_folder + '/%s/%s.root'%(out_folder,out_name)

    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

# TrigNumber = np.zeros(1,dtype=np.int32)
# Aaxis = np.zeros(1,dtype=np.int32)
# Baxis = np.zeros(1,dtype=np.int32)
# Caxis = np.zeros(1,dtype=np.int32)
SampleNum = 0
TimeDiv = 4.0e-10

print(len(Caxis))

f = TFile( outputfile, 'recreate' )
t = TTree( 'ttree', 'Test beam samples' )
t.Branch( 'Aaxis', Aaxis, 'Aaxis/I' )
t.Branch( 'Baxis', Baxis, 'Baxis/I' )
t.Branch( 'Caxis', Caxis, 'Caxis[1]/I' )
# t.Branch( 'TrigNumber', TrigNumber, 'TrigNumber[1]/I' )

SamplesNumber = 25000
Voltage = np.zeros(SamplesNumber,dtype=np.float)
Time = np.zeros(SamplesNumber,dtype=np.float)
t.Branch( 'Time', Time, 'time[{}]/f'.format(SamplesNumber))
t.Branch( 'Voltage', Voltage, 'voltage[{}]/f'.format(SamplesNumber))

for filename in os.listdir(in_folder):
    # Split the headers and extract the useful info
    fh = open(filename)
    time = 0.0
    TimeDiv = float(TimeDiv)

    for i,tt in enumerate(np.linspace(0,(SamplesNumber-1)*TimeDiv,SamplesNumber)):
        Time[i] = tt

        if int(numberOfSamples) != SamplesNumber:
            print('Strange numberOfSamples: {}'.format(numberOfSamples))
        while True:
        # read line
            line = fh.readline()
        # check if line is not empty
            if not line:
                print('Strange line: {}'.format(line))
                break

            #if the line doesen't contain text
            if not any(c.isalpha() for c in line):
                if SampleNum < Voltage.size:
                    Voltage[SampleNum] = float(line)
                    SampleNum += 1
            # else:
            #     if SampleNum == SamplesNumber:
            #         SampleNum = 0
            #         t.Fill()
            #         TrigNumber += 1
                #     # print('Looping -- Xaxis: {}  TrigNumber{}'.format(Caxis_tmp,TrigNumber))
                # elif SampleNum > 0:
                #     print('Strange SampleNum: {}'.format(SampleNum))
                fh.readline()

    t.Fill()
    fh.close()

        # else:
        #     continue

#ok
# Write in the output root file
f.Write()
f.Close()
