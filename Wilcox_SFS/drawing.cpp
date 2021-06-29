#include <iostream>
#include <iomanip>
#include <TAxis.h>
#include <TGraphErrors.h>
#include <TGraph.h>
#include <TH1D.h>
#include <TMultiGraph.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TApplication.h>
#include <TStyle.h>
#include <TPad.h>
#include <TLegend.h>
#include <TROOT.h>
#include <TColor.h>
#include <TVirtualPad.h>
#include <fstream>
using namespace std;
//---------------------------------------------------------------------------
int main()
{

  TCanvas *c1 = new TCanvas("c1","titolo Canvas");
  c1->SetFillColor(0);
  c1->cd();

  //NORTH  ************************************************************
  TString north = "/var/www/html/Wilcox_SFS/data_PLOT/North_range.txt"; //percorso
  TGraphErrors *n = new TGraphErrors(north);
  n->SetMarkerColor(kGreen);
  n->SetLineColor(kGreen);
  n->SetMarkerStyle(20);
  n->SetMarkerSize(0.1);
  n->SetLineWidth(1);
  n->SetName("North");
  n->GetYaxis()->SetTitle("Sun's Polar Field strength");
  n->GetYaxis()->CenterTitle();
  n->SetTitle("North");

    
  //NORTH 20 Hz  ************************************************************
  TString northf = "/var/www/html/Wilcox_SFS/data_PLOT/North_F_range.txt"; //percorso
  TGraphErrors *nf = new TGraphErrors(northf);
  nf->SetMarkerColor(kGreen);
  nf->SetLineStyle(2);
  nf->SetLineColor(kGreen);
  nf->SetMarkerStyle(20);
  nf->SetMarkerSize(0.1);
  nf->SetLineWidth(4);
  nf->SetName("North_20 nHz");
  nf->GetYaxis()->SetTitle("Sun's Polar Field strength");
  nf->GetYaxis()->CenterTitle();
  nf->SetTitle("North 20 nHz");
    
    
  //SOUTH  ************************************************************
  TString south = "/var/www/html/Wilcox_SFS/data_PLOT/South_range.txt"; //percorso
  TGraphErrors *s = new TGraphErrors(south);
  s->SetMarkerColor(kRed);
  s->SetLineColor(kRed);
  s->SetMarkerStyle(20);
  s->SetMarkerSize(0.1);
  s->SetLineWidth(1);
  s->SetName("South");
  s->GetYaxis()->SetTitle("Sun's Polar Field strength");
  s->GetYaxis()->CenterTitle();
  s->SetTitle("South");
    
    
  //SOUTH  20 hz ************************************************************
  TString southf = "/var/www/html/Wilcox_SFS/data_PLOT/South_F_range.txt"; //percorso
  TGraphErrors *sf = new TGraphErrors(southf);
  sf->SetMarkerColor(kRed);
  sf->SetLineColor(kRed);
  sf->SetMarkerStyle(20);
  sf->SetMarkerSize(0.1);
  sf->SetLineWidth(4);
  sf->SetLineStyle(2);
  sf->SetName("South 20 nHz");
  sf->GetYaxis()->SetTitle("Sun's Polar Field strength");
  sf->GetYaxis()->CenterTitle();
  sf->SetTitle("South 20 nHz");
    
    
  //avg  ************************************************************
  TString avg = "/var/www/html/Wilcox_SFS/data_PLOT/Avg_range.txt"; //percorso
  TGraphErrors *a = new TGraphErrors(avg);
  a->SetMarkerColor(kBlue);
  a->SetLineColor(kBlue);
  a->SetMarkerStyle(20);
  a->SetMarkerSize(0.1);
  a->SetLineWidth(1);
  a->SetName("Average");
  a->GetYaxis()->SetTitle("Sun's Polar Field strength");
    a->GetYaxis()->CenterTitle();
    a->SetTitle("Average");
    
    
    
    
    
    //avg 20 hz ************************************************************
    TString avgf = "/var/www/html/Wilcox_SFS/data_PLOT/Avg_F_range.txt"; //percorso
    TGraphErrors *af = new TGraphErrors(avgf);
    af->SetMarkerColor(kBlue);
    af->SetLineColor(kBlue);
    af->SetMarkerStyle(20);
    af->SetMarkerSize(0.1);
    af->SetLineWidth(4); af->SetLineStyle(2);
    af->SetName("Average 20 nHz");
    af->GetYaxis()->SetTitle("Sun's Polar Field strength");
    af->GetYaxis()->CenterTitle();
    af->SetTitle("Average 20 nHz");
    
    


  c1->cd();
  vector<char> variable;
  ifstream set;
  string path ="/var/www/html/Wilcox_SFS/Set.txt";
  

  set.open(path);
  char sx;
  while (!set.eof()) {
    set>>sx>>ws;
    variable.push_back(sx);
  }


  TFile ff("/var/www/html/Wilcox_SFS/SFS.root" , "recreate");
  ff.cd();

  TMultiGraph *mg = new TMultiGraph();
  TLegend *legend = new TLegend(.75,.75,.89,.89);

  for (int i=0; i<variable.size(); i++) {
    switch (variable[i]) {
    case '1':
      mg->Add(n);
      n->Write();
      legend->AddEntry(n,"North","l");
      break;
    case '2':
      mg->Add(nf);
      nf->Write();
      legend->AddEntry(nf,"North 20 nHz","l");
      break;
    case '3':
      mg->Add(s);
      s->Write();
      legend->AddEntry(s,"South","l");
      break;
    case '4':
      mg->Add(sf);
      sf->Write();
      legend->AddEntry(sf,"South 20 nHz","l");
      break;
    case '5':
      mg->Add(a);
      a->Write();
      legend->AddEntry(a,"Average","l");
      break;
    case '6':
      mg->Add(af);
      af->Write();
      legend->AddEntry(af,"Average 20 nHz","l");
      break;
    }
  }

  mg->SetTitle("Sun's Polar Field strength");

  mg->Draw("apl");
  //  mg->GetXaxis()->SetRangeUser(xmin,xmax);
  //mg->GetXaxis()->CenterTitle();
  mg->GetYaxis()->CenterTitle();
  // mg->GetXaxis()->SetTitle("year");
  mg->GetYaxis()->SetTitle("Sun's Polar Field strength (#mu T)");
  mg->SetName("SPFS Graph");

  legend->SetHeader("","C"); // option "C" allows to center the heade         
  legend->SetX1NDC(0.01);
  legend->SetX2NDC(0.9);
  legend->Draw();

  c1->Write();
  //  mg->Write();
  ff.Close();

  return 0;
}
