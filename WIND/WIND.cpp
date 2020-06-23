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
//------------------------------------------------------------------------------
int main()
{
 
  // NTMAY2020 arriva fino al giorno 331 del 2020, ma i valori hanno senso fino a inizio
  // numero righe totali e usate
  const int m_NTOTLINES= 773; // 759+14; // contare meglio
  const int m_NMAX     = 773; // 759+14; // contare meglio

  bool kPLOT  = true; // plottiamo
  bool kSTORE = false; // salviamo come root
  // ---- define basic quantities / columns ----
  int iYear; // year
  int iDay;  // DoY
  int iHour; // Hour NOT USED HERE
  int iBr;   // Bartel rotation number
  int IMF_ID; // ID IMF - Interpl Mag Field
  int SWP_ID; // ID SWP - Solar Wind Plasma
  int IMF_TS; // TimeScale #points IMF
  int SWP_TS; // TimeScale #points SWP
  double B_Scal_Avg; // Magnitude of avg scalar B-field <F> [nT]
  double B_Vect_Avg; // Magnitude of avg vector B-field <B> [nT]
  double Lat_GSE_Avg; //  LATITUDE ANGLE AVG GSE [deg] 16.9
  double Lon_GSE_Avg; //  LONGITUDE ANGLE AVG GSE [deg] 324.0
  double Bx_GSE; // Bx GSE [nT] 0.3
  double By_GSE; // By GSE [nT] -0.2
  double Bz_GSE; // Bz GSE [nT] 0.1
  double By_GSM; // By GSM [nT] -0.2
  double Bz_GSM; // Bz GSM [nT] 0.1
  double Sigma_B_Scal; // RMS [nT] 1.5
  double Sigma_B_Vect; // RMS [nT] 2.8
  double Sigma_Bx_GSE; // RMS [nT]
  double Sigma_By_GSE; // RMS [nT]
  double Sigma_Bz_GSE; // RMS [nT]

  double ProtonTemp;
  double ProtonDensity; // Proton density [part/cm3] 7.5
  double WindSpeed;     // Bulk Speed [km/s] 379.0
  double BulkFlow_Phi;  // Bulk Flow longitude phi-V [deg] -0.1
  double BulkFlow_Theta;// Bulk Flow latitude theta-V [deg] -0.2
  double APRatio; // Alpha-Proton He/P ratio 0.005
  double FlowPressure;  // [nPa] 2.01

  double Sigma_Temp;     // [K] 41771.0
  double Sigma_Density;  // [part/cm3] 3.3
  double Sigma_Speed;   // [km/s] 97.
  double Sigma_FlowPhi;  // [deg] 1.1
  double Sigma_FlowTheta;// [deg] 1.3
  double Sigma_APRatio;  // [He/P] 0.013

  double ElectricField;  // Electric Field [mV/m] -0.03
  double PlasmaBeta; // 5.64
  double MachNumber; // Alfven Mach Number Ma 14.1
  int KpIndex10;     // Geomagnetic disturbance index x 10? 10
  int SunSpotDaily;  // Daily SSN from SILSO 0-300?
  int DST_Index;     // DST INDEX from Kyoto [nT] -3
  int AE_Index;      //  AE-INDEX from Kyoto [nT] 9999
  double ProtonFlux_1MeV;    // Proton flux above 1 MeV [1/(cm^2 sec sr)] 999999.99
  double ProtonFlux_2MeV;    // Proton flux above 1 MeV [1/(cm^2 sec sr)] 999999.99
  double ProtonFlux_4MeV;    // Proton flux above 1 MeV [1/(cm^2 sec sr)] 999999.99
  double ProtonFlux_10MeV;   // Proton flux above 1 MeV [1/(cm^2 sec sr)] 0.29
  double ProtonFlux_30MeV;   // Proton flux above 1 MeV [1/(cm^2 sec sr)] 0.19
  double ProtonFlux_60MeV;   // Proton flux above 1 MeV [1/(cm^2 sec sr)] 0.14
  int MSPH_Flux_FLAG; //  -1
  int AP_Index;       // 3-hour AP index from GFZ-Potsdam [nT] 4
  double F107_Index;  // Some daily index Watts/m sq/herts 68.4
  double PCN_Index; // Some Geomagnetic parameter from Copenhagen 999.9
  int  AL_INDEX; // From Kyoto [nT]
  int  AU_INDEX; // From Kyoto [nT]
  double MAC; // Magnetosonic Mac Number 6.2

  double fYear;
  // --- Wind Speed graphs ----
  TGraph* grWindSpeedVSTime= new TGraph();
  grWindSpeedVSTime->SetName("grWindSpeedVSTime");
  grWindSpeedVSTime->SetLineWidth(2);
  grWindSpeedVSTime->SetLineColor(kAzure);
  grWindSpeedVSTime->SetLineStyle(1);
  grWindSpeedVSTime->GetXaxis()->SetTitle("year");
  grWindSpeedVSTime->GetYaxis()->SetTitle(" Wind Speed [km/s] ");
  grWindSpeedVSTime->GetXaxis()->CenterTitle();
  grWindSpeedVSTime->GetYaxis()->CenterTitle();
  grWindSpeedVSTime->SetTitle("Solar Wind Speed  ");
  
  // --- Proton Density graphs ---
  TGraph* grProtonDensityVSTime= new TGraph();
  grProtonDensityVSTime->SetName("grProtonDensityVSTime");
  grProtonDensityVSTime->SetLineWidth(2);
  grProtonDensityVSTime->SetLineColor(kAzure);
  grProtonDensityVSTime->SetLineStyle(1);
  grProtonDensityVSTime->GetXaxis()->SetTitle("year");
  grProtonDensityVSTime->GetYaxis()->SetTitle(" Proton Density [part/cm^{3}] ");
  grProtonDensityVSTime->GetXaxis()->CenterTitle();
  grProtonDensityVSTime->GetYaxis()->CenterTitle();
  grProtonDensityVSTime->SetTitle("Proton Density");

  ifstream fileNM,fileNM2;


  int iL=0; // N of line scanned
  int iWindSpeed   = 0; // N of points (effectively used in graphs)
  int iBField      = 0;
  int iPrTemp      = 0;
  int iPrDensity   = 0;
  int iAPRatio     = 0;
  
  int iSSN         = 0;
  int iKpIndex10   = 0;
  int iFlowPressure= 0;
  int iPrFlux1MeV  = 0;
  int iPrFlux60MeV = 0;
  string line;
  fileNM.open("omni_27_av.dat"); // OMNIWeb DATA FILE
  fileNM2.open("omni_27_av.dat"); // OMNIWeb DATA FILE

  double cont;
  int righe=0;
  
  while(!fileNM2.eof()) {
    fileNM2>>cont;
    righe++;
  }

  righe = righe/55;  //righe totali da leggere
     
  while( iL < righe){

    fileNM>>
      iYear >>
      iDay >>
      iHour >>
      iBr >>
      IMF_ID >>
      SWP_ID >>
      IMF_TS >>
      SWP_TS >>
      B_Scal_Avg >>
      B_Vect_Avg >>
      Lat_GSE_Avg >>
      Lon_GSE_Avg >>
      Bx_GSE >>
      By_GSE >>
      Bz_GSE >>
      By_GSM >>
      Bz_GSM >>
      Sigma_B_Scal >>
      Sigma_B_Vect >>
      Sigma_Bx_GSE >>
      Sigma_By_GSE >>
      Sigma_Bz_GSE >>
      ProtonTemp >>
      ProtonDensity >>
      WindSpeed >>
      BulkFlow_Phi >>
      BulkFlow_Theta >>
      APRatio >>
      FlowPressure >>
      Sigma_Temp >>
      Sigma_Density >>
      Sigma_Speed >>
      Sigma_FlowPhi >>
      Sigma_FlowTheta >>
      Sigma_APRatio >>
      ElectricField >>
      PlasmaBeta >>
      MachNumber >>
      KpIndex10 >>
      SunSpotDaily >>
      DST_Index >>
      AE_Index >>
      ProtonFlux_1MeV >>
      ProtonFlux_2MeV >>
      ProtonFlux_4MeV >>
      ProtonFlux_10MeV >>
      ProtonFlux_30MeV >>
      ProtonFlux_60MeV >>
      MSPH_Flux_FLAG >>
      AP_Index >>
      F107_Index >>
      PCN_Index >>
      AL_INDEX >>
      AU_INDEX >>
      MAC;

    // --- cout<< iYear<<"    " <<iDay<<endl; ---

    // ---- compute fractional year ----
    double fDOY = ((double)iDay)/365.; // fract day of the year
    fYear = (double)iYear + fDOY; // fract year
    cout<< iYear<< "       "<<iDay<<"           "<< FlowPressure<<endl;

     
    // --- wind speed  ---
    if(WindSpeed>0 && WindSpeed<9999){
      grWindSpeedVSTime->SetPoint(iWindSpeed, fYear, WindSpeed);
      iWindSpeed++;
    }

    // --- proton density ---
    if(ProtonDensity>0 && ProtonDensity<999){
      grProtonDensityVSTime->SetPoint(iPrDensity, fYear, ProtonDensity);
      iPrDensity++;
    }
  
    // increment line
    iL++;
  }

  TCanvas *c1 = new TCanvas("TOTAL Graph","titolo Canvas");
  c1->SetFillColor(0);
    
  TFile* outFile= new TFile("WIND-DENSITY.root","RECREATE");
  outFile->cd();

  grWindSpeedVSTime->Draw("l");
  grProtonDensityVSTime->Draw("l");

  


  grWindSpeedVSTime->Write();
  grProtonDensityVSTime->Write();
    

  outFile->Write();
  outFile->Close();
  
  
 




  return 0;
}

