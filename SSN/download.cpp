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
#include <TROOT.h>
#include <iostream>
#include <fstream>
#include <TColor.h>
#include <TVirtualPad.h>
#include <TBufferJSON.h>
#include <THttpServer.h>
#include <fstream>
using namespace std;
//------------------------------------------------------------------------------
int main()
{
  //daily WITH ERROR ************************************************************
  TCanvas *c1 = new TCanvas("c1","titolo Canvas");
  c1->SetFillColor(19);
  c1->cd();

  TString daily_error = "/var/www/html/SSN/SSNPLOT.txt"; //percorso
  TGraphErrors *dE = new TGraphErrors(daily_error);
  dE->GetXaxis()->SetTitle("year");
  dE->GetYaxis()->SetTitle("SunSpot Number");
  dE->GetXaxis()->CenterTitle();
  dE->GetYaxis()->CenterTitle();
  dE->SetMarkerColor(9);
  dE->SetMarkerStyle(1);
  dE->SetTitle("Solar Spot Number");
  dE->SetName("Graph with Errors");
  dE->Draw("ap");

  //daily NO  ERROR *****+++++++++++++++++++++++++++++++++++++++++++++++++++
  TString daily = "/var/www/html/SSN/SSNLINE.txt"; //percorso
  TGraph *d = new TGraph(daily);
  d->GetXaxis()->SetTitle("year");
  d->GetYaxis()->SetTitle("SunSpot Number");
  d->SetName("Graph");
  d->GetXaxis()->CenterTitle();
  d->GetYaxis()->CenterTitle();
  d->SetMarkerColor(9); 
  d->SetLineColor(9);
  d->SetMarkerStyle(1);
  d->SetTitle("SSN(t)");
  d->Draw("APL");
         
  //Smoothed 13  with ERROR***********************************************************
  TString smooth13_error = "/var/www/html/SolarSmoothed/SSN_13PLOT.txt"; //percorso
  TGraphErrors *smoE = new TGraphErrors(smooth13_error);
  smoE->GetXaxis()->SetTitle("year");
  smoE->GetYaxis()->SetTitle("SSN");
  smoE->GetXaxis()->CenterTitle();
  smoE->GetYaxis()->CenterTitle();
  smoE->SetFillColor(kMagenta-7);
  smoE->SetMarkerColor(kOrange+7);
  smoE->SetFillStyle(3002);
  smoE->SetLineColor(kPink-6);
  smoE->SetLineWidth(4);
  smoE->GetYaxis()->SetRangeUser(0.1,1000);
  smoE->Draw("a4l");
  smoE->SetTitle("Solar Spot Number Smoothed ");    

  //Smoothed 13 NO ERROR*++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  TString smooth = "/var/www/html/SolarSmoothed/SSN_13PLOT.txt"; //percorso
  TGraphErrors *smo = new TGraphErrors(nomefile);
  smo->GetXaxis()->SetTitle("year");
  smo->GetYaxis()->SetTitle("SSN");
  smo->GetXaxis()->CenterTitle();
  smo->GetYaxis()->CenterTitle();
  smo->SetFillColor(kMagenta-7);
  smo->SetMarkerColor(kOrange+7);
  smo->SetFillStyle(3002);
  smo->SetLineColor(kPink-6);
  smo->SetLineWidth(4);
  smo->GetYaxis()->SetRangeUser(0.1,1000);
  smo->Draw("a4l");
  smo->SetTitle("Solar Spot Number Smoothed ");



  //Monthly WITH  ERROR***********************************************************************
  TString monthly_error = "/var/www/html/SolarSmoothed/SSN_MonthlyPLOT.txt"; //percorso
  TGraphErrors *mE = new TGraphErrors(monthly_error);
  mE->GetXaxis()->SetTitle("year");
  mE->GetYaxis()->SetTitle("SSN");
  mE->GetXaxis()->CenterTitle();
  mE->GetYaxis()->CenterTitle();
  mE->SetMarkerColor(kAzure+2);
  mE->SetLineColor(kAzure+2);
  mE->SetMarkerStyle(20);
  mE->SetMarkerSize(0.3);
  mE->GetYaxis()->SetRangeUser(0.1,1000);
  mE->SetTitle("Solar Spot Number Monthly");
  mE->Draw("apl");



  //Monthly NO ERROR ***************************************************************************
  TString monthly = "/var/www/html/SolarSmoothed/SSN_MonthlyPLOT.txt"; //percorso
  TGraph *m = new TGraph(monthly);
  m->GetXaxis()->SetTitle("year");
  m->GetYaxis()->SetTitle("SSN");
  m->GetXaxis()->CenterTitle();
  m->GetYaxis()->CenterTitle();
  m->SetMarkerColor(kAzure+2);
  m->SetLineColor(kAzure+2);
  m->SetMarkerStyle(20);
  m->SetMarkerSize(0.3);
  m->GetYaxis()->SetRangeUser(0.1,1000);
  m->SetTitle("Solar Spot Number Monthly");
  m->Draw("apl");



  c1->cd();


  vector<char> variable;
  ifstream set;
  string path ="/var/www/html/SSN/Set.txt";
  cout<<path<<endl;

  set.open(path);
  char sx;
  while (!set.eof()) {
    set>>sx>>ws;
    variable.push_back(sx);
  }


  TMultiGraph *mg = new TMultiGraph();
  TLegend *legend = new TLegend(.75,.75,.89,.89);

  for (int i=0; i<variable.size(); i++) {
    switch (variable[i]) {
    case '1':
      mg->Add(d);
      legend->AddEntry(d,"SSN Daily","l");
      break;
    case '2':
      mg->Add(dE);
      legend->AddEntry(dE,"SSN Daily","l");
      break;
    case '3':
      mg->Add(mo);
      legend->AddEntry(mo,"SSN Monthly","l");
      break;
    case '4':
      mg->Add(moE);
      legend->AddEntry(moE,"SSN Monthly","l");
      break;
    case '5':
      mg->Add(smo);
      legend->AddEntry(smo,"SSN Smoothed ","l");
      break;
    case '6':
      mg->Add(smoE);
      legend->AddEntry(smoE,"SSN Smoothed","l");
      break;
    }
  }

  mg->SetTitle("SSN");
  mg->Draw("apl");
  mg->GetXaxis()->SetRangeUser(xmin,xmax);
  mg->GetXaxis()->CenterTitle();
  mg->GetYaxis()->CenterTitle();
  mg->GetXaxis()->SetTitle("year");
  mg->GetYaxis()->SetTitle("Sunspot Number");
  mg->SetName("SSN Graph");


  legend->SetHeader("","C"); // option "C" allows to center the heade         
  legend->SetX1NDC(0.01);
  legend->SetX2NDC(0.9);
  legend->Draw();


  TFile ff("/var/www/html/SSN/SSN.root" , "recreate");
  ff.cd();                                             
  c1->Write();
  ff.Close();
  return 0;
}
