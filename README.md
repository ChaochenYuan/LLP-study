# LLP-study
LLP study, including muon particle gun generate, analysis.

      cmsrel CMSSW_13_0_12
      cd CMSSW_13_0_12/src
      cmsenv
      cmsDriver.py GeneratorInterface/Pythia8Interface/python/Py8PtLxyGun_4tau_cfi.py --fileout file:gensim.root --mc --eventcontent RAWSIM --datatier GEN-SIM --era Run3_2023 --conditions 130X_mcRun3_2023_realistic_v14 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --nThreads 4 --nConcurrentLumis 1 --python_filename GEN-SIM_step_cfg.py -n 1000 --no_exec
after that you will get GEN-SIM_step_cfg.py, for our LLP study, we need to modify the GEN-SIM_step_cfg.py -> Muon_Particle_Gun.py and Py8PtAndLxyGun.cc(in CMSSW_13_0_12/src/GeneratorInterface/Pythia8Interface/plugins) file
      
continue with the full CMS simulation chain

      cmsRun $your directory/CMSSW_13_0_12/src/Muon_Particle_Gun.py $OUTPUT $ramdomseed $RUNNUMBER $nevent
      
      INPUT_STEP2=$OUTPUT
      
      cmsDriver.py $OUTPUT_STEP2 --filein file:$INPUT_STEP2 -s DIGI,L1,DIGI2RAW,HLT:2023v12 --conditions 130X_mcRun3_2023_realistic_v14 --datatier GEN-SIM-DIGI-RAW -n $nevent --eventcontent FEVTDEBUGHLT --geometry DB:Extended --era Run3_2023
      EXTENSION2='_DIGI_L1_DIGI2RAW_HLT'
      
      INPUT_STEP3=$OUTPUT_STEP2$EXTENSION2.root
      
      cmsDriver.py $OUTPUT_STEP3 --filein file:$INPUT_STEP3  -s RAW2DIGI,L1Reco,RECO,RECOSIM,PAT,VALIDATION:@standardValidationNoHLT+@miniAODValidation,DQM:@standardDQMFakeHLT+@miniAODDQM --conditions 130X_mcRun3_2023_realistic_v14 --datatier GEN-SIM-RECO,AODSIM,MINIAODSIM,DQMIO -n $nevent --eventcontent RECOSIM,AODSIM,MINIAODSIM,DQM --geometry DB:Extended --era Run3_2023

after that, you will get the miniAOD file together with AOD file, DQM file, we will work on the miniAOD file.
      
      python3 miniAODcheck_GEN_L1_HLT.py
this will creat a root file with information of Gen level, L1 level and HLT level
to make the plots, just need to 

      python3 plot.py
