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

  /*
  fstream f;
  f.open("/var/www/html/SSN/E.txt",ios::in);
  double xmin,xmax;
  while (!f.eof()) {
    f>>xmin>>xmax>>ws;
  }
  */

  //daily WITH ERROR ************************************************************
  TCanvas *c1 = new TCanvas("c1","titolo Canvas");
  c1->SetFillColor(0);
  c1->cd();

  TString daily_error = "/var/www/html/SSN/data_PLOT/SSN_range.txt"; //percorso

  TGraphErrors *dE = new TGraphErrors(daily_error);
  dE->SetMarkerColor(kOrange);
  dE->SetLineColor(kOrange);
  dE->SetMarkerStyle(20);
  dE->SetMarkerSize(0.1);  
  dE->SetLineWidth(1);  
  dE->SetName("SSN_daily_errors");
  dE->GetYaxis()->SetTitle("SSN");
  dE->GetYaxis()->CenterTitle();
  dE->SetTitle("SSN Daily + errors");

  //daily NO  ERROR *****+++++++++++++++++++++++++++++++++++++++++++++++++++
  TString daily = "/var/www/html/SSN/data_PLOT/SSN_range.txt"; //percorso
  TGraph *d = new TGraph(daily);
  d->SetMarkerColor(kOrange);
  d->SetLineColor(kOrange);
  d->SetMarkerStyle(20);
  d->SetMarkerSize(0.1);
  d->SetLineWidth(2);
  d->SetName("SSN_daily");
  d->GetYaxis()->SetTitle("SSN");
  d->GetYaxis()->CenterTitle();
  d->SetTitle("SSN Daily");
  
         
  //Smoothed 13  with ERROR***********************************************************
  TString smooth13_error = "/var/www/html/SSN/data_PLOT/SSN_Smooth_range.txt"; //percorso
  TGraphErrors *smoE = new TGraphErrors(smooth13_error);
  smoE->SetMarkerColor(kBlue);
  smoE->SetLineColor(kBlue);
  smoE->SetMarkerStyle(20);
  smoE->SetMarkerSize(0.1);
  smoE->SetLineWidth(1);
  smoE->SetName("SSN_smoothed_errors"); 
  smoE->GetYaxis()->SetTitle("SSN");
  smoE->GetYaxis()->CenterTitle();
  smoE->SetTitle("SSN smoothed + Errors");

  //Smoothed 13 NO ERROR*++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  TString smooth = "/var/www/html/SSN/data_PLOT/SSN_Smooth_range.txt"; //percorso
  TGraph *smo = new TGraph(smooth);
  smo->SetMarkerColor(kBlue);
  smo->SetLineColor(kBlue);
  smo->SetMarkerStyle(20);
  smo->SetMarkerSize(0.1);
  smo->SetLineWidth(2);
  smo->SetName("SSN_smoothed");
  smo->GetYaxis()->SetTitle("SSN");
  smo->GetYaxis()->CenterTitle();
  smo->SetTitle("SSN smoothed");

  //Monthly WITH  ERROR***********************************************************************
  TString monthly_error = "/var/www/html/SSN/data_PLOT/SSN_Monthly_range.txt"; //percorso
  TGraphErrors *mE = new TGraphErrors(monthly_error);
  mE->GetYaxis()->SetTitle("SSN");
  mE->GetYaxis()->CenterTitle();
  mE->SetMarkerColor(kRed);
  mE->SetLineColor(kRed);
  mE->SetMarkerStyle(20);
  mE->SetMarkerSize(0.1);
  mE->SetName("SSN_monthly_errors");
  mE->SetTitle("SSN monthly + errors");



  //Monthly NO ERROR ***************************************************************************
  TString monthly = "/var/www/html/SSN/data_PLOT/SSN_Monthly_range.txt"; //percorso
  TGraph *m = new TGraph(monthly);
  m->GetYaxis()->SetTitle("SSN");
  m->GetYaxis()->CenterTitle();
  m->SetMarkerColor(kRed);
  m->SetLineColor(kRed);
  m->SetMarkerStyle(20);
  m->SetLineWidth(2);
  m->SetMarkerSize(0.1);
  m->SetName("SSN_monthly");
  m->SetTitle("SSN monthly");

  c1->cd();
  vector<char> variable;
  ifstream set;
  string path ="/var/www/html/SSN/Set.txt";
  

  set.open(path);
  char sx;
  while (!set.eof()) {
    set>>sx>>ws;
    variable.push_back(sx);
  }


  TFile ff("/var/www/html/SSN/SSN.root" , "recreate");
  ff.cd();

  TMultiGraph *mg = new TMultiGraph();
  TLegend *legend = new TLegend(.75,.75,.89,.89);

  for (int i=0; i<variable.size(); i++) {
    switch (variable[i]) {
    case '1':
      mg->Add(d);
      d->Write();
      legend->AddEntry(d,"SSN Daily","l");
      break;
    case '2':
      mg->Add(dE);
      dE->Write();      
      legend->AddEntry(dE,"SSN Daily","l");
      break;
    case '3':
      mg->Add(m);
      m->Write();      
      legend->AddEntry(m,"SSN Monthly","l");
      break;
    case '4':
      mg->Add(mE);
      mE->Write();
      legend->AddEntry(mE,"SSN Monthly","l");
      break;
    case '5':
      mg->Add(smo);
      smo->Write();
      legend->AddEntry(smo,"SSN Smoothed ","l");
      break;
    case '6':
      mg->Add(smoE);
      smoE->Write();
      legend->AddEntry(smoE,"SSN Smoothed","l");
      break;
    }
  }

  mg->SetTitle("SunSpot Number");

  mg->Draw("apl");
  //  mg->GetXaxis()->SetRangeUser(xmin,xmax);
  //mg->GetXaxis()->CenterTitle();
  mg->GetYaxis()->CenterTitle();
  // mg->GetXaxis()->SetTitle("year");
  mg->GetYaxis()->SetTitle("SSN");
  mg->SetName("SSN Graph");

  legend->SetHeader("","C"); // option "C" allows to center the heade         
  legend->SetX1NDC(0.01);
  legend->SetX2NDC(0.9);
  legend->Draw();

  c1->Write();
  //  mg->Write();
  ff.Close();

  return 0;
}
