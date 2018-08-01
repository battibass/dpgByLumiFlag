# dpgByLumiFlag
A simple script to check BAD LS from muon DPG DCS flags

## Install:
```
cmsrel CMSSW_10_1_5
cd CMSSW_10_1_5/src
cmsrel
git clone https://github.com/battibass/dpgByLumiFlag.git
cd dpgByLumiFlag
```

## Run:
```
python dpgByLumiFlag.py --minRun=315506 --maxRun=315801

[...] lines from the creation of JSON files

***************************************
List of luminosity losses exclusively due to muon DPGs DCS flags:

DT :
{}

CSC :
{"315713": [[360, 373], [386, 399]]}

RPC :
{}
***************************************
```
