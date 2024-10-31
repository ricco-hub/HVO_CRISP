double GetProtonLISvsEkn(double Ekin /*GeV*/)
{

    // --- kinematics ---
    double E = Ekin; //kinetic energy (per nucleon)
    double Z = 1.;
    double A= 1.;
    double pA= 1.;   // mass number
    double pZ= 1.;   // charge number
    double Mp=0.938; // proton mass
    double pM=Mp*pA; // nucleus mass
    double R= (sqrt( (EIS[i]*pA+pM)*(EIS[i]*pA+pM)- (pM*pM)))/pZ; // rigidity R=p/Z
    double LnR= TMath::Log(R); // log-of-rigidity

    // --- low-R parameterization ---
    double Norm= 11600;
    double mu= -0.559;
    double sigma= 0.563;
    double G1 = -2.4482;
    double nu= 0.431;
    double LowR= (TMath::Power( 1.+ TMath::Exp(-(LnR-mu)/sigma), -1./nu ))*TMath::Power(R, G1);

    // --- high-R parameterization ---
    double Rb1 = 6.2;
    double DG1 = -0.4227;
    double S1  = -0.108;
    double Rb2 = 545.;
    double DG2 = -0.6;
    double S2  = -0.4;
    double HighR= TMath::Power(1.+ TMath::Power(  (R/Rb1)*TMath::Power(1.+ TMath::Power(R/Rb2, DG2/S2), S2) , DG1/S1 ), S1);


    double LIS_RIG =  Norm*LowR*HighR; // rigidity flux J(R) [GV^-1 m^-2 s^-1 sr^-1]
    // --- convert from rigidity to kinetic energy (per nucleon) ---
    // double dEdR = (pZ/pA)*(pZ/pA)*R/sqrt((pZ/pA)*(pZ/pA)*(R*R)+Mp*Mp); // jacobian dE/dR

    double dRdE= (pA/pZ)*(Mp + E)/sqrt(E*E + 2.*Mp*E); // Jacobian dR/dE

    double LIS_EKN = dRdE*LIS_RIG; // kinetic flux J(E) [(GeV/n)^-1 m^-2 s^-1 sr^-1]

    return LIS_EKN;
}
