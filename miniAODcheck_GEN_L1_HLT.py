# Import necessary libraries
import sys
import ROOT
import math
import inspect
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
# Setup ROOT in batch mode
oldargv = sys.argv[:]
sys.argv = ['-b-']
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# Load required ROOT libraries
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.gSystem.Load("libDataFormatsFWLite.so")
ROOT.AutoLibraryLoader.enable()

# Load FWlite python libraries
from DataFormats.FWLite import Handle, Events

# Define muon handler and label
l1Muons  = Handle ("std::BXVector<l1t::Muon>")
l1MuonLabel = ("gmtStage2Digis:Muon")

GenMuons = Handle ("std::vector<reco::GenParticle>")
GenMuonsLabel= ("prunedGenParticles")

L1Trigger = Handle ("BXVector<GlobalAlgBlk>")
L1TriggerLabel = ("gtStage2Digis")

HLTTrigger = Handle("edm::TriggerResults")
HLTTriggerLabel = ("TriggerResults","","HLT")

HLTTriggerMuon=Handle("vector<pat::TriggerObjectStandAlone>")
HLTTriggerMuonLabel=("slimmedPatTrigger")


# Open the ROOT file
input_file_path = "/afs/cern.ch/work/c/cyuan/private/LLP_ATLAS_CMS/CMSSW_13_0_12/src/Condor/condor_Jobs/muon_particle_gun_phi_pi_eta_0.root"
events = Events(input_file_path)

output_file = ROOT.TFile("muon_particle_gun_phi_pi_eta_0_GEN_L1_HLT.root", "RECREATE")
output_tree = ROOT.TTree("muon", "Muon Values")
########################GEN
Genpx = ROOT.std.vector('float')()
Genpy = ROOT.std.vector('float')()
Genpz = ROOT.std.vector('float')()

Genvx = ROOT.std.vector('float')()
Genvy = ROOT.std.vector('float')()
Genvz = ROOT.std.vector('float')()

Gendxy = ROOT.std.vector('float')()
Gendz = ROOT.std.vector('float')()
GenLxy= ROOT.std.vector('float')()

Genpt = ROOT.std.vector('float')()
Geneta = ROOT.std.vector('float')()
Genphi = ROOT.std.vector('float')()

Gensize =ROOT.std.vector('float')()
###########################L1
L1ptUnconstrained = ROOT.std.vector('float')()
L1etaAtVtx = ROOT.std.vector('float')()
L1phiAtVtx = ROOT.std.vector('float')()
L1dxy = ROOT.std.vector('float')()

L1size =ROOT.std.vector('float')()

L1_decision = ROOT.std.vector('bool')()
############################ HLT
HLT_decision = ROOT.std.vector('bool')()

HLTpx = ROOT.std.vector('float')()
HLTpy = ROOT.std.vector('float')()
HLTpz = ROOT.std.vector('float')()

HLTvx = ROOT.std.vector('float')()
HLTvy = ROOT.std.vector('float')()
HLTvz = ROOT.std.vector('float')()

HLTdxy= ROOT.std.vector('float')()
HLTLxy= ROOT.std.vector('float')()

HLTpt = ROOT.std.vector('float')()
HLTeta = ROOT.std.vector('float')()
HLTphi = ROOT.std.vector('float')()

HLTsize = ROOT.std.vector('float')()

####################################################
output_tree.Branch("Genpx", Genpx)
output_tree.Branch("Genpy", Genpy)
output_tree.Branch("Genpz", Genpz)

output_tree.Branch("Genvx", Genvx)
output_tree.Branch("Genvy", Genvy)
output_tree.Branch("Genvz", Genvz)

output_tree.Branch("Gendxy", Gendxy)
output_tree.Branch("Gendz", Gendz)

output_tree.Branch("Genpt", Genpt)
output_tree.Branch("Geneta", Geneta)
output_tree.Branch("Genphi", Genphi)

output_tree.Branch("GenLxy", GenLxy)

output_tree.Branch("Gensize", Gensize)
#####################################################
output_tree.Branch("L1ptUnconstrained", L1ptUnconstrained)
output_tree.Branch("L1etaAtVtx", L1etaAtVtx)
output_tree.Branch("L1phiAtVtx", L1phiAtVtx)
output_tree.Branch("L1_decision", L1_decision)
output_tree.Branch("L1dxy", L1dxy)
output_tree.Branch("L1size", L1size)
#####################################################

output_tree.Branch("HLT_decision", HLT_decision)

output_tree.Branch("HLTpx", HLTpx)
output_tree.Branch("HLTpy", HLTpy)
output_tree.Branch("HLTpz", HLTpz)

output_tree.Branch("HLTvx", HLTvx)
output_tree.Branch("HLTvy", HLTvy)
output_tree.Branch("HLTvz", HLTvz)

output_tree.Branch("HLTLxy", HLTLxy)
output_tree.Branch("HLTdxy", HLTdxy)

output_tree.Branch("HLTpt", HLTpt)
output_tree.Branch("HLTeta", HLTeta)
output_tree.Branch("HLTphi", HLTphi)

output_tree.Branch("HLTsize", HLTsize)


# Loop through events and store pt values in the output file
for iev, event in enumerate(events):

    Genpt.clear()
    Geneta.clear()
    Genphi.clear()

    Genpx.clear()
    Genpy.clear()
    Genpz.clear()

    Genvx.clear()
    Genvy.clear()
    Genvz.clear()

    Gendxy.clear()
    Gendz.clear()
    GenLxy.clear()

    Gensize.clear()
################################################
    L1ptUnconstrained.clear() # Store the pt value in the vector
    L1etaAtVtx.clear()
    L1phiAtVtx.clear()
    L1dxy.clear()
    L1_decision.clear()

    L1size.clear()
###################################################
    HLT_decision.clear()
    HLTpt.clear()
    HLTeta.clear()
    HLTphi.clear()

    HLTpx.clear()
    HLTpy.clear()
    HLTpz.clear()

    HLTvx.clear()
    HLTvy.clear()
    HLTvz.clear()
    HLTdxy.clear()
    HLTLxy.clear()
    HLTsize.clear()

    getHLTDecision=[]

    event.getByLabel(l1MuonLabel, l1Muons)
    event.getByLabel(GenMuonsLabel, GenMuons)
    event.getByLabel(L1TriggerLabel, L1Trigger)
    event.getByLabel(HLTTriggerLabel, HLTTrigger)
    event.getByLabel(HLTTriggerMuonLabel,HLTTriggerMuon)
    
    #print(help(HLTTriggerMuon.product()[0]))
    
    print("##################################################")
    print("event=",iev)
    print("Gensize=", GenMuons.product().size())
    print("L1 size=", l1Muons.product().size())
    print("HLT size=", HLTTriggerMuon.product().size())
    Gensize_= GenMuons.product().size()
    L1size_= l1Muons.product().size()
    HLTsize_= HLTTriggerMuon.product().size()

    Gensize.push_back(Gensize_)
    L1size.push_back(L1size_)
    HLTsize.push_back(HLTsize_)
    
    #names = event.object().triggerNames(HLTTrigger.product())
    #for i in range(HLTTrigger.product().size()):
    #    print("Trigger name=", names.triggerName(i))
    for HLTmuon in HLTTriggerMuon.product():
        #HLTmuon.unpackNamesAndLabels(event.object(), HLTTrigger.product())
        dxy_ = -float(HLTmuon.vx()) * math.sin(HLTmuon.phi()) + float(HLTmuon.vy()) * math.cos(HLTmuon.phi())
        Lxy_=math.sqrt(HLTmuon.vx()*HLTmuon.vx()+HLTmuon.vy()*HLTmuon.vy())
        #print(HLTmuon.pdgId())
        HLTpt.push_back(HLTmuon.pt())
        HLTeta.push_back(HLTmuon.eta())
        HLTphi.push_back(HLTmuon.phi())

        HLTpx.push_back(HLTmuon.px())
        HLTpy.push_back(HLTmuon.py())
        HLTpz.push_back(HLTmuon.pz())

        HLTvx.push_back(HLTmuon.vx())
        HLTvy.push_back(HLTmuon.vy())
        HLTvz.push_back(HLTmuon.vz())

        HLTdxy.push_back(dxy_)
        HLTLxy.push_back(Lxy_)

    for hlttrigger in HLTTrigger.product():
        getHLTDecision.append(hlttrigger.accept())

    HLT_decision.reserve(len(getHLTDecision))
    for hltdecision in getHLTDecision:
        HLT_decision.push_back(hltdecision)

    for l1trigger in L1Trigger.product():
        getAlgoDecisionFinal = [int(l1trigger.getAlgoDecisionFinal(j)) for j in range(len(l1trigger.getAlgoDecisionFinal()))]
        L1_decision.reserve(len(getAlgoDecisionFinal))
        for decision in getAlgoDecisionFinal:
            L1_decision.push_back(decision)



    for gmuon in GenMuons.product():
        dxy_ = -float(gmuon.vx()) * math.sin(gmuon.phi()) + float(gmuon.vy()) * math.cos(gmuon.phi())
        Lxy_=math.sqrt(gmuon.vx()*gmuon.vx()+gmuon.vy()*gmuon.vy())
        dz_= float(gmuon.vz()) - (gmuon.vx() * math.cos(gmuon.phi()) + gmuon.vy() * math.sin(gmuon.phi())) / math.tan(gmuon.theta())

        Genpt.push_back(gmuon.pt())
        Geneta.push_back(gmuon.eta())
        Genphi.push_back(gmuon.phi())

        Genpx.push_back(gmuon.px())
        Genpy.push_back(gmuon.py())
        Genpz.push_back(gmuon.pz())

        Genvx.push_back(gmuon.vx())
        Genvy.push_back(gmuon.vy())
        Genvz.push_back(gmuon.vz())

        Gendxy.push_back(dxy_)
        Gendz.push_back(dz_)

        GenLxy.push_back(Lxy_)
    
    for lmuon in (l1Muons.product()):

        L1ptUnconstrained.push_back(lmuon.ptUnconstrained()) # Store the pt value in the vector
        L1etaAtVtx.push_back(lmuon.etaAtVtx())
        L1phiAtVtx.push_back(lmuon.phiAtVtx())
        L1dxy.push_back(lmuon.hwDXY())
    print("###########################################################")
    output_tree.Fill()
# Write the tree to the output file and close it
output_file.Write()
output_file.Close()