import ROOT

f = ROOT.TFile.Open("CMS-HGG_sigfit_packaged_SR1.root")
w = f.Get("wsig_13TeV")

procs=["ggHHkl0kt1", "ggHHkl1kt1", "ggHHkl2p45kt1", "ggHHkl5kt1"]
years = [ '2016', '2017', '2018' ]

for year in years:
	for proc in procs:
		print "Now processing: " + proc + " for year " + year
		norm = w.obj("hggpdfsmrel_"+proc+"_"+year+"_SR1_13TeV_norm")
		xs = w.obj("fxs_"+proc+"_13TeV")
		br = w.obj("fbr_13TeV")
		ea = w.obj("fea_"+proc+"_"+year+"_SR1_13TeV")
		rate = w.obj("rate_"+proc+"_"+year+"_SR1_13TeV")
		
		print ("norm: {}".format(norm.getVal()))
		print ("xs: {}".format(xs.getVal()))
		print ("br: {}".format(br.getVal()))
		print ("ea: {}".format(ea.getVal()))
		print ("rate: {}".format(rate.getVal()))

	print "\n \n \n"
