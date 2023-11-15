import ROOT
import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep

# Open the ROOT file
root_file = ROOT.TFile("muon_particle_gun_phi_pi_eta_0_GEN_L1_HLT.root", "READ")

def plot_GEN_L1_triggered(var,bins,low,high):
# Access the TTree
    tree = root_file.Get("muon")

# Access branches 'a' and 'b'
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

###################################################
    tree.SetBranchAddress("Genpx", Genpx)
    tree.SetBranchAddress("Genpy", Genpy)
    tree.SetBranchAddress("Genpz", Genpz)

    tree.SetBranchAddress("Genvx", Genvx)
    tree.SetBranchAddress("Genvy", Genvy)
    tree.SetBranchAddress("Genvz", Genvz)

    tree.SetBranchAddress("Gendxy", Gendxy)
    tree.SetBranchAddress("Gendz", Gendz)
    tree.SetBranchAddress("GenLxy", GenLxy)

    tree.SetBranchAddress("Genpt", Genpt)
    tree.SetBranchAddress("Geneta", Geneta)
    tree.SetBranchAddress("Genphi", Genphi)

    tree.SetBranchAddress("Gensize", Gensize)
##############################################
    tree.SetBranchAddress("L1ptUnconstrained", L1ptUnconstrained)
    tree.SetBranchAddress("L1etaAtVtx", L1etaAtVtx)
    tree.SetBranchAddress("L1phiAtVtx", L1phiAtVtx)
    tree.SetBranchAddress("L1dxy", L1dxy)
    tree.SetBranchAddress("L1size", L1size)
    tree.SetBranchAddress("L1_decision", L1_decision)
#################################################
    tree.SetBranchAddress("HLTpx", HLTpx)
    tree.SetBranchAddress("HLTpy", HLTpy)
    tree.SetBranchAddress("HLTpz", HLTpz)

    tree.SetBranchAddress("HLTvx", HLTvx)
    tree.SetBranchAddress("HLTvy", HLTvy)
    tree.SetBranchAddress("HLTvz", HLTvz)

    tree.SetBranchAddress("HLTdxy", HLTdxy)
    tree.SetBranchAddress("HLTLxy", HLTLxy)

    tree.SetBranchAddress("HLTpt", HLTpt)
    tree.SetBranchAddress("HLTeta", HLTeta)
    tree.SetBranchAddress("HLTphi", HLTphi)

    tree.SetBranchAddress("HLT_decision", HLT_decision)
###############################################

# Create lists to store values for plotting
    var_to_plot=[]
############################################
# Loop over entries in the TTree
    for i in range(tree.GetEntries()):
        j_index=[]
        tree.GetEntry(i)
        L1_triggered=False
        for j in range(len(L1_decision)):
            if L1_decision[j] == 1:  # Condition: b > 1
                j_index.append(j)
                if len(j_index)> 6:
                    L1_triggered=True
        if L1_triggered:
            var_to_plot.append(locals()[var][0])
    plt.hist(var_to_plot, bins=bins, range=(low, high), color='blue', label=var)
    plt.xlabel(var)
    plt.ylabel('Entries')
    plt.title(var)
    hep.cms.label()
    plt.grid(True)
    plt.savefig(var+".pdf")
    plt.clf()

#######################################################################################
plot_GEN_L1_triggered("Genvx",100,0,800)
plot_GEN_L1_triggered("Genvy",100,-800,800)
plot_GEN_L1_triggered("Genvz",100,-1100,1100)

plot_GEN_L1_triggered("Genpt",100,0,600)
#######################################################################################
# Close the ROOT file

root_file.Close()
