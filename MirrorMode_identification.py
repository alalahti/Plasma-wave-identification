from ai import cdas
from datetime import datetime
from datetime import timedelta
import json
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import linalg as LA
import scipy as sp
from scipy.signal import argrelextrema
 
#Shock parameters of studied ICME sheaths listed by Palmerio et al., (2016). Parameters taken from ipshocks.fi
#B_down/B_up, theta_Bn, V_shock, M_A, ?, ?, |delta V| between down and up, Beta_upstream
def Parameters(shock, tiedosto): 
	if shock == 1:
		if tiedosto == 1:
			ResultsSimplified.write("2.97	51.26	380.00	2.90	1.41	462.075461537	26.0	6.4")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.97	51.26	380.00	2.90	1.41	462.075461537	26.0	6.4")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.97	51.26	380.00	2.90	1.41	462.075461537	26.0	6.4")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.97	51.26	380.00	2.90	1.41	462.075461537	26.0	6.4")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.97	51.26	380.00	2.90	1.41	462.075461537	26.0	6.4")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.97	51.26	380.00	2.90	1.41	462.075461537	26.0	6.4")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.97	51.26	380.00	2.90	1.41	462.075461537	26.0	6.4")
			FractionalPeaks.write("	")
	if shock == 2:
		if tiedosto == 1:
			ResultsSimplified.write("2.03	59.38	557.47	3.46	1.99	493.755594362	77	4.1")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.03	59.38	557.47	3.46	1.99	493.755594362	77	4.1")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.03	59.38	557.47	3.46	1.99	493.755594362	77	4.1")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.03	59.38	557.47	3.46	1.99	493.755594362	77	4.1")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.03	59.38	557.47	3.46	1.99	493.755594362	77	4.1")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.03	59.38	557.47	3.46	1.99	493.755594362	77	4.1")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.03	59.38	557.47	3.46	1.99	493.755594362	77	4.1")
			FractionalPeaks.write("	")
	if shock == 3:
		if tiedosto == 1:
			ResultsSimplified.write("2.49	85.73	438.40	3.85	2.68	442.147542828	76	2.1")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.49	85.73	438.40	3.85	2.68	442.147542828	76	2.1")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.49	85.73	438.40	3.85	2.68	442.147542828	76	2.1")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.49	85.73	438.40	3.85	2.68	442.147542828	76	2.1")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.49	85.73	438.40	3.85	2.68	442.147542828	76	2.1")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.49	85.73	438.40	3.85	2.68	442.147542828	76	2.1")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.49	85.73	438.40	3.85	2.68	442.147542828	76	2.1")
			FractionalPeaks.write("	")
	if shock == 4:
		#Ei loydy ipshocks eika harvard. cdaweb nakyy kylla shokki
		if tiedosto == 1:
			ResultsSimplified.write("0.00	00.00	000.00	0.00	0.00	452.466912795	0.00	0.00")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("0.00	00.00	000.00	0.00	0.00	452.466912795	0.00	0.00")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("0.00	00.00	000.00	0.00	0.00	452.466912795	0.00	0.00")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("0.00	00.00	000.00	0.00	0.00	452.466912795	0.00	0.00")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("0.00	00.00	000.00	0.00	0.00	452.466912795	0.00	0.00")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("0.00	00.00	000.00	0.00	0.00	452.466912795	0.00	0.00")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("0.00	00.00	000.00	0.00	0.00	452.466912795	0.00	0.00")
			FractionalPeaks.write("	")
	if shock == 5:
		if tiedosto == 1:
			ResultsSimplified.write("2.95	73.27	493.18	4.65	2.78	514.247618371	98	3.6")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.95	73.27	493.18	4.65	2.78	514.247618371	98	3.6")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.95	73.27	493.18	4.65	2.78	514.247618371	98	3.6")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.95	73.27	493.18	4.65	2.78	514.247618371	98	3.6")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.95	73.27	493.18	4.65	2.78	514.247618371	98	3.6")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.95	73.27	493.18	4.65	2.78	514.247618371	98	3.6")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.95	73.27	493.18	4.65	2.78	514.247618371	98	3.6")
			FractionalPeaks.write("	")
	if shock == 6:
		if tiedosto == 1:
			ResultsSimplified.write("1.61	59.10	380.18	2.71	2.08	409.287552385	71	1.4")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.61	59.10	380.18	2.71	2.08	409.287552385	71	1.4")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.61	59.10	380.18	2.71	2.08	409.287552385	71	1.4")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.61	59.10	380.18	2.71	2.08	409.287552385	71	1.4")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.61	59.10	380.18	2.71	2.08	409.287552385	71	1.4")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.61	59.10	380.18	2.71	2.08	409.287552385	71	1.4")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.61	59.10	380.18	2.71	2.08	409.287552385	71	1.4")
			FractionalPeaks.write("	")
	if shock == 7:
		#Ei loydy ipshocks eika harvard. cdaweb nakyy ~shokki
		if tiedosto == 1:
			ResultsSimplified.write("0.00	00.00	000.00	0.00	0.00	390.478923863	0.00	0.00")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("0.00	00.00	000.00	0.00	0.00	390.478923863	0.00	0.00")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("0.00	00.00	000.00	0.00	0.00	390.478923863	0.00	0.00")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("0.00	00.00	000.00	0.00	0.00	390.478923863	0.00	0.00")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("0.00	00.00	000.00	0.00	0.00	390.478923863	0.00	0.00")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("0.00	00.00	000.00	0.00	0.00	390.478923863	0.00	0.00")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("0.00	00.00	000.00	0.00	0.00	390.478923863	0.00	0.00")
			FractionalPeaks.write("	")
	if shock == 8:
		if tiedosto == 1:
			ResultsSimplified.write("2.14	29.64	662.12	3.43	2.78	643.14657118	119	1.0")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.14	29.64	662.12	3.43	2.78	643.14657118	119	1.0")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.14	29.64	662.12	3.43	2.78	643.14657118	119	1.0")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.14	29.64	662.12	3.43	2.78	643.14657118	119	1.0")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.14	29.64	662.12	3.43	2.78	643.14657118	119	1.0")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.14	29.64	662.12	3.43	2.78	643.14657118	119	1.0")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.14	29.64	662.12	3.43	2.78	643.14657118	119	1.0")
			FractionalPeaks.write("	")
	if shock == 9:
		if tiedosto == 1:
			ResultsSimplified.write("2.20	50.82	325.90	3.26	1.84	332.996186235	41	4.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.20	50.82	325.90	3.26	1.84	332.996186235	41	4.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.20	50.82	325.90	3.26	1.84	332.996186235	41	4.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.20	50.82	325.90	3.26	1.84	332.996186235	41	4.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.20	50.82	325.90	3.26	1.84	332.996186235	41	4.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.20	50.82	325.90	3.26	1.84	332.996186235	41	4.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.20	50.82	325.90	3.26	1.84	332.996186235	41	4.3")
			FractionalPeaks.write("	")
	if shock == 10:
		if tiedosto == 1:
			ResultsSimplified.write("2.82	73.67	779.81	3.39	3.06	821.463843294	209	0.5")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.82	73.67	779.81	3.39	3.06	821.463843294	209	0.5")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.82	73.67	779.81	3.39	3.06	821.463843294	209	0.5")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.82	73.67	779.81	3.39	3.06	821.463843294	209	0.5")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.82	73.67	779.81	3.39	3.06	821.463843294	209	0.5")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.82	73.67	779.81	3.39	3.06	821.463843294	209	0.5")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.82	73.67	779.81	3.39	3.06	821.463843294	209	0.5")
			FractionalPeaks.write("	")
	if shock == 11:
		if tiedosto == 1:
			ResultsSimplified.write("2.12	54.64	276.36	3.27	1.76	415.361222908	21	5.0")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.12	54.64	276.36	3.27	1.76	415.361222908	21	5.0")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.12	54.64	276.36	3.27	1.76	415.361222908	21	5.0")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.12	54.64	276.36	3.27	1.76	415.361222908	21	5.0")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.12	54.64	276.36	3.27	1.76	415.361222908	21	5.0")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.12	54.64	276.36	3.27	1.76	415.361222908	21	5.0")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.12	54.64	276.36	3.27	1.76	415.361222908	21	5.0")
			FractionalPeaks.write("	")
	if shock == 12:
		if tiedosto == 1:
			ResultsSimplified.write("2.40	59.13	778.76	4.82	3.94	647.197972458	204	1.7")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.40	59.13	778.76	4.82	3.94	647.197972458	204	1.7")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.40	59.13	778.76	4.82	3.94	647.197972458	204	1.7")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.40	59.13	778.76	4.82	3.94	647.197972458	204	1.7")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.40	59.13	778.76	4.82	3.94	647.197972458	204	1.7")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.40	59.13	778.76	4.82	3.94	647.197972458	204	1.7")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.40	59.13	778.76	4.82	3.94	647.197972458	204	1.7")
			FractionalPeaks.write("	")
	if shock == 13:
		if tiedosto == 1:
			ResultsSimplified.write("1.85	67.14	439.81	2.46	1.67	443.662475724	45	2.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.85	67.14	439.81	2.46	1.67	443.662475724	45	2.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.85	67.14	439.81	2.46	1.67	443.662475724	45	2.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.85	67.14	439.81	2.46	1.67	443.662475724	45	2.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.85	67.14	439.81	2.46	1.67	443.662475724	45	2.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.85	67.14	439.81	2.46	1.67	443.662475724	45	2.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.85	67.14	439.81	2.46	1.67	443.662475724	45	2.3")
			FractionalPeaks.write("	")
	if shock == 14:
	#???
		if tiedosto == 1:
			ResultsSimplified.write("1.57	30.04	438.75	2.16	1.85	0.00	56	0.7")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.57	30.04	438.75	2.16	1.85	0.00	56	0.7")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.57	30.04	438.75	2.16	1.85	0.00	56	0.7")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.57	30.04	438.75	2.16	1.85	0.00	56	0.7")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.57	30.04	438.75	2.16	1.85	0.00	56	0.7")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.57	30.04	438.75	2.16	1.85	0.00	56	0.7")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.57	30.04	438.75	2.16	1.85	0.00	56	0.7")
			FractionalPeaks.write("	")
	if shock == 15:
		if tiedosto == 1:
			ResultsSimplified.write("3.33	88.21	639.68	3.75	3.17	558.284738113	161	0.8")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("3.33	88.21	639.68	3.75	3.17	558.284738113	161	0.8")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("3.33	88.21	639.68	3.75	3.17	558.284738113	161	0.8")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("3.33	88.21	639.68	3.75	3.17	558.284738113	161	0.8")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("3.33	88.21	639.68	3.75	3.17	558.284738113	161	0.8")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("3.33	88.21	639.68	3.75	3.17	558.284738113	161	0.8")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("3.33	88.21	639.68	3.75	3.17	558.284738113	161	0.8")
			FractionalPeaks.write("	")
	if shock == 16:
		if tiedosto == 1:
			ResultsSimplified.write("1.65	56.58	690.93	2.05	1.60	607.620288993	48	1.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.65	56.58	690.93	2.05	1.60	607.620288993	48	1.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.65	56.58	690.93	2.05	1.60	607.620288993	48	1.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.65	56.58	690.93	2.05	1.60	607.620288993	48	1.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.65	56.58	690.93	2.05	1.60	607.620288993	48	1.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.65	56.58	690.93	2.05	1.60	607.620288993	48	1.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.65	56.58	690.93	2.05	1.60	607.620288993	48	1.3")
			FractionalPeaks.write("	")
	if shock == 17:
		if tiedosto == 1:
			ResultsSimplified.write("2.27	88.76	463.34	2.75	2.30	453.397006389	94	0.9")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.27	88.76	463.34	2.75	2.30	453.397006389	94	0.9")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.27	88.76	463.34	2.75	2.30	453.397006389	94	0.9")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.27	88.76	463.34	2.75	2.30	453.397006389	94	0.9")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.27	88.76	463.34	2.75	2.30	453.397006389	94	0.9")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.27	88.76	463.34	2.75	2.30	453.397006389	94	0.9")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.27	88.76	463.34	2.75	2.30	453.397006389	94	0.9")
			FractionalPeaks.write("	")
	if shock == 18:
		if tiedosto == 1:
			ResultsSimplified.write("2.04	63.68	588.71	2.02	1.93	622.242415399	110	0.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.04	63.68	588.71	2.02	1.93	622.242415399	110	0.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.04	63.68	588.71	2.02	1.93	622.242415399	110	0.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.04	63.68	588.71	2.02	1.93	622.242415399	110	0.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.04	63.68	588.71	2.02	1.93	622.242415399	110	0.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.04	63.68	588.71	2.02	1.93	622.242415399	110	0.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.04	63.68	588.71	2.02	1.93	622.242415399	110	0.2")
			FractionalPeaks.write("	")
	if shock == 19:
		if tiedosto == 1:
			ResultsSimplified.write("1.65	70.32	362.17	1.36	0.98	429.354512168	21	1.8")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.65	70.32	362.17	1.36	0.98	429.354512168	21	1.8")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.65	70.32	362.17	1.36	0.98	429.354512168	21	1.8")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.65	70.32	362.17	1.36	0.98	429.354512168	21	1.8")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.65	70.32	362.17	1.36	0.98	429.354512168	21	1.8")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.65	70.32	362.17	1.36	0.98	429.354512168	21	1.8")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.65	70.32	362.17	1.36	0.98	429.354512168	21	1.8")
			FractionalPeaks.write("	")
	if shock == 20:
		if tiedosto == 1:
			ResultsSimplified.write("1.59	65.76	871.76	5.66	4.86	850.780445224	62	0.8")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.59	65.76	871.76	5.66	4.86	850.780445224	62	0.8")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.59	65.76	871.76	5.66	4.86	850.780445224	62	0.8")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.59	65.76	871.76	5.66	4.86	850.780445224	62	0.8")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.59	65.76	871.76	5.66	4.86	850.780445224	62	0.8")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.59	65.76	871.76	5.66	4.86	850.780445224	62	0.8")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.59	65.76	871.76	5.66	4.86	850.780445224	62	0.8")
			FractionalPeaks.write("	")
	if shock == 21:
		if tiedosto == 1:
			ResultsSimplified.write("1.89	50.05	461.33	2.48	1.76	416.708672157	49	2.0")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.89	50.05	461.33	2.48	1.76	416.708672157	49	2.0")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.89	50.05	461.33	2.48	1.76	416.708672157	49	2.0")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.89	50.05	461.33	2.48	1.76	416.708672157	49	2.0")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.89	50.05	461.33	2.48	1.76	416.708672157	49	2.0")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.89	50.05	461.33	2.48	1.76	416.708672157	49	2.0")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.89	50.05	461.33	2.48	1.76	416.708672157	49	2.0")
			FractionalPeaks.write("	")
	if shock == 22:
		if tiedosto == 1:
			ResultsSimplified.write("2.71	73.89	511.18	3.01	2.54	472.778737358	112	0.8")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.71	73.89	511.18	3.01	2.54	472.778737358	112	0.8")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.71	73.89	511.18	3.01	2.54	472.778737358	112	0.8")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.71	73.89	511.18	3.01	2.54	472.778737358	112	0.8")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.71	73.89	511.18	3.01	2.54	472.778737358	112	0.8")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.71	73.89	511.18	3.01	2.54	472.778737358	112	0.8")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.71	73.89	511.18	3.01	2.54	472.778737358	112	0.8")
			FractionalPeaks.write("	")
	if shock == 23:
		if tiedosto == 1:
			ResultsSimplified.write("2.03	46.07	637.73	2.83	2.43	575.211962776	106	0.7")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.03	46.07	637.73	2.83	2.43	575.211962776	106	0.7")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.03	46.07	637.73	2.83	2.43	575.211962776	106	0.7")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.03	46.07	637.73	2.83	2.43	575.211962776	106	0.7")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.03	46.07	637.73	2.83	2.43	575.211962776	106	0.7")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.03	46.07	637.73	2.83	2.43	575.211962776	106	0.7")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.03	46.07	637.73	2.83	2.43	575.211962776	106	0.7")
			FractionalPeaks.write("	")
	if shock == 24:
		if tiedosto == 1:
			ResultsSimplified.write("2.11	66.67	498.11	1.94	1.62	913.626325585	182	0.9")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.11	66.67	498.11	1.94	1.62	913.626325585	182	0.9")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.11	66.67	498.11	1.94	1.62	913.626325585	182	0.9")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.11	66.67	498.11	1.94	1.62	913.626325585	182	0.9")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.11	66.67	498.11	1.94	1.62	913.626325585	182	0.9")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.11	66.67	498.11	1.94	1.62	913.626325585	182	0.9")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.11	66.67	498.11	1.94	1.62	913.626325585	182	0.9")
			FractionalPeaks.write("	")
	if shock == 25:
		if tiedosto == 1:
			ResultsSimplified.write("2.30	22.09	671.80	5.57	3.58	465.649495608	138	9.1")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.30	22.09	671.80	5.57	3.58	465.649495608	138	9.1")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.30	22.09	671.80	5.57	3.58	465.649495608	138	9.1")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.30	22.09	671.80	5.57	3.58	465.649495608	138	9.1")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.30	22.09	671.80	5.57	3.58	465.649495608	138	9.1")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.30	22.09	671.80	5.57	3.58	465.649495608	138	9.1")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.30	22.09	671.80	5.57	3.58	465.649495608	138	9.1")
			FractionalPeaks.write("	")
	if shock == 26:
		if tiedosto == 1:
			ResultsSimplified.write("2.57	54.17	430.95	2.98	2.32	404.043033243	69	1.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.57	54.17	430.95	2.98	2.32	404.043033243	69	1.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.57	54.17	430.95	2.98	2.32	404.043033243	69	1.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.57	54.17	430.95	2.98	2.32	404.043033243	69	1.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.57	54.17	430.95	2.98	2.32	404.043033243	69	1.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.57	54.17	430.95	2.98	2.32	404.043033243	69	1.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.57	54.17	430.95	2.98	2.32	404.043033243	69	1.3")
			FractionalPeaks.write("	")
	if shock == 27:
		if tiedosto == 1:
			ResultsSimplified.write("2.10	83.54	409.48	2.87	2.15	462.297505675	52	1.6")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.10	83.54	409.48	2.87	2.15	462.297505675	52	1.6")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.10	83.54	409.48	2.87	2.15	462.297505675	52	1.6")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.10	83.54	409.48	2.87	2.15	462.297505675	52	1.6")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.10	83.54	409.48	2.87	2.15	462.297505675	52	1.6")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.10	83.54	409.48	2.87	2.15	462.297505675	52	1.6")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.10	83.54	409.48	2.87	2.15	462.297505675	52	1.6")
			FractionalPeaks.write("	")
	if shock == 28:
		if tiedosto == 1:
			ResultsSimplified.write("1.74	84.00	486.84	1.57	1.42	620.2613637	61	0.4")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.74	84.00	486.84	1.57	1.42	620.2613637	61	0.4")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.74	84.00	486.84	1.57	1.42	620.2613637	61	0.4")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.74	84.00	486.84	1.57	1.42	620.2613637	61	0.4")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.74	84.00	486.84	1.57	1.42	620.2613637	61	0.4")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.74	84.00	486.84	1.57	1.42	620.2613637	61	0.4")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.74	84.00	486.84	1.57	1.42	620.2613637	61	0.4")
			FractionalPeaks.write("	")
	if shock == 29:
		if tiedosto == 1:
			ResultsSimplified.write("1.66	33.07	990.69	8.25	6.90	761.7194714	201	0.9")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.66	33.07	990.69	8.25	6.90	761.7194714	201	0.9")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.66	33.07	990.69	8.25	6.90	761.7194714	201	0.9")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.66	33.07	990.69	8.25	6.90	761.7194714	201	0.9")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.66	33.07	990.69	8.25	6.90	761.7194714	201	0.9")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.66	33.07	990.69	8.25	6.90	761.7194714	201	0.9")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.66	33.07	990.69	8.25	6.90	761.7194714	201	0.9")
			FractionalPeaks.write("	")
	if shock == 30:
		if tiedosto == 1:
			ResultsSimplified.write("1.54	13.12	712.28	2.63	2.12	723.656247867	102	1.1")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.54	13.12	712.28	2.63	2.12	723.656247867	102	1.1")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.54	13.12	712.28	2.63	2.12	723.656247867	102	1.1")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.54	13.12	712.28	2.63	2.12	723.656247867	102	1.1")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.54	13.12	712.28	2.63	2.12	723.656247867	102	1.1")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.54	13.12	712.28	2.63	2.12	723.656247867	102	1.1")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.54	13.12	712.28	2.63	2.12	723.656247867	102	1.1")
			FractionalPeaks.write("	")
	if shock == 31:
		if tiedosto == 1:
			ResultsSimplified.write("2.80	69.97	595.86	5.89	4.33	515.850412794	153	1.7")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.80	69.97	595.86	5.89	4.33	515.850412794	153	1.7")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.80	69.97	595.86	5.89	4.33	515.850412794	153	1.7")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.80	69.97	595.86	5.89	4.33	515.850412794	153	1.7")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.80	69.97	595.86	5.89	4.33	515.850412794	153	1.7")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.80	69.97	595.86	5.89	4.33	515.850412794	153	1.7")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.80	69.97	595.86	5.89	4.33	515.850412794	153	1.7")
			FractionalPeaks.write("	")
	if shock == 32:
		if tiedosto == 1:
			ResultsSimplified.write("1.68	51.99	367.61	2.62	1.55	382.346450557	32	3.7")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.68	51.99	367.61	2.62	1.55	382.346450557	32	3.7")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.68	51.99	367.61	2.62	1.55	382.346450557	32	3.7")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.68	51.99	367.61	2.62	1.55	382.346450557	32	3.7")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.68	51.99	367.61	2.62	1.55	382.346450557	32	3.7")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.68	51.99	367.61	2.62	1.55	382.346450557	32	3.7")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.68	51.99	367.61	2.62	1.55	382.346450557	32	3.7")
			FractionalPeaks.write("	")
	if shock == 33:
		if tiedosto == 1:
			ResultsSimplified.write("1.49	47.50	1678.87	14.69	12.60	679.45531913	296	0.8")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.49	47.50	1678.87	14.69	12.60	679.45531913	296	0.8")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.49	47.50	1678.87	14.69	12.60	679.45531913	296	0.8")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.49	47.50	1678.87	14.69	12.60	679.45531913	296	0.8")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.49	47.50	1678.87	14.69	12.60	679.45531913	296	0.8")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.49	47.50	1678.87	14.69	12.60	679.45531913	296	0.8")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.49	47.50	1678.87	14.69	12.60	679.45531913	296	0.8")
			FractionalPeaks.write("	")
	if shock == 34:
		if tiedosto == 1:
			ResultsSimplified.write("2.13	27.12	629.43	3.16	2.64	554.262751959	128	0.9")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.13	27.12	629.43	3.16	2.64	554.262751959	128	0.9")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.13	27.12	629.43	3.16	2.64	554.262751959	128	0.9")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.13	27.12	629.43	3.16	2.64	554.262751959	128	0.9")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.13	27.12	629.43	3.16	2.64	554.262751959	128	0.9")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.13	27.12	629.43	3.16	2.64	554.262751959	128	0.9")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.13	27.12	629.43	3.16	2.64	554.262751959	128	0.9")
			FractionalPeaks.write("	")
	if shock == 35:
		if tiedosto == 1:
			ResultsSimplified.write("3.61	76.17	546.67	4.27	3.32	530.348037451	136	1.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("3.61	76.17	546.67	4.27	3.32	530.348037451	136	1.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("3.61	76.17	546.67	4.27	3.32	530.348037451	136	1.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("3.61	76.17	546.67	4.27	3.32	530.348037451	136	1.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("3.61	76.17	546.67	4.27	3.32	530.348037451	136	1.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("3.61	76.17	546.67	4.27	3.32	530.348037451	136	1.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("3.61	76.17	546.67	4.27	3.32	530.348037451	136	1.3")
			FractionalPeaks.write("	")
	if shock == 36:
		if tiedosto == 1:
			ResultsSimplified.write("2.59	75.48	604.73	3.99	3.13	545.359877194	119	1.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.59	75.48	604.73	3.99	3.13	545.359877194	119	1.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.59	75.48	604.73	3.99	3.13	545.359877194	119	1.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.59	75.48	604.73	3.99	3.13	545.359877194	119	1.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.59	75.48	604.73	3.99	3.13	545.359877194	119	1.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("3.61	76.17	546.67	4.27	3.32	530.348037451	136	1.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("3.61	76.17	546.67	4.27	3.32	530.348037451	136	1.3")
			FractionalPeaks.write("	")
	if shock == 37:
		if tiedosto == 1:
			ResultsSimplified.write("1.65	81.87	573.29	5.23	4.75	649.056203844	327	0.4")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.65	81.87	573.29	5.23	4.75	649.056203844	327	0.4")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.65	81.87	573.29	5.23	4.75	649.056203844	327	0.4")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.65	81.87	573.29	5.23	4.75	649.056203844	327	0.4")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.65	81.87	573.29	5.23	4.75	649.056203844	327	0.4")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.65	81.87	573.29	5.23	4.75	649.056203844	327	0.4")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.65	81.87	573.29	5.23	4.75	649.056203844	327	0.4")
			FractionalPeaks.write("	")
	if shock == 38:
		if tiedosto == 1:
			ResultsSimplified.write("2.25	36.70	718.55	3.47	2.39	703.446862403	113	2.4")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.25	36.70	718.55	3.47	2.39	703.446862403	113	2.4")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.25	36.70	718.55	3.47	2.39	703.446862403	113	2.4")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.25	36.70	718.55	3.47	2.39	703.446862403	113	2.4")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.25	36.70	718.55	3.47	2.39	703.446862403	113	2.4")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.25	36.70	718.55	3.47	2.39	703.446862403	113	2.4")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.25	36.70	718.55	3.47	2.39	703.446862403	113	2.4")
			FractionalPeaks.write("	")
	if shock == 39:
		if tiedosto == 1:
			ResultsSimplified.write("2.35	59.45	587.38	2.50	2.35	434.81717107	167	0.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.35	59.45	587.38	2.50	2.35	434.81717107	167	0.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.35	59.45	587.38	2.50	2.35	434.81717107	167	0.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.35	59.45	587.38	2.50	2.35	434.81717107	167	0.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.35	59.45	587.38	2.50	2.35	434.81717107	167	0.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.35	59.45	587.38	2.50	2.35	434.81717107	167	0.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.35	59.45	587.38	2.50	2.35	434.81717107	167	0.3")
			FractionalPeaks.write("	")
	if shock == 40:
		if tiedosto == 1:
			ResultsSimplified.write("1.53	14.29	415.04	2.69	2.10	364.691727447	70	1.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.53	14.29	415.04	2.69	2.10	364.691727447	70	1.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.53	14.29	415.04	2.69	2.10	364.691727447	70	1.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.53	14.29	415.04	2.69	2.10	364.691727447	70	1.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.53	14.29	415.04	2.69	2.10	364.691727447	70	1.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.53	14.29	415.04	2.69	2.10	364.691727447	70	1.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.53	14.29	415.04	2.69	2.10	364.691727447	70	1.3")
			FractionalPeaks.write("	")
	if shock == 41:
		if tiedosto == 1:
			ResultsSimplified.write("5.20	80.88	1030.62	5.99	4.15	1462.45275278	314	2.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("5.20	80.88	1030.62	5.99	4.15	1462.45275278	314	2.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("5.20	80.88	1030.62	5.99	4.15	1462.45275278	314	2.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("5.20	80.88	1030.62	5.99	4.15	1462.45275278	314	2.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("5.20	80.88	1030.62	5.99	4.15	1462.45275278	314	2.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("5.20	80.88	1030.62	5.99	4.15	1462.45275278	314	2.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("5.20	80.88	1030.62	5.99	4.15	1462.45275278	314	2.2")
			FractionalPeaks.write("	")
	if shock == 42:
		if tiedosto == 1:
			ResultsSimplified.write("1.69	46.52	345.86	1.86	1.42	397.017350634	49	1.4")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.69	46.52	345.86	1.86	1.42	397.017350634	49	1.4")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.69	46.52	345.86	1.86	1.42	397.017350634	49	1.4")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.69	46.52	345.86	1.86	1.42	397.017350634	49	1.4")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.69	46.52	345.86	1.86	1.42	397.017350634	49	1.4")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.69	46.52	345.86	1.86	1.42	397.017350634	49	1.4")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.69	46.52	345.86	1.86	1.42	397.017350634	49	1.4")
			FractionalPeaks.write("	")
	if shock == 43:
		if tiedosto == 1:
			ResultsSimplified.write("2.89	38.91	517.39	6.82	4.10	419.32678687	157	3.7")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.89	38.91	517.39	6.82	4.10	419.32678687	157	3.7")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.89	38.91	517.39	6.82	4.10	419.32678687	157	3.7")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.89	38.91	517.39	6.82	4.10	419.32678687	157	3.7")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.89	38.91	517.39	6.82	4.10	419.32678687	157	3.7")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.89	38.91	517.39	6.82	4.10	419.32678687	157	3.7")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.89	38.91	517.39	6.82	4.10	419.32678687	157	3.7")
			FractionalPeaks.write("	")
	if shock == 44:
		if tiedosto == 1:
			ResultsSimplified.write("2.58	74.02	532.56	3.25	2.49	439.986330025	82	1.4")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.58	74.02	532.56	3.25	2.49	439.986330025	82	1.4")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.58	74.02	532.56	3.25	2.49	439.986330025	82	1.4")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.58	74.02	532.56	3.25	2.49	439.986330025	82	1.4")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.58	74.02	532.56	3.25	2.49	439.986330025	82	1.4")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.58	74.02	532.56	3.25	2.49	439.986330025	82	1.4")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.58	74.02	532.56	3.25	2.49	439.986330025	82	1.4")
			FractionalPeaks.write("	")
	if shock == 45:
		if tiedosto == 1:
			ResultsSimplified.write("2.31	36.41	452.53	2.64	2.02	466.547834363	87	1.4")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.31	36.41	452.53	2.64	2.02	466.547834363	87	1.4")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.31	36.41	452.53	2.64	2.02	466.547834363	87	1.4")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.31	36.41	452.53	2.64	2.02	466.547834363	87	1.4")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.31	36.41	452.53	2.64	2.02	466.547834363	87	1.4")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.31	36.41	452.53	2.64	2.02	466.547834363	87	1.4")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.31	36.41	452.53	2.64	2.02	466.547834363	87	1.4")
			FractionalPeaks.write("	")
	if shock == 46:
		if tiedosto == 1:
			ResultsSimplified.write("2.95	33.63	537.44	6.05	4.19	473.652537552	155	2.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.95	33.63	537.44	6.05	4.19	473.652537552	155	2.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.95	33.63	537.44	6.05	4.19	473.652537552	155	2.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.95	33.63	537.44	6.05	4.19	473.652537552	155	2.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.95	33.63	537.44	6.05	4.19	473.652537552	155	2.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.95	33.63	537.44	6.05	4.19	473.652537552	155	2.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.95	33.63	537.44	6.05	4.19	473.652537552	155	2.2")
			FractionalPeaks.write("	")
	if shock == 47:
		if tiedosto == 1:
			ResultsSimplified.write("1.55	6.98	443.39	1.65	1.57	464.722135275	87	0.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.55	6.98	443.39	1.65	1.57	464.722135275	87	0.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.55	6.98	443.39	1.65	1.57	464.722135275	87	0.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.55	6.98	443.39	1.65	1.57	464.722135275	87	0.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.55	6.98	443.39	1.65	1.57	464.722135275	87	0.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.55	6.98	443.39	1.65	1.57	464.722135275	87	0.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.55	6.98	443.39	1.65	1.57	464.722135275	87	0.2")
			FractionalPeaks.write("	")
	if shock == 48:
		if tiedosto == 1:
			ResultsSimplified.write("3.68	38.67	630.23	7.81	4.44	489.964572712	162	4.5")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("3.68	38.67	630.23	7.81	4.44	489.964572712	162	4.5")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("3.68	38.67	630.23	7.81	4.44	489.964572712	162	4.5")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("3.68	38.67	630.23	7.81	4.44	489.964572712	162	4.5")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("3.68	38.67	630.23	7.81	4.44	489.964572712	162	4.5")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("3.68	38.67	630.23	7.81	4.44	489.964572712	162	4.5")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("3.68	38.67	630.23	7.81	4.44	489.964572712	162	4.5")
			FractionalPeaks.write("	")
	if shock == 49:
		if tiedosto == 1:
			ResultsSimplified.write("2.86	86.69	709.20	3.69	3.48	475.913374096	199	0.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.86	86.69	709.20	3.69	3.48	475.913374096	199	0.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.86	86.69	709.20	3.69	3.48	475.913374096	199	0.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.86	86.69	709.20	3.69	3.48	475.913374096	199	0.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.86	86.69	709.20	3.69	3.48	475.913374096	199	0.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.86	86.69	709.20	3.69	3.48	475.913374096	199	0.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.86	86.69	709.20	3.69	3.48	475.913374096	199	0.3")
			FractionalPeaks.write("	")
	if shock == 50:
		if tiedosto == 1:
			ResultsSimplified.write("1.63	71.79	345.39	1.43	1.21	360.162363065	42	0.8")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.63	71.79	345.39	1.43	1.21	360.162363065	42	0.8")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.63	71.79	345.39	1.43	1.21	360.162363065	42	0.8")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.63	71.79	345.39	1.43	1.21	360.162363065	42	0.8")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.63	71.79	345.39	1.43	1.21	360.162363065	42	0.8")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.63	71.79	345.39	1.43	1.21	360.162363065	42	0.8")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.63	71.79	345.39	1.43	1.21	360.162363065	42	0.8")
			FractionalPeaks.write("	")
	if shock == 51:
		if tiedosto == 1:
			ResultsSimplified.write("1.54	21.52	500.73	2.67	2.10	473.476948382	43	1.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.54	21.52	500.73	2.67	2.10	473.476948382	43	1.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.54	21.52	500.73	2.67	2.10	473.476948382	43	1.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.54	21.52	500.73	2.67	2.10	473.476948382	43	1.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.54	21.52	500.73	2.67	2.10	473.476948382	43	1.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.54	21.52	500.73	2.67	2.10	473.476948382	43	1.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.54	21.52	500.73	2.67	2.10	473.476948382	43	1.2")
			FractionalPeaks.write("	")
	if shock == 52:
		if tiedosto == 1:
			ResultsSimplified.write("2.75	69.44	603.43	2.71	2.40	557.384851801	133	0.6")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.75	69.44	603.43	2.71	2.40	557.384851801	133	0.6")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.75	69.44	603.43	2.71	2.40	557.384851801	133	0.6")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.75	69.44	603.43	2.71	2.40	557.384851801	133	0.6")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.75	69.44	603.43	2.71	2.40	557.384851801	133	0.6")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.75	69.44	603.43	2.71	2.40	557.384851801	133	0.6")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.75	69.44	603.43	2.71	2.40	557.384851801	133	0.6")
			FractionalPeaks.write("	")
	if shock == 53:
		if tiedosto == 1:
			ResultsSimplified.write("1.59	40.13	692.00	1.94	1.84	740.901144069	116	0.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.59	40.13	692.00	1.94	1.84	740.901144069	116	0.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.59	40.13	692.00	1.94	1.84	740.901144069	116	0.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.59	40.13	692.00	1.94	1.84	740.901144069	116	0.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.59	40.13	692.00	1.94	1.84	740.901144069	116	0.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.59	40.13	692.00	1.94	1.84	740.901144069	116	0.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.59	40.13	692.00	1.94	1.84	740.901144069	116	0.2")
			FractionalPeaks.write("	")
	if shock == 54:
		if tiedosto == 1:
			ResultsSimplified.write("2.22	58.49	914.42	2.48	2.31	655.082895237	119	0.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.22	58.49	914.42	2.48	2.31	655.082895237	119	0.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.22	58.49	914.42	2.48	2.31	655.082895237	119	0.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.22	58.49	914.42	2.48	2.31	655.082895237	119	0.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.22	58.49	914.42	2.48	2.31	655.082895237	119	0.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.22	58.49	914.42	2.48	2.31	655.082895237	119	0.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.22	58.49	914.42	2.48	2.31	655.082895237	119	0.3")
			FractionalPeaks.write("	")
	if shock == 55:
		if tiedosto == 1:
			ResultsSimplified.write("2.37	17.42	465.77	3.62	2.87	491.552331794	100	1.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.37	17.42	465.77	3.62	2.87	491.552331794	100	1.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.37	17.42	465.77	3.62	2.87	491.552331794	100	1.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.37	17.42	465.77	3.62	2.87	491.552331794	100	1.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.37	17.42	465.77	3.62	2.87	491.552331794	100	1.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.37	17.42	465.77	3.62	2.87	491.552331794	100	1.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.37	17.42	465.77	3.62	2.87	491.552331794	100	1.2")
			FractionalPeaks.write("	")
	if shock == 56:
		if tiedosto == 1:
			ResultsSimplified.write("2.36	27.71	492.28	3.59	2.49	598.352760058	60	2.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.36	27.71	492.28	3.59	2.49	598.352760058	60	2.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.36	27.71	492.28	3.59	2.49	598.352760058	60	2.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.36	27.71	492.28	3.59	2.49	598.352760058	60	2.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.36	27.71	492.28	3.59	2.49	598.352760058	60	2.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.36	27.71	492.28	3.59	2.49	598.352760058	60	2.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.36	27.71	492.28	3.59	2.49	598.352760058	60	2.2")
			FractionalPeaks.write("	")
	if shock == 57:
		if tiedosto == 1:
			ResultsSimplified.write("4.08	63.87	1117.83	7.61	5.97	1779.33764819	361	1.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("4.08	63.87	1117.83	7.61	5.97	1779.33764819	361	1.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("4.08	63.87	1117.83	7.61	5.97	1779.33764819	361	1.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("4.08	63.87	1117.83	7.61	5.97	1779.33764819	361	1.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("4.08	63.87	1117.83	7.61	5.97	1779.33764819	361	1.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("4.08	63.87	1117.83	7.61	5.97	1779.33764819	361	1.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("4.08	63.87	1117.83	7.61	5.97	1779.33764819	361	1.3")
			FractionalPeaks.write("	")
	if shock == 58:
		if tiedosto == 1:
			ResultsSimplified.write("1.69	52.39	452.97	1.95	1.42	410.028123493	39	1.8")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.69	52.39	452.97	1.95	1.42	410.028123493	39	1.8")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.69	52.39	452.97	1.95	1.42	410.028123493	39	1.8")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.69	52.39	452.97	1.95	1.42	410.028123493	39	1.8")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.69	52.39	452.97	1.95	1.42	410.028123493	39	1.8")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.69	52.39	452.97	1.95	1.42	410.028123493	39	1.8")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.69	52.39	452.97	1.95	1.42	410.028123493	39	1.8")
			FractionalPeaks.write("	")
	if shock == 59:
		if tiedosto == 1:
			ResultsSimplified.write("2.25	50.69	733.40	3.18	2.55	646.746121767	170	1.1")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.25	50.69	733.40	3.18	2.55	646.746121767	170	1.1")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.25	50.69	733.40	3.18	2.55	646.746121767	170	1.1")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.25	50.69	733.40	3.18	2.55	646.746121767	170	1.1")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.25	50.69	733.40	3.18	2.55	646.746121767	170	1.1")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.25	50.69	733.40	3.18	2.55	646.746121767	170	1.1")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.25	50.69	733.40	3.18	2.55	646.746121767	170	1.1")
			FractionalPeaks.write("	")
	if shock == 60:
		if tiedosto == 1:
			ResultsSimplified.write("2.22	1.25	807.97	4.01	2.60	817.681558269	145	2.8")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.22	1.25	807.97	4.01	2.60	817.681558269	145	2.8")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.22	1.25	807.97	4.01	2.60	817.681558269	145	2.8")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.22	1.25	807.97	4.01	2.60	817.681558269	145	2.8")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.22	1.25	807.97	4.01	2.60	817.681558269	145	2.8")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.22	1.25	807.97	4.01	2.60	817.681558269	145	2.8")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.22	1.25	807.97	4.01	2.60	817.681558269	145	2.8")
			FractionalPeaks.write("	")
	if shock == 61:
		if tiedosto == 1:
			ResultsSimplified.write("5.58	62.23	847.68	6.89	5.32	946.451755456	296	1.4")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("5.58	62.23	847.68	6.89	5.32	946.451755456	296	1.4")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("5.58	62.23	847.68	6.89	5.32	946.451755456	296	1.4")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("5.58	62.23	847.68	6.89	5.32	946.451755456	296	1.4")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("5.58	62.23	847.68	6.89	5.32	946.451755456	296	1.4")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("5.58	62.23	847.68	6.89	5.32	946.451755456	296	1.4")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("5.58	62.23	847.68	6.89	5.32	946.451755456	296	1.4")
			FractionalPeaks.write("	")
	if shock == 62:
		if tiedosto == 1:
			ResultsSimplified.write("4.38	69.37	319.26	10.50	2.19	509.303348444	38	71.6")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("4.38	69.37	319.26	10.50	2.19	509.303348444	38	71.6")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("4.38	69.37	319.26	10.50	2.19	509.303348444	38	71.6")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("4.38	69.37	319.26	10.50	2.19	509.303348444	38	71.6")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("4.38	69.37	319.26	10.50	2.19	509.303348444	38	71.6")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("4.38	69.37	319.26	10.50	2.19	509.303348444	38	71.6")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("4.38	69.37	319.26	10.50	2.19	509.303348444	38	71.6")
			FractionalPeaks.write("	")
	if shock == 63:
		if tiedosto == 1:
			ResultsSimplified.write("3.56	71.21	555.06	6.17	3.32	509.823059613	77	4.9")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("3.56	71.21	555.06	6.17	3.32	509.823059613	77	4.9")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("3.56	71.21	555.06	6.17	3.32	509.823059613	77	4.9")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("3.56	71.21	555.06	6.17	3.32	509.823059613	77	4.9")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("3.56	71.21	555.06	6.17	3.32	509.823059613	77	4.9")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("3.56	71.21	555.06	6.17	3.32	509.823059613	77	4.9")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("3.56	71.21	555.06	6.17	3.32	509.823059613	77	4.9")
			FractionalPeaks.write("	")
	if shock == 64:
		if tiedosto == 1:
			ResultsSimplified.write("1.79	79.26	483.10	1.74	1.56	461.360733617	66	0.5")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.79	79.26	483.10	1.74	1.56	461.360733617	66	0.5")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.79	79.26	483.10	1.74	1.56	461.360733617	66	0.5")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.79	79.26	483.10	1.74	1.56	461.360733617	66	0.5")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.79	79.26	483.10	1.74	1.56	461.360733617	66	0.5")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.79	79.26	483.10	1.74	1.56	461.360733617	66	0.5")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.79	79.26	483.10	1.74	1.56	461.360733617	66	0.5")
			FractionalPeaks.write("	")
	if shock == 65:
		if tiedosto == 1:
			ResultsSimplified.write("1.69	65.26	345.11	2.52	1.73	449.029820234	23	2.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.69	65.26	345.11	2.52	1.73	449.029820234	23	2.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.69	65.26	345.11	2.52	1.73	449.029820234	23	2.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.69	65.26	345.11	2.52	1.73	449.029820234	23	2.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.69	65.26	345.11	2.52	1.73	449.029820234	23	2.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.69	65.26	345.11	2.52	1.73	449.029820234	23	2.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.69	65.26	345.11	2.52	1.73	449.029820234	23	2.3")
			FractionalPeaks.write("	")
	if shock == 66:
		if tiedosto == 1:
			ResultsSimplified.write("2.02	56.39	566.58	2.77	2.19	641.279292864	87	1.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.02	56.39	566.58	2.77	2.19	641.279292864	87	1.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.02	56.39	566.58	2.77	2.19	641.279292864	87	1.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.02	56.39	566.58	2.77	2.19	641.279292864	87	1.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.02	56.39	566.58	2.77	2.19	641.279292864	87	1.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.02	56.39	566.58	2.77	2.19	641.279292864	87	1.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.02	56.39	566.58	2.77	2.19	641.279292864	87	1.2")
			FractionalPeaks.write("	")
	if shock == 67:
		if tiedosto == 1:
			ResultsSimplified.write("1.96	79.11	475.15	2.91	1.79	531.573172315	36	3.7")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.96	79.11	475.15	2.91	1.79	531.573172315	36	3.7")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.96	79.11	475.15	2.91	1.79	531.573172315	36	3.7")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.96	79.11	475.15	2.91	1.79	531.573172315	36	3.7")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.96	79.11	475.15	2.91	1.79	531.573172315	36	3.7")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.96	79.11	475.15	2.91	1.79	531.573172315	36	3.7")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.96	79.11	475.15	2.91	1.79	531.573172315	36	3.7")
			FractionalPeaks.write("	")
	if shock == 68:
		if tiedosto == 1:
			ResultsSimplified.write("1.72	51.82	825.61	4.12	3.14	611.252353446	105	1.5")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.72	51.82	825.61	4.12	3.14	611.252353446	105	1.5")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.72	51.82	825.61	4.12	3.14	611.252353446	105	1.5")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.72	51.82	825.61	4.12	3.14	611.252353446	105	1.5")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.72	51.82	825.61	4.12	3.14	611.252353446	105	1.5")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.72	51.82	825.61	4.12	3.14	611.252353446	105	1.5")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.72	51.82	825.61	4.12	3.14	611.252353446	105	1.5")
			FractionalPeaks.write("	")
	if shock == 69:
		if tiedosto == 1:
			ResultsSimplified.write("3.49	33.09	918.67	6.76	5.47	860.857482495	304	1.1")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("3.49	33.09	918.67	6.76	5.47	860.857482495	304	1.1")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("3.49	33.09	918.67	6.76	5.47	860.857482495	304	1.1")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("3.49	33.09	918.67	6.76	5.47	860.857482495	304	1.1")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("3.49	33.09	918.67	6.76	5.47	860.857482495	304	1.1")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("3.49	33.09	918.67	6.76	5.47	860.857482495	304	1.1")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("3.49	33.09	918.67	6.76	5.47	860.857482495	304	1.1")
			FractionalPeaks.write("	")
	if shock == 70:
		if tiedosto == 1:
			ResultsSimplified.write("1.81	36.62	443.76	2.53	1.56	463.058953837	34	3.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.81	36.62	443.76	2.53	1.56	463.058953837	34	3.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.81	36.62	443.76	2.53	1.56	463.058953837	34	3.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.81	36.62	443.76	2.53	1.56	463.058953837	34	3.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.81	36.62	443.76	2.53	1.56	463.058953837	34	3.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.81	36.62	443.76	2.53	1.56	463.058953837	34	3.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.81	36.62	443.76	2.53	1.56	463.058953837	34	3.2")
			FractionalPeaks.write("	")
	if shock == 71:
		if tiedosto == 1:
			ResultsSimplified.write("1.59	73.79	375.61	1.48	1.23	373.187240904	42	0.9")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.59	73.79	375.61	1.48	1.23	373.187240904	42	0.9")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.59	73.79	375.61	1.48	1.23	373.187240904	42	0.9")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.59	73.79	375.61	1.48	1.23	373.187240904	42	0.9")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.59	73.79	375.61	1.48	1.23	373.187240904	42	0.9")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.59	73.79	375.61	1.48	1.23	373.187240904	42	0.9")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.59	73.79	375.61	1.48	1.23	373.187240904	42	0.9")
			FractionalPeaks.write("	")
	if shock == 72:
	#Ei loydy ipshocks eika harvard. cdaweb nakyy kylla shokki
		if tiedosto == 1:
			ResultsSimplified.write("0.00	00.00	000.00	0.00	0.00	288.589889313	0.00	0.00")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("0.00	00.00	000.00	0.00	0.00	288.589889313	0.00	0.00")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("0.00	00.00	000.00	0.00	0.00	288.589889313	0.00	0.00")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("0.00	00.00	000.00	0.00	0.00	288.589889313	0.00	0.00")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("0.00	00.00	000.00	0.00	0.00	288.589889313	0.00	0.00")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("0.00	00.00	000.00	0.00	0.00	288.589889313	0.00	0.00")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("0.00	00.00	000.00	0.00	0.00	288.589889313	0.00	0.00")
			FractionalPeaks.write("	")
	if shock == 73:
		if tiedosto == 1:
			ResultsSimplified.write("2.38	54.05	838.21	3.69	2.94	787.694938498	150	1.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.38	54.05	838.21	3.69	2.94	787.694938498	150	1.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.38	54.05	838.21	3.69	2.94	787.694938498	150	1.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.38	54.05	838.21	3.69	2.94	787.694938498	150	1.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.38	54.05	838.21	3.69	2.94	787.694938498	150	1.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.38	54.05	838.21	3.69	2.94	787.694938498	150	1.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.38	54.05	838.21	3.69	2.94	787.694938498	150	1.2")
			FractionalPeaks.write("	")
	if shock == 74:
		if tiedosto == 1:
			ResultsSimplified.write("1.44	27.75	297.26	2.36	1.41	369.675664555	44	3.6")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.44	27.75	297.26	2.36	1.41	369.675664555	44	3.6")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.44	27.75	297.26	2.36	1.41	369.675664555	44	3.6")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.44	27.75	297.26	2.36	1.41	369.675664555	44	3.6")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.44	27.75	297.26	2.36	1.41	369.675664555	44	3.6")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.44	27.75	297.26	2.36	1.41	369.675664555	44	3.6")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.44	27.75	297.26	2.36	1.41	369.675664555	44	3.6")
			FractionalPeaks.write("	")
	if shock == 75:
		if tiedosto == 1:
			ResultsSimplified.write("1.79	76.63	394.94	2.20	1.77	369.22579465	47	1.1")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.79	76.63	394.94	2.20	1.77	369.22579465	47	1.1")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.79	76.63	394.94	2.20	1.77	369.22579465	47	1.1")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.79	76.63	394.94	2.20	1.77	369.22579465	47	1.1")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.79	76.63	394.94	2.20	1.77	369.22579465	47	1.1")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.79	76.63	394.94	2.20	1.77	369.22579465	47	1.1")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.79	76.63	394.94	2.20	1.77	369.22579465	47	1.1")
			FractionalPeaks.write("	")
	if shock == 76:
		if tiedosto == 1:
			ResultsSimplified.write("2.42	86.77	509.38	3.22	2.50	458.280039489	80	1.4")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.42	86.77	509.38	3.22	2.50	458.280039489	80	1.4")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.42	86.77	509.38	3.22	2.50	458.280039489	80	1.4")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.42	86.77	509.38	3.22	2.50	458.280039489	80	1.4")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.42	86.77	509.38	3.22	2.50	458.280039489	80	1.4")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.42	86.77	509.38	3.22	2.50	458.280039489	80	1.4")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.42	86.77	509.38	3.22	2.50	458.280039489	80	1.4")
			FractionalPeaks.write("	")
	if shock == 77:
		if tiedosto == 1:
			ResultsSimplified.write("2.35	46.89	543.83	3.53	2.67	681.940558626	115	1.5")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.35	46.89	543.83	3.53	2.67	681.940558626	115	1.5")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.35	46.89	543.83	3.53	2.67	681.940558626	115	1.5")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.35	46.89	543.83	3.53	2.67	681.940558626	115	1.5")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.35	46.89	543.83	3.53	2.67	681.940558626	115	1.5")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.35	46.89	543.83	3.53	2.67	681.940558626	115	1.5")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.35	46.89	543.83	3.53	2.67	681.940558626	115	1.5")
			FractionalPeaks.write("	")
	if shock == 78:
		if tiedosto == 1:
			ResultsSimplified.write("2.45	67.35	415.86	3.86	2.05	384.30214537	56	5.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.45	67.35	415.86	3.86	2.05	384.30214537	56	5.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.45	67.35	415.86	3.86	2.05	384.30214537	56	5.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.45	67.35	415.86	3.86	2.05	384.30214537	56	5.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.45	67.35	415.86	3.86	2.05	384.30214537	56	5.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.45	67.35	415.86	3.86	2.05	384.30214537	56	5.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.45	67.35	415.86	3.86	2.05	384.30214537	56	5.3")
			FractionalPeaks.write("	")
	if shock == 79:
		if tiedosto == 1:
			ResultsSimplified.write("1.87	60.44	486.30	2.62	1.88	512.099620661	49	1.9")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.87	60.44	486.30	2.62	1.88	512.099620661	49	1.9")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.87	60.44	486.30	2.62	1.88	512.099620661	49	1.9")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.87	60.44	486.30	2.62	1.88	512.099620661	49	1.9")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.87	60.44	486.30	2.62	1.88	512.099620661	49	1.9")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.87	60.44	486.30	2.62	1.88	512.099620661	49	1.9")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.87	60.44	486.30	2.62	1.88	512.099620661	49	1.9")
			FractionalPeaks.write("	")
	if shock == 80:
		if tiedosto == 1:
			ResultsSimplified.write("2.08	33.24	616.51	4.08	3.56	613.465248579	197	0.6")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.08	33.24	616.51	4.08	3.56	613.465248579	197	0.6")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.08	33.24	616.51	4.08	3.56	613.465248579	197	0.6")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.08	33.24	616.51	4.08	3.56	613.465248579	197	0.6")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.08	33.24	616.51	4.08	3.56	613.465248579	197	0.6")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.08	33.24	616.51	4.08	3.56	613.465248579	197	0.6")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.08	33.24	616.51	4.08	3.56	613.465248579	197	0.6")
			FractionalPeaks.write("	")
	if shock == 81:
		if tiedosto == 1:
			ResultsSimplified.write("1.96	74.46	444.97	2.25	1.89	393.683429351	67	0.8")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.96	74.46	444.97	2.25	1.89	393.683429351	67	0.8")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.96	74.46	444.97	2.25	1.89	393.683429351	67	0.8")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.96	74.46	444.97	2.25	1.89	393.683429351	67	0.8")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.96	74.46	444.97	2.25	1.89	393.683429351	67	0.8")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.96	74.46	444.97	2.25	1.89	393.683429351	67	0.8")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.96	74.46	444.97	2.25	1.89	393.683429351	67	0.8")
			FractionalPeaks.write("	")
	if shock == 82:
		if tiedosto == 1:
			ResultsSimplified.write("1.31	40.16	498.68	1.65	1.31	509.155806935	25	1.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.31	40.16	498.68	1.65	1.31	509.155806935	25	1.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.31	40.16	498.68	1.65	1.31	509.155806935	25	1.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.31	40.16	498.68	1.65	1.31	509.155806935	25	1.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.31	40.16	498.68	1.65	1.31	509.155806935	25	1.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.31	40.16	498.68	1.65	1.31	509.155806935	25	1.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.31	40.16	498.68	1.65	1.31	509.155806935	25	1.2")
			FractionalPeaks.write("	")
	if shock == 83:
		if tiedosto == 1:
			ResultsSimplified.write("2.37	86.26	391.21	4.20	2.21	364.713949628	58	5.2")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.37	86.26	391.21	4.20	2.21	364.713949628	58	5.2")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.37	86.26	391.21	4.20	2.21	364.713949628	58	5.2")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.37	86.26	391.21	4.20	2.21	364.713949628	58	5.2")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.37	86.26	391.21	4.20	2.21	364.713949628	58	5.2")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.37	86.26	391.21	4.20	2.21	364.713949628	58	5.2")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.37	86.26	391.21	4.20	2.21	364.713949628	58	5.2")
			FractionalPeaks.write("	")
	if shock == 84:
		if tiedosto == 1:
			ResultsSimplified.write("2.81	76.37	375.92	4.00	2.87	404.091854105	73	1.9")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.81	76.37	375.92	4.00	2.87	404.091854105	73	1.9")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.81	76.37	375.92	4.00	2.87	404.091854105	73	1.9")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.81	76.37	375.92	4.00	2.87	404.091854105	73	1.9")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.81	76.37	375.92	4.00	2.87	404.091854105	73	1.9")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.81	76.37	375.92	4.00	2.87	404.091854105	73	1.9")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.81	76.37	375.92	4.00	2.87	404.091854105	73	1.9")
			FractionalPeaks.write("	")
	if shock == 85:
		if tiedosto == 1:
			ResultsSimplified.write("2.45	39.06	719.02	6.13	4.66	686.288159876	199	1.5")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.45	39.06	719.02	6.13	4.66	686.288159876	199	1.5")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.45	39.06	719.02	6.13	4.66	686.288159876	199	1.5")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.45	39.06	719.02	6.13	4.66	686.288159876	199	1.5")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.45	39.06	719.02	6.13	4.66	686.288159876	199	1.5")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.45	39.06	719.02	6.13	4.66	686.288159876	199	1.5")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.45	39.06	719.02	6.13	4.66	686.288159876	199	1.5")
			FractionalPeaks.write("	")
	if shock == 86:
		if tiedosto == 1:
			ResultsSimplified.write("2.61	40.30	478.94	4.66	3.46	459.62464221	106	1.7")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.61	40.30	478.94	4.66	3.46	459.62464221	106	1.7")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.61	40.30	478.94	4.66	3.46	459.62464221	106	1.7")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.61	40.30	478.94	4.66	3.46	459.62464221	106	1.7")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.61	40.30	478.94	4.66	3.46	459.62464221	106	1.7")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.61	40.30	478.94	4.66	3.46	459.62464221	106	1.7")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.61	40.30	478.94	4.66	3.46	459.62464221	106	1.7")
			FractionalPeaks.write("	")
	if shock == 87:
		if tiedosto == 1:
			ResultsSimplified.write("1.99	78.57	493.04	3.52	2.85	465.650316489	47	1.1")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.99	78.57	493.04	3.52	2.85	465.650316489	47	1.1")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.99	78.57	493.04	3.52	2.85	465.650316489	47	1.1")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.99	78.57	493.04	3.52	2.85	465.650316489	47	1.1")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.99	78.57	493.04	3.52	2.85	465.650316489	47	1.1")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.99	78.57	493.04	3.52	2.85	465.650316489	47	1.1")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.99	78.57	493.04	3.52	2.85	465.650316489	47	1.1")
			FractionalPeaks.write("	")
	if shock == 88:
		if tiedosto == 1:
			ResultsSimplified.write("2.58	79.12	565.43	1.52	1.35	608.302346582	73	0.5")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.58	79.12	565.43	1.52	1.35	608.302346582	73	0.5")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.58	79.12	565.43	1.52	1.35	608.302346582	73	0.5")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.58	79.12	565.43	1.52	1.35	608.302346582	73	0.5")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.58	79.12	565.43	1.52	1.35	608.302346582	73	0.5")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.58	79.12	565.43	1.52	1.35	608.302346582	73	0.5")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.58	79.12	565.43	1.52	1.35	608.302346582	73	0.5")
			FractionalPeaks.write("	")
	if shock == 89:
		if tiedosto == 1:
			ResultsSimplified.write("1.60	84.73	271.46	1.87	1.28	412.625708347	21	2.3")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("1.60	84.73	271.46	1.87	1.28	412.625708347	21	2.3")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("1.60	84.73	271.46	1.87	1.28	412.625708347	21	2.3")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("1.60	84.73	271.46	1.87	1.28	412.625708347	21	2.3")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("1.60	84.73	271.46	1.87	1.28	412.625708347	21	2.3")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("1.60	84.73	271.46	1.87	1.28	412.625708347	21	2.3")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("1.60	84.73	271.46	1.87	1.28	412.625708347	21	2.3")
			FractionalPeaks.write("	")
	if shock == 90:
		if tiedosto == 1:
			ResultsSimplified.write("3.01	64.28	746.91	4.20	3.79	707.793774148	228	0.5")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("3.01	64.28	746.91	4.20	3.79	707.793774148	228	0.5")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("3.01	64.28	746.91	4.20	3.79	707.793774148	228	0.5")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("3.01	64.28	746.91	4.20	3.79	707.793774148	228	0.5")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("3.01	64.28	746.91	4.20	3.79	707.793774148	228	0.5")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("3.01	64.28	746.91	4.20	3.79	707.793774148	228	0.5")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("3.01	64.28	746.91	4.20	3.79	707.793774148	228	0.5")
			FractionalPeaks.write("	")
	if shock == 91:
		if tiedosto == 1:
			ResultsSimplified.write("2.52	63.12	561.66	3.53	2.87	595.240383136	109	1.0")
			ResultsSimplified.write("	")
		if tiedosto == 2:
			ModesSimplified.write("2.52	63.12	561.66	3.53	2.87	595.240383136	109	1.0")
			ModesSimplified.write("	")
		if tiedosto == 3:
			Fractional.write("2.52	63.12	561.66	3.53	2.87	595.240383136	109	1.0")
			Fractional.write("	")
		if tiedosto == 4:
			SheathFrac.write("2.52	63.12	561.66	3.53	2.87	595.240383136	109	1.0")
			SheathFrac.write("	")
		if tiedosto == 5:
			ThresholdWholeSheath.write("2.52	63.12	561.66	3.53	2.87	595.240383136	109	1.0")
			ThresholdWholeSheath.write("	")
		if tiedosto == 6:
			FractionalDips.write("2.52	63.12	561.66	3.53	2.87	595.240383136	109	1.0")
			FractionalDips.write("	")
		if tiedosto == 7:
			FractionalPeaks.write("2.52	63.12	561.66	3.53	2.87	595.240383136	109	1.0")
			FractionalPeaks.write("	")
	return

Fractional = open("/pathtoFile/File1.dat", 'w')
FractionalDips = open("/pathtoFile/File2.dat", 'w')
FractionalPeaks = open("/pathtoFile/File3.dat", 'w')
SingleSkippaus = 0	
	
Results = open("/pathtoFile/File4.dat", 'w') #Individual modes
Modes = open("/pathtoFile/File5.dat", 'w') #Statistics about mirror modes (MMs)
MVA_Intervals = open("/pathtoFile/File6.dat", 'w')
ResultsSimplified = open("/pathtoFile/File7.dat", 'w') #Simplified Individual Mode Statistics
MVASimplified = open("/pathtoFile/File8.dat", 'w')
ModesSimplified = open("/pathtoFile/File9.dat", 'w') #Simplified MM statistics
TrainLengthsDips = open("/pathtoFile/File10.dat", 'w')
TrainLengthsPeaks = open("/pathtoFile/File11.dat", 'w')
SingleMMs = open("/pathtoFile/File12.dat", 'w')
TrainMMs = open("/pathtoFile/File13.dat", 'w')
SheathFrac = open("/pathtoFile/File14.dat", 'w') #Fractional distances
PeakMMs = open("/pathtoFile/File15.dat", 'w')
DipMMs = open("/pathtoFile/File16.dat", 'w')

ThresholdWholeSheath = open("/pathtoFile/File17.dat", 'w')
ThresholdMirrorModes = open("/pathtoFile/File18.dat", 'w')
ThresholdOnlySheath = open("/pathtoFile/File19.dat", 'w')
CmSingles = open("/pathtoFile/File20.dat", 'w')
CmMMTrains = open("/pathtoFile/File21.dat", 'w')
CmTrains = open("/pathtoFile/File22.dat", 'w')

CmPeaks = open("/pathtoFile/File22.dat", 'w')
CmDips = open("/pathtoFile/File23.dat", 'w')

#Set the criteria
#MVA criteria:
MVA_Angle1 = 30
MVA_Angle2 = 150 
EV_relation_MinIM = 0.3
EV_relation_MaxIM = 1.5
#MirrorMode criteria
EdgeAngle = 10
MaxNumberOfMinMax = 2
DepthMin = 1.25
DepthMax = 0.75

#Downloading the data of studied events
day = 1
while day != 92:
	print day
 	if day == 1:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1997,1,10,00,52), datetime(1997,1,10,4,58), ['B3F1','B3GSE'])
		except:
			day = day + 1
	if day == 2:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1997,2,9,12,51), datetime(1997,2,10,2,44), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 3:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1997,5,15,1,15), datetime(1997,5,15,9,52), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 4:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1997,11,6,22,19), datetime(1997,11,7,5,28), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 5:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1997,11,22,9,13), datetime(1997,11,22,18,52), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 6:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,1,6,13,29), datetime(1998,1,7,2,50), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 7:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,1,28,15,54), datetime(1998,1,29,20,12), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 8:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,5,1,21,21), datetime(1998,5,2,9,12), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 9:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,8,19,18,40), datetime(1998,8,20,9,00), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 10:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,9,24,23,19), datetime(1998,9,25,6,28), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 11:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1998,10,18,19,29), datetime(1998,10,19,4,22), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 12:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1999,2,18,2,47), datetime(1999,2,18,10,28), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 13:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1999,3,10,1,33), datetime(1999,3,10,18,54), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 14:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1999,4,16,11,12), datetime(1999,4,16,15,35), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 15:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,2,11,23,34), datetime(2000,2,12,12,22), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 16:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,2,14,7,13), datetime(2000,2,14,17,15), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 17:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,2,20,21,4), datetime(2000,2,21,5,27), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 18:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,8,11,18,50), datetime(2000,8,12,5,32), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 19:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,9,4,13,15), datetime(2000,9,4,21,52), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 20:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,9,17,16,49), datetime(2000,9,17,23,00), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 21:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,10,3,1,2), datetime(2000,10,3,17,00), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 22:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,10,12,22,33), datetime(2000,10,13,5,52), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 23:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,11,6,9,30), datetime(2000,11,6,22,27), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 24:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2000,11,10,6,19), datetime(2000,11,10,11,46), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 25:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,1,23,10,48), datetime(2001,1,24,00,40), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 26:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,1,31,8,34), datetime(2001,2,1,2,50), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 27:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,3,19,11,34), datetime(2001,3,19,18,1), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 28:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,3,27,18,8), datetime(2001,3,27,23,2), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 29:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,4,4,14,41), datetime(2001,4,4,18,5), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 30:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,4,11,14,8), datetime(2001,4,11,22,45), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 31:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,4,18,00,50), datetime(2001,4,18,12,14), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 32:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,4,21,15,28), datetime(2001,4,22,00,8), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 33:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,4,28,5,5), datetime(2001,4,28,16,20), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 34:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,5,27,14,45), datetime(2001,5,28,4,15), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 35:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,8,17,11,1), datetime(2001,8,17,21,50), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 36:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,8,27,19,38), datetime(2001,8,28,5,28), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 37:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,9,25,20,17), datetime(2001,9,26,10,12), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 38:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,9,29,9,30), datetime(2001,9,29,11,56), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 39:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,10,28,3,13), datetime(2001,10,29,5,48), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 40:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,10,31,13,45), datetime(2001,10,31,18,35), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 41:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2001,11,24,5,53), datetime(2001,11,24,14,00), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 42:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,2,28,5,6), datetime(2002,2,28,18,36), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 43:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,3,18,13,13), datetime(2002,3,19,6,12), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 44:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,3,23,11,24), datetime(2002,3,24,11,39), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 45:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,5,11,10,30), datetime(2002,5,11,16,16), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 46:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,5,18,19,46), datetime(2002,5,19,3,20), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 47:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,8,1,5,19), datetime(2002,8,1,12,50), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 48:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,8,18,18,41), datetime(2002,8,19,22,00), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 49:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,9,7,16,21), datetime(2002,9,8,4,15), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 50:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,9,30,7,54), datetime(2002,9,30,21,26), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 51:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,11,16,23,31), datetime(2002,11,17,7,20), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 52:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2002,11,26,21,45), datetime(2002,11,27,7,48), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 53:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2003,3,20,4,27), datetime(2003,3,20,8,45), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 54:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2003,5,29,18,30), datetime(2003,5,30,3,18), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 55:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,7,22,9,45), datetime(2004,7,22,13,1), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 56:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,7,24,5,30), datetime(2004,7,24,11,50), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 57:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,7,26,22,24), datetime(2004,7,27,1,40), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 58:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,8,29,9,8), datetime(2004,8,29,18,31), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 59:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,11,7,17,59), datetime(2004,11,7,22,39), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 60:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2004,11,9,18,25), datetime(2004,11,9,20,27), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 61:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,5,15,2,11), datetime(2005,5,15,5,32), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 62:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,6,12,6,47), datetime(2005,6,12,14,41), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 63:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,6,14,17,56), datetime(2005,6,15,5,15), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 64:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,7,10,2,42), datetime(2005,7,10,10,10), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 65:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,7,17,00,53), datetime(2005,7,17,15,17), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 66:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2005,9,2,13,50), datetime(2005,9,2,18,43), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 67:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2006,4,13,11,19), datetime(2006,4,13,15,25), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 68:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2006,12,8,4,1), datetime(2006,12,8,14,53), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 69:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2006,12,14,13,52), datetime(2006,12,14,22,27), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 70:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2007,11,19,17,22), datetime(2007,11,19,23,20), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 71:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2009,2,3,19,21), datetime(2009,2,4,2,13), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 72:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2009,12,12,4,38), datetime(2009,12,12,18,7), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 73:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2010,4,5,7,56), datetime(2010,4,5,12,6), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 74:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2010,5,28,1,53), datetime(2010,5,28,19,50), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 75:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2011,3,29,15,10), datetime(2011,3,30,00,21), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 76:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2011,9,17,2,57), datetime(2011,9,17,15,40), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 77:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2011,9,26,11,44), datetime(2011,9,26,19,42), ['B3F1','B3GSE'])      
		except:
			day = day + 1
	if day == 78:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,4,23,2,15), datetime(2012,4,23,16,43), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 79:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,6,16,19,35), datetime(2012,6,16,22,15), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 80:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,7,14,17,39), datetime(2012,7,15,6,19), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 81:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,10,8,4,12), datetime(2012,10,8,17,15), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 82:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,10,11,22,47), datetime(2012,10,12,15,52), ['B3F1','B3GSE'])	
		except: day = day + 1

	if day == 83:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,10,31,14,28), datetime(2012,10,31,23,34), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 84:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2012,11,23,20,51), datetime(2012,11,24,11,34), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 85:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2013,3,17,5,22), datetime(2013,3,17,11,55), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 86:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2013,4,13,22,13), datetime(2013,4,14,16,40), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 87:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2013,7,12,16,43), datetime(2013,7,13,4,56), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 88:
		try:
	                data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2014,4,20,10,20), datetime(2014,4,21,7,25), ['B3F1','B3GSE'])       
		except:
			day = day + 1
	if day == 89:
		try:	
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2014,8,19,5,47), datetime(2014,8,19,17,30), ['B3F1','B3GSE'])
		except: day = day + 1
	if day == 90:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2014,9,12,15,17), datetime(2014,9,12,21,35), ['B3F1','B3GSE'])	
		except: day = day + 1
	if day == 91:
		try:
			data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2015,3,17,4,00), datetime(2015,3,17,13,9), ['B3F1','B3GSE'])
		except: day = day + 1
	

	mask = np.abs(data_mfi['B']) < 1e3
	data_mfi['B'] = data_mfi['B'][mask]
	data_mfi['EPOCH'] = np.array(data_mfi['EPOCH'])[mask]
	data_mfi['BX_(GSE)'] = data_mfi['BX_(GSE)'][mask]
	data_mfi['BY_(GSE)'] = data_mfi['BY_(GSE)'][mask]
	data_mfi['BZ_(GSE)'] = data_mfi['BZ_(GSE)'][mask]

	B = data_mfi['B']
	B_x = data_mfi['BX_(GSE)']
	B_y = data_mfi['BY_(GSE)']
	B_z = data_mfi['BZ_(GSE)']

	#The beginning and the length of a sheath
	TheBeginning = data_mfi['EPOCH'][0]
	TheLength = (data_mfi['EPOCH'][-1]-data_mfi['EPOCH'][0]).total_seconds()	

	TIMES = []
	index = 0
	k = 0
	#Going through the given data and doing the MVA
	while index < np.shape(B)[0]:
		#Taking the beginning point of the next interval
		while k+1 < np.shape(B)[0]:
			k = k + 1
			if k + 1 == np.shape(B)[0]:
				spot = k
			if (data_mfi['EPOCH'][k] - data_mfi['EPOCH'][index]).total_seconds() >= 3.0:
				spot = k
				break
		#Taking 1min interval
		while k+1 < np.shape(B)[0]:
			k = k + 1
			if (data_mfi['EPOCH'][k] - data_mfi['EPOCH'][index]).total_seconds() >= 60.0:
				break
		if (data_mfi['EPOCH'][index] - data_mfi['EPOCH'][spot]).total_seconds() == 0:
			break
        
		#Approving only intervals with 20 data points and which last exactly 60 seconds 
		if (data_mfi['EPOCH'][k] - data_mfi['EPOCH'][index]).total_seconds() == 60.0 and k-index == 20:
			#MVA to 1 minute interval
			AvB_x = 0
			AvB_y = 0
			AvB_z = 0
			Bxx = 0
			Bxy = 0
			Bxz = 0
			Byy = 0
			Byx = 0
			Byz = 0
			Bzz = 0
			Bzx = 0
			Bzy = 0
			Magnitude = 0
			j = 0
			Aika = k-index
			while j <= Aika:
				if index + j == np.shape(B_x)[0]:
					break
				Magnitude = Magnitude + ( B_x[index+j]**2 + B_y[index+j]**2 + B_z[index+j]**2 )**(1.0/2.0)
				AvB_x = AvB_x + B_x[index+j]
				AvB_y = AvB_y + B_y[index+j]
				AvB_z = AvB_z + B_z[index+j]
				Bxx = Bxx + B_x[index+j]**2
				Bxy = Bxy + B_x[index+j]*B_y[index+j]
				Bxz = Bxz + B_x[index+j]*B_z[index+j]
				Byy = Byy + B_y[index+j]**2
				Byz = Byz + B_y[index+j]*B_z[index+j]
				Bzz = Bzz + B_z[index+j]**2
				j = j + 1
			if j == 0:
				break
			Magnitude = Magnitude/j
			AvB_x = AvB_x/j
			AvB_y = AvB_y/j
			AvB_z = AvB_z/j
			Bxx = Bxx/j - AvB_x**2
			Bxy = Bxy/j - AvB_x*AvB_y
			Bxz = Bxz/j - AvB_x*AvB_z
			Byy = Byy/j - AvB_y**2
			Byx = Bxy
			Byz = Byz/j - AvB_y*AvB_z
			Bzz = Bzz/j - AvB_z**2
			Bzx = Bxz
			Bzy = Byz
			j = 0
			Var = 0
			while j <= Aika:
				if index + j == np.shape(B_x)[0]:
					break
				Var = Var + (B[index + j] - Magnitude)**2
				j = j + 1
			Var = Var/j
			b = [AvB_x, AvB_y, AvB_z]/Magnitude
			M = np.matrix([[Bxx, Bxy, Bxz],[Byx, Byy, Byz],[Bzx, Bzy, Bzz]])
			Eigenvalues, Eigenvectors = LA.eig(M)
			Max = np.argmax(Eigenvalues)
			MaxEV = Eigenvectors[Max]
			Min = np.argmin(Eigenvalues)
			MinEV = Eigenvectors[Min]
			if abs(Max - Min) == 2:
				IM = 1
			if Min == 1 and Max == 2:
				IM = 0
			if Min == 1 and Max == 0:
				IM = 2
			if Min == 2 and Max == 1:
				IM = 0
			if Min == 0 and Max == 1:
				IM = 2
			if Min == IM or Min == Max or Max == IM:
				print "Something went wrong"
			Max_Angle = MaxEV[0,0]*b[0] + MaxEV[0,1]*b[1] + MaxEV[0,2]*b[2]
			Min_Angle = MinEV[0,0]*b[0] + MinEV[0,1]*b[1] + MinEV[0,2]*b[2]
			Max_Angle = math.acos(Max_Angle)/(2*math.pi)*360
			Min_Angle = math.acos(Min_Angle)/(2*math.pi)*360
			Max_IM = Eigenvalues[Max]/Eigenvalues[IM]
			Min_IM = Eigenvalues[Min]/Eigenvalues[IM]
			#Testing if the one minute interval passes the MVA criteria and writing it down
			if Min_IM > EV_relation_MinIM and Max_IM > EV_relation_MaxIM and (Max_Angle < MVA_Angle1 or Max_Angle > MVA_Angle2):
				TIMES.append(index)
				TIMES.append(index+(k-index))
		index = spot
		k = spot
		
	#Combining overlapping MVA criteria satisfying intervals to array called TimeIntervals
	TimeIntervals = []
	w = 0
	while w < np.shape(TIMES)[0]:
		TimeIntervals.append(TIMES[w])
		w = w + 1
		v = w
		while v + 1 < np.shape(TIMES)[0]:
			if (data_mfi['EPOCH'][TIMES[v]] - data_mfi['EPOCH'][TIMES[v+1]]).total_seconds() <= 60.0 and (data_mfi['EPOCH'][TIMES[v]] - data_mfi['EPOCH'][TIMES[v+1]]).total_seconds() > 0.0:
				v = v + 2
			else:
				TimeIntervals.append(TIMES[v])
				break
		w = v + 1
	if np.shape(TIMES)[0] > 0:
		TimeIntervals.append(TIMES[-1])
	#TimeIntervals include now the new intervals which are not overlapping
	MirrorModes = 0
	index = 0
	Singles = 0
	Trains = 0
	Peaks = 0
	Dips = 0
	DipTrains = 0
	PeakTrains = 0
	Serie = []
	SerieLength = []
	FractionalDistances = []
	FractionalDistancesDips = []
	FractionalDistancesPeaks = []
	Locations = []
	LocationOfDips = []
	LocationOfPeaks = []
	LocationOfTrain = []
	LocationOfSingle = []
	while index < np.shape(TimeIntervals)[0]:
		Interval = []
		k = 0
		while k < np.shape(B)[0]:
			if k >= TimeIntervals[index] and k <= TimeIntervals[index+1]:
				Interval.append(k)
			if k > TimeIntervals[index+1]:
				break
			k = k + 1
		Beginning = Interval[0]
		Ending = Interval[-1]
		#The average magnetic field magnitude during the interval
		AverageB = 0
		k = 0
		while k < np.shape(Interval)[0]:
			AverageB = AverageB + B[Interval[k]]
			k = k + 1
		AverageB = AverageB/np.shape(Interval)[0]
		#The variance during the interval
		Variance = 0
		k = 0
		while k < np.shape(Interval)[0]:
			Variance = Variance + (B[Interval[k]] - AverageB)**2.0
			k = k + 1
		Variance = Variance/np.shape(Interval)[0]
		StanDev = Variance**(1.0/2.0)
		Magneticfield = B[Interval[0]:(Interval[-1]+1)]
		#Computing the skewness
		Skewness = 0
		k = 0
		while k < np.shape(Magneticfield)[0]:
			Skewness = Skewness + (Magneticfield[k] - AverageB)**3
			k = k + 1
		Skewness = Skewness/np.shape(Magneticfield)[0]
		Skewness = Skewness/(Variance**3)
		#Going through interval minima and maxima 
		minima = argrelextrema(Magneticfield, np.less)
		RightLimitsMin = []
		LeftLimitsMin = []
		Minimit = []
		Durationmin = []
		LocationsMin = []
		k = 0
		ModesMin = 0
		while k < np.shape(minima)[1]:
			Minimum = Magneticfield[minima[0][k]]
			spot = minima[0][k]
			l = 1
			LeftLimit = spot
			while spot - l >= 0:
				if Magneticfield[spot - l] < Minimum:
					LeftLimit = spot
					break
				if Magneticfield[spot - l] > (AverageB - StanDev) and Magneticfield[spot-l] > Minimum*DepthMin: 
					LeftLimit = spot - l
					break
				else:
					LeftLimit = spot
				l = l + 1
			l = 1
			RightLimit = spot
			while spot + l < np.shape(Magneticfield)[0]:
				if Magneticfield[spot + l] < Minimum:
					RightLimit = spot
					break
				if Magneticfield[spot + l] > (AverageB - StanDev) and Magneticfield[spot + l] > Minimum*DepthMin:
					RightLimit = spot + l
					break
				else:
					RightLimit = spot
				l = l + 1

			if LeftLimit != spot and RightLimit != spot:
				LeftEdge = Beginning + LeftLimit
				RightEdge = Beginning + RightLimit
				B1 = [B_x[LeftEdge], B_y[LeftEdge], B_z[LeftEdge]]
				B2 = [B_x[RightEdge], B_y[RightEdge], B_z[RightEdge]]
				Mag1 = (B1[0]**2 + B1[1]**2 + B1[2]**2)**(1.0/2.0)
				Mag2 = (B2[0]**2 + B2[1]**2 + B2[2]**2)**(1.0/2.0)
				angle = (B1[0]*B2[0] + B1[1]*B2[1] + B1[2]*B2[2])/(Mag1*Mag2)
				angle = math.acos(angle)/(2*math.pi)*360
				TheMode = B[LeftEdge:(RightEdge+1)]
				TheMode = np.array(TheMode)
				NumberOfMinima = np.shape(argrelextrema(TheMode, np.less))[1]
				if angle < EdgeAngle and NumberOfMinima <= MaxNumberOfMinMax:
					LeftLimitsMin.append(LeftEdge)
					RightLimitsMin.append(RightEdge)
					Minimit.append(Minimum)
					LocationsMin.append(Beginning + spot)
					Durationmin.append((data_mfi['EPOCH'][RightEdge]-data_mfi['EPOCH'][LeftEdge]).total_seconds())
					ModesMin = ModesMin + 1
			k = k + 1	

		Maxima = argrelextrema(Magneticfield, np.greater)
		RightLimitsMax = []
		LeftLimitsMax = []
		Maksimit = []
		Durationmax = []	
		LocationsMax = []
		k = 0
		ModesMax = 0
		while k < np.shape(Maxima)[1]:
			Maximum = Magneticfield[Maxima[0][k]]
			spot = Maxima[0][k]
			l = 1
			LeftLimit = spot
			while spot - l >= 0:
				if Magneticfield[spot - l] > Maximum:
					LeftLimit = spot
					break
				if Magneticfield[spot - l] < (AverageB + StanDev) and Magneticfield[spot-l] < Maximum*DepthMax:
					LeftLimit = spot - l
					break
				else:
					LeftLimit = spot
				l  = l + 1
			l = 1
			RightLimit = spot
			while spot + l < np.shape(Magneticfield)[0]:
				if Magneticfield[spot + l] > Maximum:					
					RightLimit = spot
					break
				if Magneticfield[spot + l] < (AverageB + StanDev) and Magneticfield[spot + l] < Maximum*DepthMax:
					RightLimit = spot + l
					break
				else:
					RightLimit = spot
				l = l + 1
			if LeftLimit != spot and RightLimit != spot:
				LeftEdge = Beginning + LeftLimit
				RightEdge = Beginning + RightLimit	
				B1 = [B_x[LeftEdge], B_y[LeftEdge], B_z[LeftEdge]]
				B2 = [B_x[RightEdge], B_y[RightEdge], B_z[RightEdge]]
				Mag1 = (B1[0]**2 + B1[1]**2 + B1[2]**2)**(1.0/2.0)
				Mag2 = (B2[0]**2 + B2[1]**2 + B2[2]**2)**(1.0/2.0)
				angle = (B1[0]*B2[0] + B1[1]*B2[1] + B1[2]*B2[2])/(Mag1*Mag2)
				angle = math.acos(angle)/(2*math.pi)*360
				TheMode = B[LeftEdge:(RightEdge+1)]
				TheMode = np.array(TheMode)
				NumberOfMaxima = np.shape(argrelextrema(TheMode, np.greater))[1]
				if angle < EdgeAngle and NumberOfMaxima <= MaxNumberOfMinMax:
					LeftLimitsMax.append(LeftEdge)
					RightLimitsMax.append(RightEdge)
					Maksimit.append(Maximum)
					LocationsMax.append(Beginning + spot)
					Durationmax.append((data_mfi['EPOCH'][RightEdge]-data_mfi['EPOCH'][LeftEdge]).total_seconds())
					ModesMax = ModesMax + 1
			k = k + 1
		#Comparing the number minima and maxima to the skewness
		if ModesMin != 0 or ModesMax!= 0:
			if Skewness < 0 and ModesMin >= ModesMax:
				MirrorModes = MirrorModes + ModesMin
				h = 0
				MVA_Intervals.write(str(data_mfi['EPOCH'][Beginning]))
				MVA_Intervals.write("	")
				MVA_Intervals.write(str(data_mfi['EPOCH'][Ending]))
				MVA_Intervals.write("	")
				MVA_Intervals.write(str((data_mfi['EPOCH'][Ending]-data_mfi['EPOCH'][Beginning]).total_seconds()))
				#MVA_Intervals.write("\n")
				MVASimplified.write(str((data_mfi['EPOCH'][Ending]-data_mfi['EPOCH'][Beginning]).total_seconds()))
				MVASimplified.write("\n")
				while h < np.shape(LeftLimitsMin)[0]:
					Location = (data_mfi['EPOCH'][LocationsMin[h]]-TheBeginning).total_seconds()
					Results.write(str(data_mfi['EPOCH'][LocationsMin[h]]))
					Locations.append(data_mfi['EPOCH'][LocationsMin[h]])
					
					LocationOfDips.append(data_mfi['EPOCH'][LocationsMin[h]])
					
					Results.write("	")
					Results.write(str(Location/TheLength))	
					Results.write("	")
					Duration = Durationmin[h]
					Results.write(str(Durationmin[h]))
					Results.write("	")
					Results.write(str(((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h])/((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0)))
					Results.write("	")
					Results.write(str((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h]))
					Results.write("	")
					#Parameters(day)
					FractionalDistances.append(Location/TheLength)
					FractionalDistancesDips.append(Location/TheLength)
					
					Results.write("\n")
					Parameters(day,1)
					ResultsSimplified.write(str(Location/TheLength))	
					ResultsSimplified.write("	")
					ResultsSimplified.write(str(Durationmin[h]))
					ResultsSimplified.write("	")
					ResultsSimplified.write(str(((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h])/((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0)))
					ResultsSimplified.write("	")
					ResultsSimplified.write(str((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h]))
					ResultsSimplified.write("\n")
					
					DipMMs.write(str(Location/TheLength))
					DipMMs.write("	")
					DipMMs.write(str(Durationmin[h]))
					DipMMs.write("	")
					DipMMs.write(str(((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h])/((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0)))
					DipMMs.write("	")
					DipMMs.write(str((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h]))
					DipMMs.write("\n")
					#ResultsSimplified.write("	")
					h = h + 1
				if ModesMin > 1:
					DipTrains = DipTrains + 1
					Trains = Trains + 1
					Serie.append(ModesMin)
					SerieLength.append((data_mfi['EPOCH'][RightLimitsMin[-1]]-data_mfi['EPOCH'][LeftLimitsMin[0]]).total_seconds())
					TrainLengthsDips.write(str(ModesMin))
					TrainLengthsDips.write("\n")
					
					MVA_Intervals.write("	")
					MVA_Intervals.write(str(1))
					MVA_Intervals.write("\n")
					h = 0
					while h < np.shape(LeftLimitsMin)[0]:
						Location = (data_mfi['EPOCH'][LocationsMin[h]]-TheBeginning).total_seconds()
						TrainMMs.write(str(Location/TheLength))
						TrainMMs.write("	")
						TrainMMs.write(str(Durationmin[h]))
						TrainMMs.write("	")
						TrainMMs.write(str(((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h])/((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0)))
						TrainMMs.write("	")
						TrainMMs.write(str((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h]))
						TrainMMs.write("\n")
						LocationOfTrain.append(data_mfi['EPOCH'][LocationsMin[h]])
						h = h + 1
					LocationOfTrain.append(0)
				else:
					MVA_Intervals.write("	")
					MVA_Intervals.write(str(0))
					MVA_Intervals.write("\n")
					h = 0
					while h < np.shape(LeftLimitsMin)[0]:
						Location = (data_mfi['EPOCH'][LocationsMin[h]]-TheBeginning).total_seconds()
						SingleMMs.write(str(Location/TheLength))
						SingleMMs.write("	")
						SingleMMs.write(str(Durationmin[h]))
						SingleMMs.write("	")
						SingleMMs.write(str(((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h])/((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0)))
						SingleMMs.write("	")
						SingleMMs.write(str((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h]))
						SingleMMs.write("\n")
						LocationOfSingle.append(data_mfi['EPOCH'][LocationsMin[h]])
						h = h + 1
					Singles = Singles + 1
				Dips = Dips + ModesMin
			elif Skewness > 0 and ModesMax >= ModesMin:
				MirrorModes = MirrorModes + ModesMax
				h = 0
				MVA_Intervals.write(str(data_mfi['EPOCH'][Beginning]))
				MVA_Intervals.write("	")
				MVA_Intervals.write(str(data_mfi['EPOCH'][Ending]))
				MVA_Intervals.write("	")
				MVA_Intervals.write(str((data_mfi['EPOCH'][Ending]-data_mfi['EPOCH'][Beginning]).total_seconds()))
				#MVA_Intervals.write("\n")
				MVASimplified.write(str((data_mfi['EPOCH'][Ending]-data_mfi['EPOCH'][Beginning]).total_seconds()))
				MVASimplified.write("\n")			
				while h < np.shape(LeftLimitsMax)[0]:
					Location = (data_mfi['EPOCH'][LocationsMax[h]]-TheBeginning).total_seconds()
					Results.write(str(data_mfi['EPOCH'][LocationsMax[h]]))
					Locations.append(data_mfi['EPOCH'][LocationsMax[h]])
					
					LocationOfPeaks.append(data_mfi['EPOCH'][LocationsMax[h]])
					
					Results.write("	")
					Results.write(str(Location/TheLength))	
					Results.write("	")
					Duration = Durationmax[h]
					Results.write(str(Durationmax[h]))
					Results.write("	")
					Results.write(str(((Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))/((B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0)))
					Results.write("	")
					Results.write(str(Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))
					Results.write("	")
					#Parameters(day)
					FractionalDistances.append(Location/TheLength)
					FractionalDistancesPeaks.append(Location/TheLength)
					
					Results.write("\n")
					Parameters(day,1)
					ResultsSimplified.write(str(Location/TheLength))	
					ResultsSimplified.write("	")
					ResultsSimplified.write(str(Durationmax[h]))
					ResultsSimplified.write("	")
					ResultsSimplified.write(str(((Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))/((B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0)))
					ResultsSimplified.write("	")
					ResultsSimplified.write(str(Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))
					ResultsSimplified.write("\n")
					#ResultsSimplified.write("	")
					
					PeakMMs.write(str(Location/TheLength))	
					PeakMMs.write("	")
					PeakMMs.write(str(Durationmax[h]))
					PeakMMs.write("	")
					PeakMMs.write(str(((Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))/((B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0)))
					PeakMMs.write("	")
					PeakMMs.write(str(Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))
					PeakMMs.write("\n")
					
					h = h + 1
				if ModesMax > 1:
					PeakTrains = PeakTrains + 1
					Trains = Trains + 1
					Serie.append(ModesMax)
					SerieLength.append((data_mfi['EPOCH'][RightLimitsMax[-1]]-data_mfi['EPOCH'][LeftLimitsMax[0]]).total_seconds())
					TrainLengthsPeaks.write(str(ModesMax))
					TrainLengthsPeaks.write("\n")
					MVA_Intervals.write("	")
					MVA_Intervals.write(str(1))
					MVA_Intervals.write("\n")
					h = 0
					while h < np.shape(LeftLimitsMax)[0]:
						Location = (data_mfi['EPOCH'][LocationsMax[h]]-TheBeginning).total_seconds()
						TrainMMs.write(str(Location/TheLength))	
						TrainMMs.write("	")
						TrainMMs.write(str(Durationmax[h]))
						TrainMMs.write("	")
						TrainMMs.write(str(((Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))/((B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0)))
						TrainMMs.write("	")
						TrainMMs.write(str(Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))
						TrainMMs.write("\n")
						LocationOfTrain.append(data_mfi['EPOCH'][LocationsMax[h]])
						h = h + 1
					LocationOfTrain.append(0)
				else:
					MVA_Intervals.write("	")
					MVA_Intervals.write(str(0))
					MVA_Intervals.write("\n")
					h = 0
					while h < np.shape(LeftLimitsMax)[0]:
						Location = (data_mfi['EPOCH'][LocationsMax[h]]-TheBeginning).total_seconds()
						SingleMMs.write(str(Location/TheLength))	
						SingleMMs.write("	")
						SingleMMs.write(str(Durationmax[h]))
						SingleMMs.write("	")
						SingleMMs.write(str(((Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))/((B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0)))
						SingleMMs.write("	")
						SingleMMs.write(str(Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))
						SingleMMs.write("\n")
						LocationOfSingle.append(data_mfi['EPOCH'][LocationsMax[h]])
						h = h + 1
					Singles = Singles + 1
				Peaks = Peaks + ModesMax
			else:
			#Plot mirror mode intervals when the skewness contradicts with the number of minima or maxima:
				print Skewness
				plt.figure(figsize = (12,7.5))
				if Beginning == 0 or Beginning-20<=0:
					plt.plot(data_mfi['EPOCH'][(Beginning):(Ending+20)],B[(Beginning):(Ending+20)], color = 'k', linewidth = 3)
				else:
					plt.plot(data_mfi['EPOCH'][(Beginning-20):(Ending+20)],B[(Beginning-20):(Ending+20)], color = 'k', linewidth = 3)
					plt.axvline(x = data_mfi['EPOCH'][Beginning], linewidth = 6, color = 'r')
					plt.axvline(x = data_mfi['EPOCH'][Ending], linewidth = 6, color = 'r')
				plt.ylabel('B[nT]', fontsize = 20, color = 'k',fontweight = 'bold')
				plt.xlabel('Time', fontsize = 20, color = 'k',fontweight = 'bold')
				if ModesMin != 0:
					h = 0
					while h < np.shape(LeftLimitsMin)[0]:
						plt.axvline(x = data_mfi['EPOCH'][LeftLimitsMin[h]], linewidth = 3, color = 'b')
						h = h + 1
					h = 0
					while h < np.shape(RightLimitsMin)[0]:
						plt.axvline(x = data_mfi['EPOCH'][RightLimitsMin[h]], linewidth = 3, color = 'b')
						h = h + 1
				if ModesMax != 0:
					h = 0
					while h < np.shape(LeftLimitsMax)[0]:
						plt.axvline(x = data_mfi['EPOCH'][LeftLimitsMax[h]], linewidth = 3, color = 'g')
						h = h + 1
					h = 0
					while h < np.shape(RightLimitsMax)[0]:
						plt.axvline(x = data_mfi['EPOCH'][RightLimitsMax[h]], linewidth = 3, color = 'g')
						h = h + 1
				plt.show()
				#Decide whether the interval has mirror modes 
				Choice = int(input("Dips(0), Peaks(1) or No mirror modes(2): "))
				if Choice == 0:
					MVA_Intervals.write(str(data_mfi['EPOCH'][Beginning]))
					MVA_Intervals.write("	")
					MVA_Intervals.write(str(data_mfi['EPOCH'][Ending]))
					MVA_Intervals.write("	")
					MVA_Intervals.write(str((data_mfi['EPOCH'][Ending]-data_mfi['EPOCH'][Beginning]).total_seconds()))
					#MVA_Intervals.write("\n")
					MVASimplified.write(str((data_mfi['EPOCH'][Ending]-data_mfi['EPOCH'][Beginning]).total_seconds()))
					MVASimplified.write("\n")
					MirrorModes = MirrorModes + ModesMin
					h = 0
					while h < np.shape(LeftLimitsMin)[0]:	
						Location = (data_mfi['EPOCH'][LocationsMin[h]]-TheBeginning).total_seconds()
						Results.write(str(data_mfi['EPOCH'][LocationsMin[h]]))
						Locations.append(data_mfi['EPOCH'][LocationsMin[h]])
						
						LocationOfDips.append(data_mfi['EPOCH'][LocationsMin[h]])
						
						Results.write("	")
						Results.write(str(Location/TheLength))	
						Results.write("	")
						Duration = Durationmin[h]
						Results.write(str(Durationmin[h]))
						Results.write("	")
						Results.write(str(((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h])/((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0)))
						Results.write("	")
						Results.write(str((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h]))
						Results.write("	")
						#Parameters(day)
						FractionalDistances.append(Location/TheLength)
						FractionalDistancesDips.append(Location/TheLength)
						
						Results.write("\n")
						Parameters(day,1)
						ResultsSimplified.write(str(Location/TheLength))	
						ResultsSimplified.write("	")
						ResultsSimplified.write(str(Durationmin[h]))
						ResultsSimplified.write("	")
						ResultsSimplified.write(str(((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h])/((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0)))
						ResultsSimplified.write("	")
						ResultsSimplified.write(str((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h]))
						ResultsSimplified.write("\n")
						#ResultsSimplified.write("	")
						
						DipMMs.write(str(Location/TheLength))
						DipMMs.write("	")
						DipMMs.write(str(Durationmin[h]))
						DipMMs.write("	")
						DipMMs.write(str(((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h])/((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0)))
						DipMMs.write("	")
						DipMMs.write(str((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h]))
						DipMMs.write("\n")
						
						h = h + 1
					if ModesMin > 1:
						DipTrains = DipTrains + 1
						Trains = Trains + 1
						Serie.append(ModesMin)
						SerieLength.append((data_mfi['EPOCH'][RightLimitsMin[-1]]-data_mfi['EPOCH'][LeftLimitsMin[0]]).total_seconds())
						TrainLengthsDips.write(str(ModesMin))
						TrainLengthsDips.write("\n")
						MVA_Intervals.write("	")
						MVA_Intervals.write(str(1))
						MVA_Intervals.write("\n")
						h = 0
						while h < np.shape(LeftLimitsMin)[0]:
							Location = (data_mfi['EPOCH'][LocationsMin[h]]-TheBeginning).total_seconds()
							TrainMMs.write(str(Location/TheLength))
							TrainMMs.write("	")
							TrainMMs.write(str(Durationmin[h]))
							TrainMMs.write("	")
							TrainMMs.write(str(((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h])/((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0)))
							TrainMMs.write("	")
							TrainMMs.write(str((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h]))
							TrainMMs.write("\n")
							LocationOfTrain.append(data_mfi['EPOCH'][LocationsMin[h]])
							h = h + 1
						LocationOfTrain.append(0)
					else:
						MVA_Intervals.write("	")
						MVA_Intervals.write(str(0))
						MVA_Intervals.write("\n")
						h = 0
						while h < np.shape(LeftLimitsMin)[0]:
							Location = (data_mfi['EPOCH'][LocationsMin[h]]-TheBeginning).total_seconds()
							SingleMMs.write(str(Location/TheLength))
							SingleMMs.write("	")
							SingleMMs.write(str(Durationmin[h]))
							SingleMMs.write("	")
							SingleMMs.write(str(((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h])/((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0)))
							SingleMMs.write("	")
							SingleMMs.write(str((B[LeftLimitsMin[h]]+B[RightLimitsMin[h]])/2.0-Minimit[h]))
							SingleMMs.write("\n")
							LocationOfSingle.append(data_mfi['EPOCH'][LocationsMin[h]])
							h = h + 1
						Singles = Singles + 1
					Dips = Dips + ModesMin

				elif Choice == 1:
					MVA_Intervals.write(str(data_mfi['EPOCH'][Beginning]))
					MVA_Intervals.write("	")
					MVA_Intervals.write(str(data_mfi['EPOCH'][Ending]))
					MVA_Intervals.write("	")
					MVA_Intervals.write(str((data_mfi['EPOCH'][Ending]-data_mfi['EPOCH'][Beginning]).total_seconds()))
					#MVA_Intervals.write("\n")
					MVASimplified.write(str((data_mfi['EPOCH'][Ending]-data_mfi['EPOCH'][Beginning]).total_seconds()))
					MVASimplified.write("\n")
					MirrorModes = MirrorModes + ModesMax
					h = 0
					while h < np.shape(LeftLimitsMax)[0]:
						Location = (data_mfi['EPOCH'][LocationsMax[h]]-TheBeginning).total_seconds()
						Results.write(str(data_mfi['EPOCH'][LocationsMax[h]]))
						Locations.append(data_mfi['EPOCH'][LocationsMax[h]])
						
						LocationOfPeaks.append(data_mfi['EPOCH'][LocationsMax[h]])
						
						Results.write("	")
						Results.write(str(Location/TheLength))	
						Results.write("	")
						Duration = Durationmax[h]
						Results.write(str(Durationmax[h]))
						Results.write("	")
						Results.write(str(((Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))/((B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0)))
						Results.write("	")
						Results.write(str(Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))
						Results.write("	")
						#Parameters(day)
						FractionalDistances.append(Location/TheLength)
						FractionalDistancesPeaks.append(Location/TheLength)
						
						Results.write("\n")
						Parameters(day,1)
						ResultsSimplified.write(str(Location/TheLength))	
						ResultsSimplified.write("	")
						ResultsSimplified.write(str(Durationmax[h]))
						ResultsSimplified.write("	")
						ResultsSimplified.write(str(((Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))/((B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0)))
						ResultsSimplified.write("	")
						ResultsSimplified.write(str(Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))
						ResultsSimplified.write("\n")
						#ResultsSimplified.write("	")
						PeakMMs.write(str(Location/TheLength))	
						PeakMMs.write("	")
						PeakMMs.write(str(Durationmax[h]))
						PeakMMs.write("	")
						PeakMMs.write(str(((Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))/((B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0)))
						PeakMMs.write("	")
						PeakMMs.write(str(Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))
						PeakMMs.write("\n")
						
						h = h + 1

					if ModesMax > 1:
						PeakTrains = PeakTrains + 1
						Trains = Trains + 1
						Serie.append(ModesMax)
						SerieLength.append((data_mfi['EPOCH'][RightLimitsMax[-1]]-data_mfi['EPOCH'][LeftLimitsMax[0]]).total_seconds())
						TrainLengthsPeaks.write(str(ModesMax))
						TrainLengthsPeaks.write("\n")
						MVA_Intervals.write("	")
						MVA_Intervals.write(str(1))
						MVA_Intervals.write("\n")
						h = 0
						while h < np.shape(LeftLimitsMax)[0]:
							Location = (data_mfi['EPOCH'][LocationsMax[h]]-TheBeginning).total_seconds()
							TrainMMs.write(str(Location/TheLength))	
							TrainMMs.write("	")
							TrainMMs.write(str(Durationmax[h]))
							TrainMMs.write("	")
							TrainMMs.write(str(((Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))/((B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0)))
							TrainMMs.write("	")
							TrainMMs.write(str(Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))
							TrainMMs.write("\n")
							LocationOfTrain.append(data_mfi['EPOCH'][LocationsMax[h]])
							h = h + 1
						LocationOfTrain.append(0)
					else:
						MVA_Intervals.write("	")
						MVA_Intervals.write(str(0))
						MVA_Intervals.write("\n")
						h = 0
						while h < np.shape(LeftLimitsMax)[0]:
							Location = (data_mfi['EPOCH'][LocationsMax[h]]-TheBeginning).total_seconds()
							SingleMMs.write(str(Location/TheLength))	
							SingleMMs.write("	")
							SingleMMs.write(str(Durationmax[h]))
							SingleMMs.write("	")
							SingleMMs.write(str(((Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))/((B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0)))
							SingleMMs.write("	")
							SingleMMs.write(str(Maksimit[h]-(B[LeftLimitsMax[h]]+B[RightLimitsMax[h]])/2.0))
							SingleMMs.write("\n")
							LocationOfSingle.append(data_mfi['EPOCH'][LocationsMax[h]])
							h = h + 1
						Singles = Singles + 1
					Peaks = Peaks + ModesMax
		index = index + 2
	if np.shape(FractionalDistances)[0]>0:
		F1 = [x for x in FractionalDistances if x < 0.10]
		F2 = [x for x in FractionalDistances if x >= 0.10 and x < 0.20]
		F3 = [x for x in FractionalDistances if x >= 0.20 and x < 0.30]
		F4 = [x for x in FractionalDistances if x >= 0.30 and x < 0.40]
		F5 = [x for x in FractionalDistances if x >= 0.40 and x < 0.50]
		F6 = [x for x in FractionalDistances if x >= 0.50 and x < 0.60]
		F7 = [x for x in FractionalDistances if x >= 0.60 and x < 0.70]
		F8 = [x for x in FractionalDistances if x >= 0.70 and x < 0.80]
		F9 = [x for x in FractionalDistances if x >= 0.80 and x < 0.90]
		F10 = [x for x in FractionalDistances if x >= 0.90]
	
		Parameters(day,3)
		Fractional.write(str(np.shape(F1)[0]))
		Fractional.write("	")
		Fractional.write(str(np.shape(F2)[0]))
		Fractional.write("	")
		Fractional.write(str(np.shape(F3)[0]))
		Fractional.write("	")
		Fractional.write(str(np.shape(F4)[0]))
		Fractional.write("	")
		Fractional.write(str(np.shape(F5)[0]))
		Fractional.write("	")
		Fractional.write(str(np.shape(F6)[0]))
		Fractional.write("	")
		Fractional.write(str(np.shape(F7)[0]))
		Fractional.write("	")
		Fractional.write(str(np.shape(F8)[0]))
		Fractional.write("	")
		Fractional.write(str(np.shape(F9)[0]))
		Fractional.write("	")
		Fractional.write(str(np.shape(F10)[0]))
		Fractional.write("\n")
	else:
		Parameters(day,3)
		Fractional.write('0')
		Fractional.write("	")
		Fractional.write('0')
		Fractional.write("	")
		Fractional.write('0')
		Fractional.write("	")
		Fractional.write('0')
		Fractional.write("	")
		Fractional.write('0')
		Fractional.write("	")
		Fractional.write('0')
		Fractional.write("	")
		Fractional.write('0')
		Fractional.write("	")
		Fractional.write('0')
		Fractional.write("	")
		Fractional.write('0')
		Fractional.write("	")
		Fractional.write('0')
		Fractional.write("\n")
		
	if np.shape(FractionalDistancesDips)[0]>0:
		F1 = [x for x in FractionalDistancesDips if x < 0.10]
		F2 = [x for x in FractionalDistancesDips if x >= 0.10 and x < 0.20]
		F3 = [x for x in FractionalDistancesDips if x >= 0.20 and x < 0.30]
		F4 = [x for x in FractionalDistancesDips if x >= 0.30 and x < 0.40]
		F5 = [x for x in FractionalDistancesDips if x >= 0.40 and x < 0.50]
		F6 = [x for x in FractionalDistancesDips if x >= 0.50 and x < 0.60]
		F7 = [x for x in FractionalDistancesDips if x >= 0.60 and x < 0.70]
		F8 = [x for x in FractionalDistancesDips if x >= 0.70 and x < 0.80]
		F9 = [x for x in FractionalDistancesDips if x >= 0.80 and x < 0.90]
		F10 = [x for x in FractionalDistancesDips if x >= 0.90]
	
		Parameters(day,6)
		FractionalDips.write(str(np.shape(F1)[0]))
		FractionalDips.write("	")
		FractionalDips.write(str(np.shape(F2)[0]))
		FractionalDips.write("	")
		FractionalDips.write(str(np.shape(F3)[0]))
		FractionalDips.write("	")
		FractionalDips.write(str(np.shape(F4)[0]))
		FractionalDips.write("	")
		FractionalDips.write(str(np.shape(F5)[0]))
		FractionalDips.write("	")
		FractionalDips.write(str(np.shape(F6)[0]))
		FractionalDips.write("	")
		FractionalDips.write(str(np.shape(F7)[0]))
		FractionalDips.write("	")
		FractionalDips.write(str(np.shape(F8)[0]))
		FractionalDips.write("	")
		FractionalDips.write(str(np.shape(F9)[0]))
		FractionalDips.write("	")
		FractionalDips.write(str(np.shape(F10)[0]))
		FractionalDips.write("\n")
	else:
		Parameters(day,6)
		FractionalDips.write('0')
		FractionalDips.write("	")
		FractionalDips.write('0')
		FractionalDips.write("	")
		FractionalDips.write('0')
		FractionalDips.write("	")
		FractionalDips.write('0')
		FractionalDips.write("	")
		FractionalDips.write('0')
		FractionalDips.write("	")
		FractionalDips.write('0')
		FractionalDips.write("	")
		FractionalDips.write('0')
		FractionalDips.write("	")
		FractionalDips.write('0')
		FractionalDips.write("	")
		FractionalDips.write('0')
		FractionalDips.write("	")
		FractionalDips.write('0')
		FractionalDips.write("\n")	
	
	if np.shape(FractionalDistancesPeaks)[0]>0:
		F1 = [x for x in FractionalDistancesPeaks if x < 0.10]
		F2 = [x for x in FractionalDistancesPeaks if x >= 0.10 and x < 0.20]
		F3 = [x for x in FractionalDistancesPeaks if x >= 0.20 and x < 0.30]
		F4 = [x for x in FractionalDistancesPeaks if x >= 0.30 and x < 0.40]
		F5 = [x for x in FractionalDistancesPeaks if x >= 0.40 and x < 0.50]
		F6 = [x for x in FractionalDistancesPeaks if x >= 0.50 and x < 0.60]
		F7 = [x for x in FractionalDistancesPeaks if x >= 0.60 and x < 0.70]
		F8 = [x for x in FractionalDistancesPeaks if x >= 0.70 and x < 0.80]
		F9 = [x for x in FractionalDistancesPeaks if x >= 0.80 and x < 0.90]
		F10 = [x for x in FractionalDistancesPeaks if x >= 0.90]
	
		Parameters(day,7)
		FractionalPeaks.write(str(np.shape(F1)[0]))
		FractionalPeaks.write("	")
		FractionalPeaks.write(str(np.shape(F2)[0]))
		FractionalPeaks.write("	")
		FractionalPeaks.write(str(np.shape(F3)[0]))
		FractionalPeaks.write("	")
		FractionalPeaks.write(str(np.shape(F4)[0]))
		FractionalPeaks.write("	")
		FractionalPeaks.write(str(np.shape(F5)[0]))
		FractionalPeaks.write("	")
		FractionalPeaks.write(str(np.shape(F6)[0]))
		FractionalPeaks.write("	")
		FractionalPeaks.write(str(np.shape(F7)[0]))
		FractionalPeaks.write("	")
		FractionalPeaks.write(str(np.shape(F8)[0]))
		FractionalPeaks.write("	")
		FractionalPeaks.write(str(np.shape(F9)[0]))
		FractionalPeaks.write("	")
		FractionalPeaks.write(str(np.shape(F10)[0]))
		FractionalPeaks.write("\n")
	else:
		Parameters(day,7)
		FractionalPeaks.write('0')
		FractionalPeaks.write("	")
		FractionalPeaks.write('0')
		FractionalPeaks.write("	")
		FractionalPeaks.write('0')
		FractionalPeaks.write("	")
		FractionalPeaks.write('0')
		FractionalPeaks.write("	")
		FractionalPeaks.write('0')
		FractionalPeaks.write("	")
		FractionalPeaks.write('0')
		FractionalPeaks.write("	")
		FractionalPeaks.write('0')
		FractionalPeaks.write("	")
		FractionalPeaks.write('0')
		FractionalPeaks.write("	")
		FractionalPeaks.write('0')
		FractionalPeaks.write("	")
		FractionalPeaks.write('0')
		FractionalPeaks.write("\n")
		
	
	if np.shape(FractionalDistances)[0] > 0:
		NearShock = [x for x in FractionalDistances if x < 0.33]
		MidSheath = [x for x in FractionalDistances if x >= 0.33 and x < 0.66]
		NearLE = [x for x in FractionalDistances if x >= 0.66]	
		NearShockPercent = float(np.shape(NearShock)[0])/np.shape(FractionalDistances)[0]
		MidSheathPercent = float(np.shape(MidSheath)[0])/np.shape(FractionalDistances)[0]
		NearLEPercent = float(np.shape(NearLE)[0])/np.shape(FractionalDistances)[0]
	
		Parameters(day,4)
		SheathFrac.write(str(np.shape(NearShock)[0]))
		SheathFrac.write("	")
		SheathFrac.write(str(np.shape(MidSheath)[0]))
		SheathFrac.write("	")
		SheathFrac.write(str(np.shape(NearLE)[0]))
		SheathFrac.write("	")
		SheathFrac.write(str(NearShockPercent))
		SheathFrac.write("	")
		SheathFrac.write(str(MidSheathPercent))
		SheathFrac.write("	")
		SheathFrac.write(str(NearLEPercent))
		SheathFrac.write("\n")
	else:
		Parameters(day,4)
		SheathFrac.write('0')
		SheathFrac.write("	")
		SheathFrac.write('0')
		SheathFrac.write("	")
		SheathFrac.write('0')
		SheathFrac.write("	")
		SheathFrac.write('0')
		SheathFrac.write("	")
		SheathFrac.write('0')
		SheathFrac.write("	")
		SheathFrac.write('0')
		SheathFrac.write("\n")
	
	Modes.write(str(data_mfi['EPOCH'][0]))
	Modes.write('	')
	Modes.write(str(data_mfi['EPOCH'][-1]))
	Modes.write('	')
	Modes.write(str(Singles + Trains))
	Modes.write('	')
	Modes.write(str(Singles))
	Modes.write('	')
	Modes.write(str(Trains))
	Modes.write('	')
	Modes.write(str(MirrorModes))
	Modes.write('	')
	Modes.write(str(Dips))
	Modes.write('	')
	Modes.write(str(Peaks))
	Modes.write('	')
	Modes.write(str(DipTrains))
	Modes.write('	')
	Modes.write(str(PeakTrains))
	Modes.write('\n')
	Parameters(day,2)
	ModesSimplified.write(str(TheLength))
	ModesSimplified.write("	")
	ModesSimplified.write(str(Singles + Trains))
	ModesSimplified.write("	")
	ModesSimplified.write(str(Singles))
	ModesSimplified.write("	")
	ModesSimplified.write(str(Trains))
	ModesSimplified.write("	")
	ModesSimplified.write(str(MirrorModes))
	ModesSimplified.write("	")
	ModesSimplified.write(str(Dips))
	ModesSimplified.write("	")
	ModesSimplified.write(str(Peaks))
	ModesSimplified.write("	")
	ModesSimplified.write(str(DipTrains))
	ModesSimplified.write("	")
	ModesSimplified.write(str(PeakTrains))
	ModesSimplified.write('\n')

	#Computing plasma parameters
	Ehto = 0
	if day == 1:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,1,10,00,52), datetime(1997,1,10,4,58),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 2:
		try: 
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,2,9,12,51), datetime(1997,2,10,2,44),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 3:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,5,15,1,15), datetime(1997,5,15,9,52),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])      
			Ehto = 1
		except:
			Ehto = 0
	if day == 4:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,11,6,22,19), datetime(1997,11,7,5,28),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 5:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1997,11,22,9,13), datetime(1997,11,22,18,52),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 6:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,1,6,13,29), datetime(1998,1,7,2,50),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 7:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,1,28,15,54), datetime(1998,1,29,20,12),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 8:
		try: 
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,5,1,21,21), datetime(1998,5,2,9,12),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])     
			Ehto = 1
		except:
			Ehto = 0
	if day == 9:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,8,19,18,40), datetime(1998,8,20,9,00),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])       
			Ehto = 1
		except:
			Ehto = 0
	if day == 10:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,9,24,23,19), datetime(1998,9,25,6,28),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 11:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1998,10,18,19,29), datetime(1998,10,19,4,22),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 12:
		try:
			#data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(1999,2,18,2,47), datetime(1999,2,18,10,28), ['B3F1','B3GSE'])
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1999,2,18,2,47), datetime(1999,2,18,10,28),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 13:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1999,3,10,1,33), datetime(1999,3,10,18,54),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 14:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(1999,4,16,11,12), datetime(1999,4,16,15,35),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])     
			Ehto = 1
		except:
			Ehto = 0
	if day == 15:
		try: 
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,2,11,23,34), datetime(2000,2,12,12,22),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])     
			Ehto = 1
		except:
			Ehto = 0
	if day == 16:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,2,14,7,13), datetime(2000,2,14,17,15),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 17:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,2,20,21,4), datetime(2000,2,21,5,27),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 18:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,8,11,18,50), datetime(2000,8,12,5,32),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 19:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,9,4,13,15), datetime(2000,9,4,21,52),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 20:
		try: 
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,9,17,16,43), datetime(2000,9,17,23,00),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])   
			Ehto = 1
		except:
			Ehto = 0
	if day == 21:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,10,3,1,2), datetime(2000,10,3,17,00),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])      
			Ehto = 1
		except:
			Ehto = 0
	if day == 22:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,10,12,22,33), datetime(2000,10,13,5,52),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 23:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,11,6,9,30), datetime(2000,11,6,22,27),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 24:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2000,11,10,6,19), datetime(2000,11,10,11,46),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 25:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,1,23,10,48), datetime(2001,1,24,00,40),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 26:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,1,31,8,34), datetime(2001,2,1,2,50),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])    
			Ehto = 1
		except:
			Ehto = 0
	if day == 27:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,3,19,11,34), datetime(2001,3,19,18,1),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])      
			Ehto = 1
		except:
			Ehto = 0
	if day == 28:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,3,27,18,8), datetime(2001,3,27,23,2),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 29:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,4,14,38), datetime(2001,4,4,18,5),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 30:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,11,14,8), datetime(2001,4,11,22,45),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 31:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,18,00,50), datetime(2001,4,18,12,14),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 32:
		try:  
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,21,15,28), datetime(2001,4,22,00,8),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])    
			Ehto = 1
		except:
			Ehto = 0
	if day == 33:
		try: 
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,4,28,5,5), datetime(2001,4,28,16,20),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])     
			Ehto = 1
		except:
			Ehto = 0
	if day == 34:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,5,27,14,45), datetime(2001,5,28,4,15),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 35:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,8,17,11,1), datetime(2001,8,17,21,50),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 36:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,8,27,19,38), datetime(2001,8,28,5,28),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 37:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,9,25,20,17), datetime(2001,9,26,10,12),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 38:
		try:    
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,9,29,9,30), datetime(2001,9,29,11,56),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])  
			Ehto = 1
		except:
			Ehto = 0
	if day == 39:
		try:  
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,10,28,3,13), datetime(2001,10,29,5,48),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])     
			Ehto = 1
		except:
			Ehto = 0
	if day == 40:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,10,31,13,45), datetime(2001,10,31,18,35),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 41:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2001,11,24,5,53), datetime(2001,11,24,14,00),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 42:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,2,28,5,6), datetime(2002,2,28,18,36),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 43:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,3,18,13,13), datetime(2002,3,19,6,12),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 44:
		try: 
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,3,23,11,24), datetime(2002,3,24,11,39),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])     
			Ehto = 1
		except:
			Ehto = 0
	if day == 45:
		try:  
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,5,11,10,30), datetime(2002,5,11,16,16),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])     
			Ehto = 1
		except:
			Ehto = 0
	if day == 46:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,5,18,19,46), datetime(2002,5,19,3,20),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 47:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,8,1,5,19), datetime(2002,8,1,12,50),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 48:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,8,18,18,35), datetime(2002,8,19,22,00),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 49:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,9,7,16,21), datetime(2002,9,8,4,15),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 50:
		try: 
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,9,30,7,54), datetime(2002,9,30,21,26),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])     
			Ehto = 1
		except:
			Ehto = 0
	if day == 51:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,11,16,23,31), datetime(2002,11,17,7,20),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])      
			Ehto = 1
		except:
			Ehto = 0
	if day == 52:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2002,11,26,21,45), datetime(2002,11,27,7,48),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 53:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2003,3,20,4,27), datetime(2003,3,20,8,45),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 54:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2003,5,29,18,30), datetime(2003,5,30,3,18),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 55:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,7,22,9,45), datetime(2004,7,22,13,1),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 56:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,7,24,5,30), datetime(2004,7,24,11,50),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 57:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,7,26,22,24), datetime(2004,7,27,1,40),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 58:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,8,29,9,8), datetime(2004,8,29,18,31),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 59:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,11,7,17,59), datetime(2004,11,7,22,39),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])      
			Ehto = 1
		except:
			Ehto = 0
	if day == 60:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2004,11,9,18,25), datetime(2004,11,9,20,27),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])      
			Ehto = 1
		except:
			Ehto = 0
	if day == 61:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,5,15,2,11), datetime(2005,5,15,5,32),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 62:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,6,12,6,47), datetime(2005,6,12,14,41),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 63:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,6,14,17,56), datetime(2005,6,15,5,15),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 64:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,7,10,2,42), datetime(2005,7,10,10,10),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 65:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,7,17,00,53), datetime(2005,7,17,15,17),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])      
			Ehto = 1
		except:
			Ehto = 0
	if day == 66:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2005,9,2,13,50), datetime(2005,9,2,18,43),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])       
			Ehto = 1
		except:
			Ehto = 0
	if day == 67:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2006,4,13,11,19), datetime(2006,4,13,15,25),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 68:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2006,12,8,4,1), datetime(2006,12,8,14,53),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 69:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2006,12,14,13,52), datetime(2006,12,14,22,27),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 70:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2007,11,19,17,22), datetime(2007,11,19,23,20),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 71:
		try:  
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2009,2,3,19,21), datetime(2009,2,4,2,13),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])    
			Ehto = 1
		except:
			Ehto = 0
	if day == 72:
		try: 
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2009,12,12,4,38), datetime(2009,12,12,18,7),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])      
			Ehto = 1
		except:
			Ehto = 0
	if day == 73:
		Ehto = 0
		#print day
		print "no plasma data"
		#day = day + 1
		#try:######3	
		#	data_mfi = cdas.get_data('sp_phys', 'WI_H0_MFI', datetime(2010,4,5,7,56), datetime(2010,4,5,12,6), ['B3F1','B3GSE'])
		#	data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2010,4,5,7,56), datetime(2010,4,5,12,6),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
		#	Ehto = 1
		#except: day = day + 1
	if day == 74:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2010,5,28,1,53), datetime(2010,5,28,19,50),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 75:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2011,3,29,15,10), datetime(2011,3,30,00,21),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 76:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2011,9,17,2,57), datetime(2011,9,17,15,40),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 77:
		try: 
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2011,9,26,11,44), datetime(2011,9,26,19,42),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])     
			Ehto = 1
		except:
			Ehto = 0
	if day == 78:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,4,23,2,15), datetime(2012,4,23,16,43),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])      
			Ehto = 1
		except:
			Ehto = 0
	if day == 79:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,6,16,19,35), datetime(2012,6,16,22,15),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 80:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,7,14,17,39), datetime(2012,7,15,6,19),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 81:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,10,8,4,12), datetime(2012,10,8,17,15),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 82:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,10,11,22,47), datetime(2012,10,12,15,52),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 83:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,10,31,14,28), datetime(2012,10,31,23,34),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])      
			Ehto = 1
		except:
			Ehto = 0
	if day == 84:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2012,11,23,20,51), datetime(2012,11,24,11,34),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 85:
		try:	
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2013,3,17,5,22), datetime(2013,3,17,11,55),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 86:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2013,4,13,22,13), datetime(2013,4,14,16,40),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 87:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2013,7,12,16,43), datetime(2013,7,13,4,56),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 88:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2014,4,20,10,20), datetime(2014,4,21,7,25),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])      
			Ehto = 1
		except:
			Ehto = 0
	if day == 89:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2014,8,19,5,47), datetime(2014,8,19,17,30),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if day == 90:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2014,9,12,15,17), datetime(2014,9,12,21,35),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])	
			Ehto = 1
		except:
			Ehto = 0
	if day == 91:
		try:
			data_swe = cdas.get_data('sp_phys', 'WI_H1_SWE', datetime(2015,3,17,4,00), datetime(2015,3,17,13,9),['Proton_Wperp_nonlin','Proton_Wpar_nonlin','Proton_Np_nonlin'])
			Ehto = 1
		except:
			Ehto = 0
	if Ehto == 0:
		print day
		print "skip"
	
	if Ehto == 1:
		mask = np.abs(data_swe['P+_WPERP_NONLIN']) < 1e3
		data_swe['P+_DENSITY'] = data_swe['P+_DENSITY'][mask]
		data_swe['EPOCH'] = np.array(data_swe['EPOCH'])[mask]
		data_swe['P+_WPERP_NONLIN'] = data_swe['P+_WPERP_NONLIN'][mask]
		data_swe['P+_WPAR_NONLIN'] = data_swe['P+_WPAR_NONLIN'][mask]

		mask = np.abs(data_swe['P+_DENSITY']) < 1e3
		data_swe['P+_DENSITY'] = data_swe['P+_DENSITY'][mask]
		data_swe['EPOCH'] = np.array(data_swe['EPOCH'])[mask]
		data_swe['P+_WPERP_NONLIN'] = data_swe['P+_WPERP_NONLIN'][mask]
		data_swe['P+_WPAR_NONLIN'] = data_swe['P+_WPAR_NONLIN'][mask]
		
		mask = np.abs(data_swe['P+_WPAR_NONLIN']) < 1e3
		data_swe['P+_DENSITY'] = data_swe['P+_DENSITY'][mask]
		data_swe['EPOCH'] = np.array(data_swe['EPOCH'])[mask]
		data_swe['P+_WPERP_NONLIN'] = data_swe['P+_WPERP_NONLIN'][mask]
		data_swe['P+_WPAR_NONLIN'] = data_swe['P+_WPAR_NONLIN'][mask]
		
		B = data_mfi['B']
		B_x = data_mfi['BX_(GSE)']
		B_y = data_mfi['BY_(GSE)']
		B_z = data_mfi['BZ_(GSE)']

		WPERP = data_swe['P+_WPERP_NONLIN']
		WPAR = data_swe['P+_WPAR_NONLIN']
		DENSITY = data_swe['P+_DENSITY']
		
		values = []
		k = 0
		while k < np.shape(DENSITY)[0]:
			spot = 0
			variable1 = data_mfi['EPOCH'][0]
			variable2 = data_mfi['EPOCH'][0]
			Difference1 = abs((data_swe['EPOCH'][k]-variable1).total_seconds())
			Difference2 = (variable2-data_swe['EPOCH'][k]).total_seconds()

			slot1 = spot
			
			while spot < np.shape(data_mfi['EPOCH'])[0]:
				
				if abs((data_swe['EPOCH'][k]-variable1).total_seconds()) > abs((data_swe['EPOCH'][k]-data_mfi['EPOCH'][spot]).total_seconds()):
					variable1 = data_mfi['EPOCH'][spot]
					Difference1 = abs((data_swe['EPOCH'][k]-data_mfi['EPOCH'][spot]).total_seconds())
					slot1 = spot
				spot = spot + 1
			values.append(slot1)	
			k = k + 1
					
		#Computing plasma beta and mirror instability in the whole ICME sheath and writing them down
		index = 0
		while index < np.shape(data_swe['EPOCH'])[0]:
			TheSpotInSheath = (data_swe['EPOCH'][index]-TheBeginning).total_seconds()
			TheSpotInSheath = TheSpotInSheath/TheLength
			TPERP = ((WPERP[index]*1000)**2.0*1.672621898*10**(-27.0))/(1.38064881e-23)
			TPAR  = ((WPAR[index]*1000)**2.0*1.672621898*10**(-27.0))/(1.38064881e-23)
	
			Threshold = TPERP/TPAR-1
		
			Beta = 2*(12.566370614e-7)*(1.38064881e-23)
			Beta = Beta/( (B[values[index]]*10**(-9.0))**2 )

			BetaPAR = Beta*(DENSITY[index]*10**6)*TPAR
			BetaPERP = Beta*(DENSITY[index]*10**6)*TPERP

			#ThresHoldi = Threshold - 0.87/BetaPAR**(0.56)
			ThresHoldi = Threshold - 1/BetaPERP
			Parameters(day, 5)	
			ThresholdWholeSheath.write(str(TheSpotInSheath))
			ThresholdWholeSheath.write("	")	
			ThresholdWholeSheath.write(str(BetaPAR))
			ThresholdWholeSheath.write("	")
			ThresholdWholeSheath.write(str(BetaPERP))
			ThresholdWholeSheath.write("	")
			ThresholdWholeSheath.write(str(ThresHoldi))
			ThresholdWholeSheath.write("\n")
			index = index + 1
		
		#Computing plasma beta and mirror instability of MMs appearing as single, isolated ones
		k = 0
		while k < np.shape(LocationOfSingle)[0]:
			Location = (LocationOfSingle[k]-TheBeginning).total_seconds()
			Location = Location/TheLength
			ajat = []
			j = 0
			while j < np.shape(data_swe['EPOCH'])[0]:
				if (LocationOfSingle[k]-data_swe['EPOCH'][j]).total_seconds() <= 150.0 and (LocationOfSingle[k]-data_swe['EPOCH'][j]).total_seconds() > 0.0:
					ajat.append(j)
				if (data_swe['EPOCH'][j]-LocationOfSingle[k]).total_seconds() <= 150.0 and (data_swe['EPOCH'][j]-LocationOfSingle[k]).total_seconds() > 0.0:
					ajat.append(j)
				j = j + 1
			if np.shape(ajat)[0] != 0:
				j = 0
				TPERP = 0
				TPAR = 0
				n = 0
				MagF = 0
				
				while j < np.shape(ajat)[0]:
					TPERP = TPERP + (WPERP[ajat[j]]*1000)**2.0
					TPAR = TPAR + (WPAR[ajat[j]]*1000)**2.0
					MagF = MagF + (B[values[ajat[j]]]*10**(-9.0))**2
					n = n + DENSITY[ajat[j]]*10**6
					j = j + 1
				
				TPERP = (TPERP*1.672621898*10**(-27.0))/(1.38064881e-23)
				TPAR = (TPAR*1.672621898*10**(-27.0))/(1.38064881e-23)
				
				Threshold = TPERP/TPAR-1
			
				Beta = 2*(12.566370614e-7)*(1.38064881e-23)
				Beta = Beta/MagF

				BetaPAR = Beta*n*TPAR
				BetaPERP = Beta*n*TPERP

				BetaPAR = BetaPAR/j
				BetaPERP = BetaPERP/j

				ThresHoldi = Threshold - 1/BetaPERP	
				CmSingles.write(str(Location))
				CmSingles.write("	")
				CmSingles.write(str(BetaPAR))
				CmSingles.write("	")
				CmSingles.write(str(BetaPERP))
				CmSingles.write("	")
				CmSingles.write(str(ThresHoldi))
				CmSingles.write("\n")	
			else:
				SingleSkippaus = SingleSkippaus + 1
			k = k + 1

		#Computing plasma beta and mirror instability of MM in MM trains
		k = 0
		while k < np.shape(LocationOfTrain)[0]:
			i = k
			Bpe = 0
			Bpa = 0
			Cm = 0
			Frac = 0
			while LocationOfTrain[i] !=0 :
				Location = (LocationOfTrain[i]-TheBeginning).total_seconds()
				Location = Location/TheLength
				ajat = []
				j = 0
				while j < np.shape(data_swe['EPOCH'])[0]:
					if (LocationOfTrain[i]-data_swe['EPOCH'][j]).total_seconds() <= 150.0 and (LocationOfTrain[i]-data_swe['EPOCH'][j]).total_seconds() > 0.0:
						ajat.append(j)
					if (data_swe['EPOCH'][j]-LocationOfTrain[i]).total_seconds() <= 150.0 and (data_swe['EPOCH'][j]-LocationOfTrain[i]).total_seconds() > 0.0:
						ajat.append(j)
					j = j + 1
				if np.shape(ajat)[0] != 0:
					j = 0
					TPERP = 0
					TPAR = 0
					n = 0
					MagF = 0
				
					while j < np.shape(ajat)[0]:
						TPERP = TPERP + (WPERP[ajat[j]]*1000)**2.0
						TPAR = TPAR + (WPAR[ajat[j]]*1000)**2.0
						MagF = MagF + (B[values[ajat[j]]]*10**(-9.0))**2
						n = n + DENSITY[ajat[j]]*10**6
						j = j + 1
				
					TPERP = (TPERP*1.672621898*10**(-27.0))/(1.38064881e-23)
					TPAR = (TPAR*1.672621898*10**(-27.0))/(1.38064881e-23)
				
					Threshold = TPERP/TPAR-1
			
					Beta = 2*(12.566370614e-7)*(1.38064881e-23)
					Beta = Beta/MagF

					BetaPAR = Beta*n*TPAR
					BetaPERP = Beta*n*TPERP

					BetaPAR = BetaPAR/j
					BetaPERP = BetaPERP/j

					ThresHoldi = Threshold - 1/BetaPERP	
					
					Bpe = Bpe + BetaPERP
					Bpa = Bpa + BetaPAR
					Cm = Cm + ThresHoldi
					Frac = Frac + Location
					CmMMTrains.write(str(Location))
					CmMMTrains.write("	")
					CmMMTrains.write(str(BetaPAR))
					CmMMTrains.write("	")
					CmMMTrains.write(str(BetaPERP))
					CmMMTrains.write("	")
					CmMMTrains.write(str(ThresHoldi))
					CmMMTrains.write("\n")
				i = i + 1
			Bpe = Bpe/(i-k)
			Bpa = Bpa/(i-k)
			Cm = Cm/(i-k)
			Frac = Frac/(i-k)
			CmTrains.write(str(i-k))
			CmTrains.write("	")
			CmTrains.write(str(Frac))
			CmTrains.write("	")
			CmTrains.write(str(Bpa))
			CmTrains.write("	")
			CmTrains.write(str(Bpe))
			CmTrains.write("	")
			CmTrains.write(str(Cm))
			CmTrains.write("\n")
			k = i + 1

		#Computing plasma beta and mirror instability of all MM
		k = 0
		DeletedOnes = []
		while k < np.shape(Locations)[0]:
			Location = (Locations[k]-TheBeginning).total_seconds()
			Location = Location/TheLength
			ajat = []
			j = 0
			#Taking the surrounding of a MM			
			while j < np.shape(data_swe['EPOCH'])[0]:
				if (Locations[k]-data_swe['EPOCH'][j]).total_seconds() <= 150.0 and (Locations[k]-data_swe['EPOCH'][j]).total_seconds() > 0.0:
					#ajat.append(data_swe['EPOCH'][j])
					ajat.append(j)
					DeletedOnes.append(j)
				if (data_swe['EPOCH'][j]-Locations[k]).total_seconds() <= 150.0 and (data_swe['EPOCH'][j]-Locations[k]).total_seconds() > 0.0:
					#ajat.append(data_swe['EPOCH'][j])
					ajat.append(j)
					DeletedOnes.append(j)
				j = j + 1

			if np.shape(ajat)[0] != 0:
				j = 0
				TPERP = 0
				TPAR = 0
				n = 0
				MagF = 0
				 
				while j < np.shape(ajat)[0]:
					TPERP = TPERP + (WPERP[ajat[j]]*1000)**2.0
					TPAR = TPAR + (WPAR[ajat[j]]*1000)**2.0
					MagF = MagF + (B[values[ajat[j]]]*10**(-9.0))**2
					n = n + DENSITY[ajat[j]]*10**6
					j = j + 1
				
				TPERP = (TPERP*1.672621898*10**(-27.0))/(1.38064881e-23)
				TPAR = (TPAR*1.672621898*10**(-27.0))/(1.38064881e-23)
				
				Threshold = TPERP/TPAR-1
			
				Beta = 2*(12.566370614e-7)*(1.38064881e-23)
				Beta = Beta/MagF

				BetaPAR = Beta*n*TPAR
				BetaPERP = Beta*n*TPERP

				BetaPAR = BetaPAR/j
				BetaPERP = BetaPERP/j

				ThresHoldi = Threshold - 1/BetaPERP

				#Parameters(day)
				ThresholdMirrorModes.write(str(Location))
				ThresholdMirrorModes.write("	")
				ThresholdMirrorModes.write(str(BetaPAR))
				ThresholdMirrorModes.write("	")
				ThresholdMirrorModes.write(str(BetaPERP))
				ThresholdMirrorModes.write("	")
				ThresholdMirrorModes.write(str(ThresHoldi))
				ThresholdMirrorModes.write("	")
				ThresholdMirrorModes.write(str(j))
				ThresholdMirrorModes.write("\n")
				
			else:
				ThresholdMirrorModes.write("0")
				ThresholdMirrorModes.write("	")
				ThresholdMirrorModes.write("0")
				ThresholdMirrorModes.write("	")
				ThresholdMirrorModes.write("0")
				ThresholdMirrorModes.write("\n")
			k = k + 1
		#####
		#Computing plasma beta and mirror instability of dip-like MMs
		k = 0
		DeletedOnes = []
		while k < np.shape(LocationOfDips)[0]:
			Location = (LocationOfDips[k]-TheBeginning).total_seconds()
			Location = Location/TheLength
			ajat = []
			j = 0
			#eteen ja taakse intervalli			
			while j < np.shape(data_swe['EPOCH'])[0]:
				if (LocationOfDips[k]-data_swe['EPOCH'][j]).total_seconds() <= 150.0 and (LocationOfDips[k]-data_swe['EPOCH'][j]).total_seconds() > 0.0:
					#ajat.append(data_swe['EPOCH'][j])
					ajat.append(j)
					DeletedOnes.append(j)
				if (data_swe['EPOCH'][j]-LocationOfDips[k]).total_seconds() <= 150.0 and (data_swe['EPOCH'][j]-LocationOfDips[k]).total_seconds() > 0.0:
					#ajat.append(data_swe['EPOCH'][j])
					ajat.append(j)
					DeletedOnes.append(j)
				j = j + 1

			if np.shape(ajat)[0] != 0:
				j = 0
				TPERP = 0
				TPAR = 0
				n = 0
				MagF = 0
				 
				while j < np.shape(ajat)[0]:
					TPERP = TPERP + (WPERP[ajat[j]]*1000)**2.0
					TPAR = TPAR + (WPAR[ajat[j]]*1000)**2.0
					MagF = MagF + (B[values[ajat[j]]]*10**(-9.0))**2
					n = n + DENSITY[ajat[j]]*10**6
					j = j + 1
				
				TPERP = (TPERP*1.672621898*10**(-27.0))/(1.38064881e-23)
				TPAR = (TPAR*1.672621898*10**(-27.0))/(1.38064881e-23)
				
				Threshold = TPERP/TPAR-1
			
				Beta = 2*(12.566370614e-7)*(1.38064881e-23)
				Beta = Beta/MagF

				BetaPAR = Beta*n*TPAR
				BetaPERP = Beta*n*TPERP

				BetaPAR = BetaPAR/j
				BetaPERP = BetaPERP/j

				ThresHoldi = Threshold - 1/BetaPERP

				#Parameters(day)
				CmDips.write(str(Location))
				CmDips.write("	")
				CmDips.write(str(BetaPAR))
				CmDips.write("	")
				CmDips.write(str(BetaPERP))
				CmDips.write("	")
				CmDips.write(str(ThresHoldi))
				CmDips.write("	")
				CmDips.write(str(j))
				CmDips.write("\n")
				
			else:
				CmDips.write("0")
				CmDips.write("	")
				CmDips.write("0")
				CmDips.write("	")
				CmDips.write("0")
				CmDips.write("\n")
			k = k + 1
		
		
		#Computing plasma beta and mirror instability of peak-like MMs
		k = 0
		DeletedOnes = []
		while k < np.shape(LocationOfPeaks)[0]:
			Location = (LocationOfPeaks[k]-TheBeginning).total_seconds()
			Location = Location/TheLength
			ajat = []
			j = 0
			#eteen ja taakse intervalli			
			while j < np.shape(data_swe['EPOCH'])[0]:
				if (LocationOfPeaks[k]-data_swe['EPOCH'][j]).total_seconds() <= 150.0 and (LocationOfPeaks[k]-data_swe['EPOCH'][j]).total_seconds() > 0.0:
					#ajat.append(data_swe['EPOCH'][j])
					ajat.append(j)
					DeletedOnes.append(j)
				if (data_swe['EPOCH'][j]-LocationOfPeaks[k]).total_seconds() <= 150.0 and (data_swe['EPOCH'][j]-LocationOfPeaks[k]).total_seconds() > 0.0:
					#ajat.append(data_swe['EPOCH'][j])
					ajat.append(j)
					DeletedOnes.append(j)
				j = j + 1

			if np.shape(ajat)[0] != 0:
				j = 0
				TPERP = 0
				TPAR = 0
				n = 0
				MagF = 0
				 
				while j < np.shape(ajat)[0]:
					TPERP = TPERP + (WPERP[ajat[j]]*1000)**2.0
					TPAR = TPAR + (WPAR[ajat[j]]*1000)**2.0
					MagF = MagF + (B[values[ajat[j]]]*10**(-9.0))**2
					n = n + DENSITY[ajat[j]]*10**6
					j = j + 1
				
				TPERP = (TPERP*1.672621898*10**(-27.0))/(1.38064881e-23)
				TPAR = (TPAR*1.672621898*10**(-27.0))/(1.38064881e-23)
				
				Threshold = TPERP/TPAR-1
			
				Beta = 2*(12.566370614e-7)*(1.38064881e-23)
				Beta = Beta/MagF

				BetaPAR = Beta*n*TPAR
				BetaPERP = Beta*n*TPERP

				BetaPAR = BetaPAR/j
				BetaPERP = BetaPERP/j

				ThresHoldi = Threshold - 1/BetaPERP

				#Parameters(day)
				CmPeaks.write(str(Location))
				CmPeaks.write("	")
				CmPeaks.write(str(BetaPAR))
				CmPeaks.write("	")
				CmPeaks.write(str(BetaPERP))
				CmPeaks.write("	")
				CmPeaks.write(str(ThresHoldi))
				CmPeaks.write("	")
				CmPeaks.write(str(j))
				CmPeaks.write("\n")
				
			else:
				CmPeaks.write("0")
				CmPeaks.write("	")
				CmPeaks.write("0")
				CmPeaks.write("	")
				CmPeaks.write("0")
				CmPeaks.write("\n")
			k = k + 1
		
		
		######
		#Computing plasma beta and mirror instability of in non-MM sheath
		data_swe['P+_DENSITY'] = np.delete(data_swe['P+_DENSITY'], DeletedOnes)
		data_swe['P+_WPERP_NONLIN'] = np.delete(data_swe['P+_WPERP_NONLIN'], DeletedOnes)
		data_swe['P+_WPAR_NONLIN'] = np.delete(data_swe['P+_WPAR_NONLIN'], DeletedOnes)
		index = 0
		while index < np.shape(data_swe['P+_DENSITY'])[0]:
			TheSpotInSheath = (data_swe['EPOCH'][index]-TheBeginning).total_seconds()
			TheSpotInSheath = TheSpotInSheath/TheLength
			TPERP = ((WPERP[index]*1000)**2.0*1.672621898*10**(-27.0))/(1.38064881e-23)
			TPAR  = ((WPAR[index]*1000)**2.0*1.672621898*10**(-27.0))/(1.38064881e-23)
	
			Threshold = TPERP/TPAR-1
		
			Beta = 2*(12.566370614e-7)*(1.38064881e-23)
			Beta = Beta/( (B[values[index]]*10**(-9.0))**2 )

			BetaPAR = Beta*(DENSITY[index]*10**6)*TPAR
			BetaPERP = Beta*(DENSITY[index]*10**6)*TPERP

			#ThresHoldi = Threshold - 0.87/BetaPAR**(0.56)
			ThresHoldi = Threshold - 1/BetaPERP
			#Parameters3(day)		
			ThresholdOnlySheath.write(str(TheSpotInSheath))
			ThresholdOnlySheath.write("	")
			ThresholdOnlySheath.write(str(BetaPAR))
			ThresholdOnlySheath.write("	")
			ThresholdOnlySheath.write(str(BetaPERP))
			ThresholdOnlySheath.write("	")
			ThresholdOnlySheath.write(str(ThresHoldi))
			ThresholdOnlySheath.write("\n")
			index = index + 1

	########################################
	day = day + 1

Results.close()
Modes.close()
MVA_Intervals.close()
ResultsSimplified.close()
MVASimplified.close()
ModesSimplified.close()
TrainLengthsDips.close()
TrainLengthsPeaks.close()
SingleMMs.close()
TrainMMs.close()
SheathFrac.close()
ThresholdWholeSheath.close()
ThresholdMirrorModes.close()
ThresholdOnlySheath.close()
CmSingles.close()
CmMMTrains.close()
CmTrains.close()
Fractional.close()
FractionalDips.close()
FractionalPeaks.close()

DipMMs.close()
PeakMMs.close()

CmPeaks.close()
CmDips.close()
#print SingleSkippaus