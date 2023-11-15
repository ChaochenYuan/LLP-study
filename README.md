# LLP-study
LLP study, including muon particle gun generate, analysis.

      cmsrel CMSSW_13_0_12
      cd CMSSW_13_0_12/src
      cmsenv
      cmsDriver.py GeneratorInterface/Pythia8Interface/python/Py8PtLxyGun_4tau_cfi.py --fileout file:gensim.root --mc --eventcontent RAWSIM --datatier GEN-SIM --era Run3_2023 --conditions 130X_mcRun3_2023_realistic_v14 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --nThreads 4 --nConcurrentLumis 1 --python_filename GEN-SIM_step_cfg.py -n 1000 --no_exec
      
