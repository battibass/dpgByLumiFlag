#!/usr/bin/python

import argparse, sys, os
from subprocess import call

template_file_name = "cert_config_template.cfg"

min_run_tag   = "MIN_RUN"
max_run_tag   = "MAX_RUN"
flag_tag      = "DCS_FLAGS"
dir_tag       = "DIR_NAME"
lab_tag       = "TAG"

cert_script = "certTools/dataCert.py"

all_good_flags = "Bpix,Fpix,Tibtid,TecM,TecP,Tob,Ebm,Ebp,EeM,EeP,EsM,EsP,HbheA,HbheB,HbheC,Hf,Ho,Dtm,Dtp,Dt0,CscM,CscP,Rpc"
no_dt_flags    = "Bpix,Fpix,Tibtid,TecM,TecP,Tob,Ebm,Ebp,EeM,EeP,EsM,EsP,HbheA,HbheB,HbheC,Hf,Ho,CscM,CscP,Rpc"
no_csc_flags   = "Bpix,Fpix,Tibtid,TecM,TecP,Tob,Ebm,Ebp,EeM,EeP,EsM,EsP,HbheA,HbheB,HbheC,Hf,Ho,Dtm,Dtp,Dt0,Rpc"
no_rpc_flags   = "Bpix,Fpix,Tibtid,TecM,TecP,Tob,Ebm,Ebp,EeM,EeP,EsM,EsP,HbheA,HbheB,HbheC,Hf,Ho,CscM,CscP,Dtm,Dtp,Dt0"

flags_map = {"all" : all_good_flags, "noDT" : no_dt_flags, "noCSC" : no_csc_flags, "noRPC" : no_rpc_flags}

json_to_compare = ["noDT", "noCSC", "noRPC"]

parser = argparse.ArgumentParser(description='[dpgByLumiFlag] configuration parameters :')

parser.add_argument('--minRun', type=int, required=True,  help='min run number')
parser.add_argument('--maxRun', type=int, required=True,  help='max run number')

args = parser.parse_args()

dir_name = "cert_" + str(args.minRun) + "_" + str(args.maxRun) 

if not os.path.exists(dir_name):
    os.makedirs(dir_name)

for tag,flags in flags_map.iteritems() :

    template_file = file(template_file_name, "r")

    output_file_name = dir_name + "/cert_config_" + tag +".cfg"

    output_file = file(output_file_name, "w")

    for line in template_file.readlines() :

        output_line = line
        
        output_line = output_line.replace(min_run_tag,str(args.minRun))
        output_line = output_line.replace(max_run_tag,str(args.maxRun))
        output_line = output_line.replace(dir_tag,dir_name)
        output_line = output_line.replace(flag_tag,flags)
        output_line = output_line.replace(lab_tag,tag)

        output_file.write(output_line)

    template_file.close()
    output_file.close()

    call(["python", cert_script, output_file_name])


print "\n\n\n***************************************"
print "List of luminosity losses exclusively due to muon DPGs DCS flags:"
all_file_name = dir_name + "/cert_" +str(args.minRun) + "-" + str(args.maxRun)+ "_all.json"

for tag in json_to_compare :
    print "\n" + tag.strip("no") + " :"
    dpg_file_name = dir_name + "/cert_" +str(args.minRun) + "-" + str(args.maxRun)+ "_" + tag +".json"

    call(["compareJSON.py", "--sub",  dpg_file_name, all_file_name])

print "***************************************"
    
    

