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

  //speed

  TString speed = "/var/www/html/WIND/data_PLOT/Speed_range.txt"; //percorso
  TGraph *sp = new TGraph(speed);
  sp->SetMarkerColor(kBlue);
  sp->SetLineColor(kBlue);
  sp->SetMarkerStyle(20);
  sp->SetMarkerSize(0.1);
  sp->SetLineWidth(2);
  sp->SetName("Solar_wind_Speed");
  sp->GetYaxis()->SetTitle("Solar Wind Speed");
  sp->GetYaxis()->CenterTitle();
  sp->SetTitle("Solar Wind Speed");



  //proton density

  TString proton_density = "/var/www/html/WIND/data_PLOT/Proton_range.txt"; //percorso
  TGraph *pd = new TGraph(proton_density);
  pd->SetMarkerColor(kOrange);
  pd->SetLineColor(kOrange);
  pd->SetMarkerStyle(20);
  pd->SetMarkerSize(0.1);
  pd->SetLineWidth(2);
  pd->SetName("Proton_Density");
  pd->GetYaxis()->SetTitle("Proton Density");
  pd->GetYaxis()->CenterTitle();
  pd->SetTitle("Proton Density");


  vector<char> variable;
  ifstream set;
  string path ="/var/www/html/WIND/Set.txt";


  set.open(path);
  char sx;
  while (!set.eof()) {
    set>>sx>>ws;
    variable.push_back(sx);
  }


  TFile ff("/var/www/html/WIND/SolarWind.root" , "recreate");
  ff.cd();



  for (int i=0; i<variable.size(); i++) {
    switch (variable[i]) {
    case '1':
      sp->Write();
      break;
    case '2':
      pd->Write();
      break;
    }


  return 0;
}
