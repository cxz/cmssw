import FWCore.ParameterSet.Config as cms

# File: CaloMET.cfi
# Author: B. Scurlock & R. Remington
# Date: 03.04.2008
#
# Fill validation histograms for MET
from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer
metAnalyzer = DQMEDAnalyzer(
    "METTester",
    InputMETLabel = cms.InputTag("caloMet"),
    METType = cms.untracked.string("calo"),
    PrimaryVertices = cms.InputTag("offlinePrimaryVertices")
    )

#metHOAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("metHO")
#    )
#
#metNoHFAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("metNoHF")
#    )
#
#metNoHFHOAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("metNoHFHO")
#    )
#
#metOptAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("metOpt")
#    )
#
#metOptHOAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("metOptHO")
#    )
#
#metOptNoHFAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("metOptNoHF")
#    )
#
#metOptNoHFHOAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("metOptNoHFHO")
#    )

pfMetAnalyzer = DQMEDAnalyzer(
   "METTester",
   InputMETLabel = cms.InputTag("pfMet"),
   METType = cms.untracked.string("pf"),
   PrimaryVertices = cms.InputTag("offlinePrimaryVertices")
   ) 

#tcMetAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("tcMet"),
#    InputCaloMETLabel = cms.InputTag("caloMet"),
#    InputTrackLabel = cms.InputTag("generalTracks"),
#    InputMuonLabel = cms.InputTag("muons"),
#    InputElectronLabel = cms.InputTag("gedGsfElectrons"),
#    InputBeamSpotLabel = cms.InputTag("offlineBeamSpot"),
#    sample = cms.untracked.string('NULL'),
#    minhits = cms.int32(6),
#    maxd0 = cms.double(0.1),
#    maxchi2 = cms.double(5),
#    maxeta = cms.double(2.65),
#    maxpt = cms.double(100.),
#    maxPtErr = cms.double(0.2),
#    trkQuality = cms.vint32(2),
#    trkAlgos = cms.vint32(),
#    METType = cms.untracked.string("tc")
#    ) 

#corMetGlobalMuonsAnalyzer = DQMEDAnalyzer(
#    "METTester",
#     OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("caloMetM"),
#    METType = cms.untracked.string("cor")
#    ) 


#genMptTrueAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("genMptTrue"),
#    )

genMetTrueAnalyzer = DQMEDAnalyzer(
    "METTester",
    InputMETLabel = cms.InputTag("genMetTrue"),
    METType = cms.untracked.string("gen"),
    PrimaryVertices = cms.InputTag("offlinePrimaryVertices")
    )

#genMetCaloAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("genMetCalo")
#    )
#
#genMptCaloAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("genMptCalo")
#    )
#
#
#genMetCaloAndNonPromptAnalyzer = DQMEDAnalyzer(
#    "METTester",
#    OutputFile = cms.untracked.string(''),
#    InputMETLabel = cms.InputTag("genMetCaloAndNonPrompt")
#    )
pfType0CorrectedMetAnalyzer = DQMEDAnalyzer(
   "METTester",
   InputMETLabel = cms.InputTag("pfMetT0pc"),
   METType = cms.untracked.string("pf"),
   PrimaryVertices = cms.InputTag("offlinePrimaryVertices")
   )
pfType1CorrectedMetAnalyzer = DQMEDAnalyzer(
   "METTester",
   InputMETLabel = cms.InputTag("PfMetT1"),
   METType = cms.untracked.string("pf"),
   PrimaryVertices = cms.InputTag("offlinePrimaryVertices")
   )
pfType01CorrectedMetAnalyzer = DQMEDAnalyzer(
   "METTester",
   InputMETLabel = cms.InputTag("PfMetT0pcT1"),
   METType = cms.untracked.string("pf"),
   PrimaryVertices = cms.InputTag("offlinePrimaryVertices")
   )
pfType1CorrectedMetAnalyzerMiniAOD = DQMEDAnalyzer(
   "METTester",
   InputMETLabel = cms.InputTag("slimmedMETs"),
   METType = cms.untracked.string("miniaod"),
   PrimaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices")
   )

pfPuppiMetAnalyzerMiniAOD = DQMEDAnalyzer(
   "METTester",
   InputMETLabel = cms.InputTag("slimmedMETsPuppi"),
   METType = cms.untracked.string("miniaod"),
   PrimaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices")
   )
