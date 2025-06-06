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

  TCanvas *c1 = new TCanvas("c1","c1");
  c1->SetFillColor(0);
  c1->cd();

  //selected stations
  vector<string> variable;
  ifstream set;
  string path ="/var/www/html/Forecast/NM_Set.txt";
    

  set.open(path);
  string sx;
  while (!set.eof()) {
    set>>sx>>ws;
    variable.push_back(sx);
  }

  //energy set
  vector<string> energy_ref;
  ifstream ref;
  string path_E ="/var/www/html/Forecast/E.txt";


  ref.open(path_E);
  string eR;
  while (!ref.eof()) {
    ref>>eR>>ws;
  energy_ref.push_back(eR);
  }

  TString E_ref= energy_ref[0];
  cout<<energy_ref[0]<<endl;

  //phi graph

  TFile ff("/var/www/html/Forecast/ForceFieldPHI.root" , "recreate");
  ff.cd();
  TMultiGraph *mg = new TMultiGraph();
  TLegend *legend = new TLegend(.75,.75,.89,.89);
    
  for (int i=0; i<variable.size(); i++) {
    //selected stations NM  ************************************************************
    TString north = "/var/www/html/Forecast/data_PLOT/"+variable[i]+"PHI.txt"; //percorso
    TGraph *n = new TGraph(north);
    cout<<north<<endl;
    if(variable[i] == "OULU"){n->SetMarkerColor(kOrange);
      n->SetLineColor(kOrange);}
    
    if(variable[i] == "NEWK"){n->SetMarkerColor(kBlue);
      n->SetLineColor(kBlue);}

    if(variable[i] == "APTY"){n->SetMarkerColor(kGreen+2);
      n->SetLineColor(kGreen+2);}

    if(variable[i] == "JUNG"){n->SetMarkerColor(kRed);
      n->SetLineColor(kRed);}

    if(variable[i] == "HRMS"){n->SetMarkerColor(kCyan-7);
      n->SetLineColor(kCyan-7);}

    if(variable[i] == "MOSC"){n->SetMarkerColor(kViolet);
      n->SetLineColor(kViolet);}
    if(variable[i] == "MXCO"){n->SetMarkerColor(kBlack);
      n->SetLineColor(kBlack);}

    n->SetMarkerStyle(20);
    n->SetMarkerSize(0.1);
    n->SetLineWidth(1);
    TString name = variable[i];
    n->SetName(name);
    n->GetYaxis()->SetTitle("#phi [MV]");
    n->GetYaxis()->CenterTitle();
    n->SetTitle("#phi modulation potential");
  
    mg->Add(n);
    n->Write();
    legend->AddEntry(n,name,"l");
    
  }


  mg->SetTitle("#phi modulation potential");

  mg->Draw("apl");
  mg->GetYaxis()->CenterTitle();
  mg->GetYaxis()->SetTitle("#phi [MV]");
  mg->SetName("phi");

  legend->SetHeader("","C"); // option "C" allows to center the heade         
  legend->SetX1NDC(0.01);
  legend->SetX2NDC(0.9);
  legend->Draw();

  c1->Write();
  //  mg->Write();
  ff.Close();



  //JMOD flux
  TCanvas *c2= new TCanvas("c2","c2");
  c2->SetFillColor(0);
  c2->cd();
  TFile fj("/var/www/html/Forecast/ForceFieldJMOD.root" , "recreate");
  fj.cd();
  TMultiGraph *mgj = new TMultiGraph();
  TLegend *legendj = new TLegend(.75,.75,.89,.89);

  for (int i=0; i<variable.size(); i++) {
    //selected stations NM  ************************************************************                                                                           
    TString north = "/var/www/html/Forecast/data_PLOT/JMOD"+variable[i]+".txt"; //percorso  

     
    TGraph *n = new TGraph(north);

    if(variable[i] == "OULU"){n->SetMarkerColor(kOrange);
      n->SetLineColor(kOrange);}

    if(variable[i] == "NEWK"){n->SetMarkerColor(kBlue);
      n->SetLineColor(kBlue);}

    if(variable[i] == "APTY"){n->SetMarkerColor(kGreen+2);
      n->SetLineColor(kGreen+2);}

    if(variable[i] == "JUNG"){n->SetMarkerColor(kRed);
      n->SetLineColor(kRed);}

    if(variable[i] == "HRMS"){n->SetMarkerColor(kCyan-7);
      n->SetLineColor(kCyan-7);}

    if(variable[i] == "MOSC"){n->SetMarkerColor(kViolet);
      n->SetLineColor(kViolet);}
    if(variable[i] == "MXCO"){n->SetMarkerColor(kBlack);
      n->SetLineColor(kBlack);}

    n->SetMarkerStyle(20);
    n->SetMarkerSize(0.1);
    n->SetLineWidth(1);
    TString name = variable[i];
    n->SetName(name);
    n->GetYaxis()->SetTitle("J modulated flux [ GeV^{ -1} m^{ -2} s^{ -1} sr^{ -1} ]");
    n->GetYaxis()->CenterTitle();
    n->SetTitle("J modulation potential");

    mgj->Add(n);
    n->Write();
    legendj->AddEntry(n,name,"l");

  }


  mgj->SetTitle("J modulated flux: E = " + E_ref+ " GeV");

  mgj->Draw("apl");
  mgj->GetYaxis()->CenterTitle();
  mgj->GetYaxis()->SetTitle("J [ GeV^{ -1} m^{ -2} s^{ -1} sr^{ -1} ]");
  mgj->SetName("phi");

  legendj->SetHeader("","C"); // option "C" allows to center the heade                                                                                              
  legendj->SetX1NDC(0.01);
  legendj->SetX2NDC(0.9);
  legendj->Draw();

  c2->Write();
  //  mg->Write();                                                                                                                                                 
  fj.Close();



  return 0;
}
