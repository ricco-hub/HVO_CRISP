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

  //NORTH L   ************************************************************
  TString northL = "/var/www/html/Wilcox_TILT/data_PLOT/Tilt_L_n.txt"; //percorso
  TGraphErrors *ln = new TGraphErrors(northL);
  ln->SetMarkerColor(kOrange);
  ln->SetLineColor(kOrange);
  ln->SetMarkerStyle(20);
  ln->SetMarkerSize(0.1);
  ln->SetLineWidth(1);
  ln->SetName("Tilt L Northern");
  ln->GetYaxis()->SetTitle("Computed Tilt Angle of the Heliospheric Current Sheet (deg)");
  ln->GetYaxis()->CenterTitle();
  ln->SetTitle("Tilt L Northern");




  //south L    ************************************************************
  TString southL = "/var/www/html/Wilcox_TILT/data_PLOT/Tilt_L_s.txt"; //percorso
  TGraphErrors *ls = new TGraphErrors(southL);
  ls->SetMarkerColor(kRed);
  ls->SetLineColor(kRed);
  ls->SetMarkerStyle(20);
  ls->SetMarkerSize(0.1);
  ls->SetLineWidth(1);
  ls->SetName("Tilt L Southern");
  ls->GetYaxis()->SetTitle("Computed Tilt Angle of the Heliospheric Current Sheet (deg)");
  ls->GetYaxis()->CenterTitle();
  ls->SetTitle("Tilt L Southern");


  //avg L    ************************************************************
  TString avgL = "/var/www/html/Wilcox_TILT/data_PLOT/Tilt_L_av.txt"; //percorso
  TGraphErrors *lavg = new TGraphErrors(avgL);
  lavg->SetMarkerColor(kBlue);
  lavg->SetLineColor(kBlue);
  lavg->SetMarkerStyle(20);
  lavg->SetMarkerSize(0.1);
  lavg->SetLineWidth(1);
  lavg->SetName("Tilt L Average");
  lavg->GetYaxis()->SetTitle("Computed Tilt Angle of the Heliospheric Current Sheet (deg)");
  lavg->GetYaxis()->CenterTitle();
  lavg->SetTitle("Tilt L average");




  //NORTH R   ************************************************************
  TString northR = "/var/www/html/Wilcox_TILT/data_PLOT/Tilt_R_n.txt"; //percorso
  TGraphErrors *rn = new TGraphErrors(northR);
  rn->SetMarkerColor(kViolet+1);
  rn->SetLineColor(kViolet+1);
  rn->SetMarkerStyle(20);
  rn->SetMarkerSize(0.1);
  rn->SetLineWidth(1);
  rn->SetName("Tilt R Northern");
  rn->GetYaxis()->SetTitle("Computed Tilt Angle of the Heliospheric Current Sheet (deg)");
  rn->GetYaxis()->CenterTitle();
  rn->SetTitle("Tilt R Northern");




  //south R    ************************************************************
  TString southR = "/var/www/html/Wilcox_TILT/data_PLOT/Tilt_R_s.txt"; //percorso
  TGraphErrors *rs = new TGraphErrors(southR);
  rs->SetMarkerColor(kGreen+2);
  rs->SetLineColor(kGreen+2);
  rs->SetMarkerStyle(20);
  rs->SetMarkerSize(0.1);
  rs->SetLineWidth(1);
  rs->SetName("Tilt R Southern");
  rs->GetYaxis()->SetTitle("Computed Tilt Angle of the Heliospheric Current Sheet (deg)");
  rs->GetYaxis()->CenterTitle();
  rs->SetTitle("Tilt R Southern");


  //avg R    ************************************************************
  TString avgR = "/var/www/html/Wilcox_TILT/data_PLOT/Tilt_R_av.txt"; //percorso
  TGraphErrors *ravg = new TGraphErrors(avgR);
  ravg->SetMarkerColor(kOrange+7);
  ravg->SetLineColor(kOrange+7);
  ravg->SetMarkerStyle(20);
  ravg->SetMarkerSize(0.1);
  ravg->SetLineWidth(1);
  ravg->SetName("Tilt R Average");
  ravg->GetYaxis()->SetTitle("Computed Tilt Angle of the Heliospheric Current Sheet (deg)");
  ravg->GetYaxis()->CenterTitle();
  ravg->SetTitle("Tilt R average");




  c1->cd();
  vector<char> variable;
  ifstream set;
  string path ="/var/www/html/Wilcox_TILT/Set.txt";


  set.open(path);
  char sx;
  while (!set.eof()) {
    set>>sx>>ws;
    variable.push_back(sx);
  }


  TFile ff("/var/www/html/Wilcox_TILT/TILT.root" , "recreate");
  ff.cd();

  TMultiGraph *mg = new TMultiGraph();
  TLegend *legend = new TLegend(.75,.75,.89,.89);

  for (int i=0; i<variable.size(); i++) {
    switch (variable[i]) {
    case '2':
      mg->Add(ln);
      ln->Write();
      legend->AddEntry(ln," L-Model North","l");
      break;
    case '3':
      mg->Add(ls);
      ls->Write();
      legend->AddEntry(ls,"L-Model South","l");
      break;
    case '1':
      mg->Add(lavg);
      lavg->Write();
      legend->AddEntry(lavg,"L-Model Avg","l");
      break;
    case '5':
      mg->Add(rn);
      rn->Write();
      legend->AddEntry(rn,"R-Model North","l");
      break;
    case '6':
      mg->Add(rs);
      rs->Write();
      legend->AddEntry(rs,"R-Model South","l");
      break;
    case '4':
      mg->Add(ravg);
      ravg->Write();
      legend->AddEntry(ravg,"R-Model Avg","l");
      break;
    }
  }

  mg->SetTitle("Tilt Angle of the Heliospheric Current Sheet");

  mg->Draw("apl");
  //  mg->GetXaxis()->SetRangeUser(xmin,xmax);
  //mg->GetXaxis()->CenterTitle();
  mg->GetYaxis()->CenterTitle();
  // mg->GetXaxis()->SetTitle("year");
  mg->GetYaxis()->SetTitle("Computed Tilt Angle of the Heliospheric Current Sheet (deg)");
  mg->SetName("TILT Graph");

  legend->SetHeader("","C"); // option "C" allows to center the heade
  legend->SetX1NDC(0.01);
  legend->SetX2NDC(0.9);
  legend->Draw();

  c1->Write();
  //  mg->Write();
  ff.Close();

  return 0;
}
