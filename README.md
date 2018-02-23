# dpgByLumiFlag
A simple script to check BAD LS from muon DPG DCS flags

## Install:
```
cmsrel CMSSW_10_0_2
cd CMSSW_10_0_2/src
cmsrel
git clone https://github.com/battibass/dpgByLumiFlag.git
cd dpgByLumiFlag
git clone https://github.com/cms-DQM/certTools
```

## Run:
```
python dpgByLumiFlag.py --minRun=304911 --maxRun=306462

[...] lines from the creation of JSON files

***************************************
List of luminosity losses exlusively due to muon DPGs DCS flags:

DT :
{"306418": [[34, 34]]}

CSC :
{"305044": [[204, 301], [307, 308], [311, 312], [314, 317]],
 "305358": [[232, 232]],
 "305365": [[669, 675]],
 "305366": [[722, 723], [757, 768]],
 "305377": [[1293, 1293], [1384, 1385]],
 "305406": [[395, 400], [521, 527], [536, 539]],
 "305590": [[501, 516]],
 "305636": [[340, 341], [668, 670]],
 "306135": [[1096, 1169]]}

RPC :
{}
***************************************
```
