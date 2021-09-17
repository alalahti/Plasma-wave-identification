%Preparing SheathData
%Construct a matrix for studied events first three columns being the shock
%theta, M_A, the number of mirror modes in the sheath; columns 20:22 are
%the number of MMs in the sheath subregions
%PrepareSheathData   

%Set the length of studied intervals
timesequence = 60;

%Setting the criteria
Angle_criterion = 45;
Perp_Mean_criterion = 0.01;
Perp_Par_critetion = 8.6;
Max_Int_criterion = 10;

Azimuth_criterion = 30;
Elevation_criterion = 30;
Magnitude_criterion = 0.3;

%Set the cutoff frequency
cutoff = 0.015;

%Hodograms for a sheath
Drawing = 3; %If you want to plot hodograms

%Import the data
%%%% Whole data %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Data = importdata('/pathtoFile/File1.dat');
%PlasmaData = importdata('/pathtoFile/File2.dat');
%VelocityData = importdata('/pathtoFile/File3.dat');
%DensityData = importdata('/pathtoFile/AICwaves/File.dat');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
PlasmaData(:,4) = PlasmaData(:,5);
PlasmaData(:,5) = PlasmaData(:,3)./PlasmaData(:,2);  

time = transpose(Data(:,1));
timeplasma = transpose(PlasmaData(:,1));

StudiedSheath = 1;

Xaxis = [];
Yaxis = [];
Zaxis = [];
MagneticField = [];

Time = [];
TimePlasma = [];

spots = find(time == 0);
spotsplasma = find(timeplasma == 0);

Intervals = [];
AICPlasmaValues = [];
NonAICSheathPlasmaValues = [];
SheathPlasmaValues = [];
Fluctuations = [];

IntervalsPassed = 0;
IntervalsNonPassed = 0;
laps = 0;
lapslongenough = 0;
sheath = 0;

SizeOfInterval = [];
MaxIntRatios = [];
Variations = [];
W1min = [];
W1minPassed = [];

Frequencies = [];

value = 0;
while StudiedSheath <= size(find(time == 0),2)
    
    sheath = sheath + 1
    
    NumberOfEventsInSheath = 0;
    NumberOfIntervalsInSheath = 0;
    AIC_in_NS = 0;
    AIC_in_MS = 0;
    AIC_in_NLE = 0;
    
    F01 = 0;
    F12 = 0;
    F23 = 0;
    F34 = 0;
    F45 = 0;
    F56 = 0;
    F67 = 0;
    F78 = 0;
    F89 = 0;
    F91 = 0;
    
    %Taking the data of a sheath%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if StudiedSheath == size(find(time == 0),2)
        Xaxis = Data(spots(StudiedSheath):end,3);
        Yaxis = Data(spots(StudiedSheath):end,4);
        Zaxis = Data(spots(StudiedSheath):end,5);
        MagneticField = Data(spots(StudiedSheath):end,2);
        Time = time(1,spots(StudiedSheath):end);
        TimePlasma = timeplasma(1,spotsplasma(StudiedSheath):end);
        Plasma = PlasmaData(spotsplasma(StudiedSheath):end,:);
        Velocity = VelocityData(spotsplasma(StudiedSheath):end,:);
        Density = DensityData(spotsplasma(StudiedSheath):end,:);
    else
        Xaxis = Data(spots(StudiedSheath):spots(StudiedSheath+1)-1,3);
        Yaxis = Data(spots(StudiedSheath):spots(StudiedSheath+1)-1,4);
        Zaxis = Data(spots(StudiedSheath):spots(StudiedSheath+1)-1,5);
        MagneticField = Data(spots(StudiedSheath):spots(StudiedSheath+1)-1,2);
        Time = time(1,spots(StudiedSheath):spots(StudiedSheath+1)-1);
        TimePlasma = timeplasma(1,spotsplasma(StudiedSheath):spotsplasma(StudiedSheath+1)-1);
        Plasma = PlasmaData(spotsplasma(StudiedSheath):spotsplasma(StudiedSheath+1)-1,:);
        Velocity = VelocityData(spotsplasma(StudiedSheath):spotsplasma(StudiedSheath+1)-1,:);
        Density = DensityData(spotsplasma(StudiedSheath):spotsplasma(StudiedSheath+1)-1,:);
    end
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
   %Low-pass filtering:
    X = fftf_LowPass(transpose(Time),Xaxis,cutoff);
    Y = fftf_LowPass(transpose(Time),Yaxis,cutoff);
    Z = fftf_LowPass(transpose(Time),Zaxis,cutoff);
    B = [X; Y; Z];
    B(4,:) = sqrt(B(1,:).*B(1,:) + B(2,:).*B(2,:) + B(3,:).*B(3,:));
    %%%%%%%%%%%%%%%%%%%
    %High-pass filtering:
    X_f = fftf_HighPass(transpose(Time),Xaxis,cutoff);
    Y_f = fftf_HighPass(transpose(Time),Yaxis,cutoff);
    Z_f = fftf_HighPass(transpose(Time),Zaxis,cutoff);
    B_f = [X_f; Y_f; Z_f];
    %%%%%%%%%%%%%%%%%%%
    %Removing the extra 5min from the beginning and ending
    timecut = 300;
    Start = find(Time >= timecut);
    Start = Start(1);

    End = find(Time >= Time(end)-timecut);
    End = End(1);
    
    X = X(:,Start:End);
    Y = Y(:,Start:End);
    Z = Z(:,Start:End);
    B = B(:,Start:End);

    X_f = X_f(:,Start:End);
    Y_f = Y_f(:,Start:End);
    Z_f = Z_f(:,Start:End);
    B_f = B_f(:,Start:End);

    Time = Time(:,Start:End);
    Time = Time-timecut;
    
    if size(Plasma,1) > 1
        Start = find(TimePlasma >= timecut);
        Start = Start(1);

        End = find(TimePlasma >= TimePlasma(end)-timecut);
        End = End(1);
 
        TimePlasma = TimePlasma(1,Start:End);
        TimePlasma = TimePlasma-timecut;
    
        Plasma = Plasma(Start:End,:);
        Plasma(:,1) = Plasma(:,1)-timecut;
        
        Velocity = Velocity(Start:End,:);
        Velocity(:,1) = Velocity(:,1)-timecut;
        
        Density = Density(Start:End,:);
        Density(:,1) = Density(:,1)-timecut;
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Sheath Duration in seconds
    LengthOfSheath = size(Time,2);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %Compute the unit vector for B
    b_0 = [X; Y; Z];
    b_0 = b_0./sqrt(b_0(1,:).*b_0(1,:) + b_0(2,:).*b_0(2,:) + b_0(3,:).*b_0(3,:));
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %Parallel and perpendicular components of fluctuation field
    B_f_par = dot(B_f,b_0).*b_0;
    B_f_perp = B_f - B_f_par;

    B_f_par(4,:) = sqrt(B_f_par(1,:).*B_f_par(1,:) + B_f_par(2,:).*B_f_par(2,:) + B_f_par(3,:).*B_f_par(3,:));
    B_f_perp(4,:) = sqrt(B_f_perp(1,:).*B_f_perp(1,:) + B_f_perp(2,:).*B_f_perp(2,:) + B_f_perp(3,:).*B_f_perp(3,:));
    B_f(4,:) = sqrt(B_f(1,:).*B_f(1,:) + B_f(2,:).*B_f(2,:) + B_f(3,:).*B_f(3,:));
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    index = 1;
    %Going through a sheath
    while index < size(Time,2)
        laps = laps + 1;
  
        k = index;
        Start = index;
        Differences = [];
        while k < size(Time,2) && Time(k)-Time(index)<timesequence   
            k = k + 1;
            Differences(k-Start) = Time(k)-Time(k-1);
        end
        End = k;

        SizeOfInterval(laps,1) = End - Start;
        SizeOfInterval(laps,2) = mean(Differences);
        SizeOfInterval(laps,3) = max(Differences);
        SizeOfInterval(laps,4) = SizeOfInterval(laps,1)*mean(Differences);
        
        Location = Start+(End-Start)/2;
        RelativeLocation = Location/LengthOfSheath;
        %%%%%%%%%%%%%%%
        BetaPar = 0;
        BetaPerp = 0;
        Threshold = 0;
        Anisotropy = 0;
        n = 0;
        Vbulk = 0;
        %%%%%%%%%%%%%%%       
        if size(Plasma,1) > 1
            PlasmaDataPoints = find(TimePlasma > Time(Start)-150 & TimePlasma < Time(End)+150);

            if size(PlasmaDataPoints,2) >= 1
               BetaPar = sum(Plasma(PlasmaDataPoints,2))/size(PlasmaDataPoints,2);
               BetaPerp = sum(Plasma(PlasmaDataPoints,3))/size(PlasmaDataPoints,2);
               Threshold = sum(Plasma(PlasmaDataPoints,4))/size(PlasmaDataPoints,2);
               Anisotropy = sum(Plasma(PlasmaDataPoints,5))/size(PlasmaDataPoints,2);
               
               Vbulk = sum(Velocity(PlasmaDataPoints,3:5),1)/size(PlasmaDataPoints,2);
               Vbulk = Vbulk.*1000;
               n = sum(Density(PlasmaDataPoints,2))/size(PlasmaDataPoints,2);
               vperp = sum(Density(PlasmaDataPoints,3))/size(PlasmaDataPoints,2);
            end  
        end    
        
        SheathPlasmaValues(laps,1) = Location;
        SheathPlasmaValues(laps,2) = RelativeLocation;
        SheathPlasmaValues(laps,3) = BetaPar;
        SheathPlasmaValues(laps,4) = BetaPerp;
        SheathPlasmaValues(laps,5) = Threshold;
        SheathPlasmaValues(laps,6) = Anisotropy;
        
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %Taking the intervals long enough and with max data gap of 5.52s
        if Time(k)-Time(index)>timesequence-20 && max(Differences) < 5.52
            NumberOfIntervalsInSheath = NumberOfIntervalsInSheath + 1;
            lapslongenough = lapslongenough + 1;
            i = index;
            
            %Computing the mean B during the interval
            %Computing ion cyclotron frequency
            ii = 1;
            T = 0;
            
            B_mean = 0;
            w = 0;
            w_e = 0;
            c = 299792458;
            q = 1.6021766208e-19;
            m = 1.672621898e-27;
            m_e = 9.1093835611e-31;
            e = 8.854187817e-12;
            
            while i <= k
                if i < k
                    T(ii) = time(i+1) - time(i);
                    ii = ii + 1;
                end
                B_mean = B_mean + B(4,i);
                w = w + (q/m)*B(4,i)*1e-9;
                w_e = w_e - (q/m_e)*B(4,i)*1e-9;
                i = i + 1;
            end
            samplesize = k-index+1;
            B_mean = B_mean/samplesize;
            T = sum(T)/size(T,2);
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            w = w/(2*pi*samplesize);
            w_e = w_e/(2*pi*samplesize);
            W1min = [W1min; [w B_mean]];
            
            W_gi = 2*pi*w;
            W_ge = 2*pi*w_e;
            W_pi = sqrt((n*q*q)/(e*m));
            W_pe = sqrt((n*q*q)/(e*m_e));
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %Computing mean square of background B (B_dc)
            %and mean square fluctuations(BF_average, Fluctuations_par,
            %Fluctuations_perp)
            i = index;
            B_dc = 0;
            BF_average = 0;
            Fluctuations_par = 0;
            Fluctuations_perp = 0;
            while i <= k
               B_dc = B_dc + B(4,i).*B(4,i);
               BF_average = BF_average + B_f(4,i).*B_f(4,i);
               Fluctuations_par = Fluctuations_par + B_f_par(4,i).*B_f_par(4,i);
               Fluctuations_perp = Fluctuations_perp + B_f_perp(4,i).*B_f_perp(4,i);
               i = i + 1; 
            end
            samplesize = k-index+1;
            B_dc = B_dc/samplesize;
            BF_average = BF_average/samplesize;  
            Fluctuations_par =  Fluctuations_par/samplesize;
            Fluctuations_perp = Fluctuations_perp/samplesize;
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%            
            %Average direction of b_0, B and BF during the interval
            b_0mean = [sum(b_0(1,index:k))/samplesize, sum(b_0(2,index:k))/samplesize, sum(b_0(3,index:k))/samplesize];
            
            Bmean = [sum(B(1,index:k))/samplesize, sum(B(2,index:k))/samplesize, sum(B(3,index:k))/samplesize];
            BFmean = [sum(B_f(1,index:k))/samplesize, sum(B_f(2,index:k))/samplesize, sum(B_f(3,index:k))/samplesize];
            
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %%%%Computing the angular and magnitudinal variation of background magnetic field
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %Spherical coordinates
            B_r = [];
            B_theta = [];
            B_phi = [];
            
            i = index;
            i2 = 1;
            while i <= k
                [B_phi2,B_theta2,B_r(i2,1)] = cart2sph(B(1,i),B(2,i),B(3,i));
                B_phi2 = B_phi2/pi*180;
                B_theta2 = B_theta2/(pi/2)*90;
                
                B_theta2 = 90 + B_theta2;
                
                B_phi(i2,1) = B_phi2;
                B_theta(i2,1) = B_theta2;
                
                i2 = i2 + 1;
                i = i + 1;
            end
            
            Max_A = max(B_phi);
            Min_A = min(B_phi);
            if Max_A > 0 && Min_A >0
                Azimuth_variation = max(B_phi)-min(B_phi);
            elseif Max_A < 0 && Min_A < 0
                Azimuth_variation = abs(max(B_phi)-min(B_phi));     
            elseif Max_A > 90 && Min_A < -90
                Azimuth_variation = (180-max(B_phi))+abs(-180-min(B_phi));
            else
                Azimuth_variation = max(B_phi)+abs(min(B_phi));
            end
            
            Elevation_variation = max(B_theta)-min(B_theta);
            Magnitude_variation = (max(B_r)-min(B_r))/B_dc;
            Variations(lapslongenough,1) = Azimuth_variation;
            Variations(lapslongenough,2) = Elevation_variation;
            Variations(lapslongenough,3) = Magnitude_variation;

            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %Computing the ratios of fluctutations
            Perp_Mean_ratio = Fluctuations_perp/B_dc;
            Perp_Mean_ratioF =  Fluctuations_perp/BF_average;
            Perp_Par_ratio = Fluctuations_perp/Fluctuations_par;
            FlucRatio = BF_average/B_dc;
            
            Fluctuations(lapslongenough,1) = RelativeLocation;
            Fluctuations(lapslongenough,2) = BF_average;    
            Fluctuations(lapslongenough,3) = Perp_Mean_ratio;
            Fluctuations(lapslongenough,4) = Perp_Par_ratio;
            %Fluctuations(lapslongenough,5) = FlucRatio;
            
            Fluctuations(lapslongenough,5) = BetaPar;
            Fluctuations(lapslongenough,6) = BetaPerp;
            Fluctuations(lapslongenough,7) = Threshold;
            Fluctuations(lapslongenough,8) = Anisotropy;
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %Standard variance analysis
            Bx = sum(B_f(1,index:k))/samplesize;
            By = sum(B_f(2,index:k))/samplesize;
            Bz = sum(B_f(3,index:k))/samplesize;
            Bxx = sum(B_f(1,index:k).*B_f(1,index:k))/samplesize;
            Byy = sum(B_f(2,index:k).*B_f(2,index:k))/samplesize;
            Bzz = sum(B_f(3,index:k).*B_f(3,index:k))/samplesize;
            Bxy = sum(B_f(1,index:k).*B_f(2,index:k))/samplesize;
            Bxz = sum(B_f(1,index:k).*B_f(3,index:k))/samplesize;
            Byz = sum(B_f(2,index:k).*B_f(3,index:k))/samplesize;
         
            B11 = Bxx-Bx*Bx;
            B12 = Bxy-Bx*By;
            B13 = Bxz-Bx*Bz;
        
            B21 = B12;
            B22 = Byy-By*By;
            B23 = Byz-By*Bz;
        
            B31 = B13;
            B32 = B23;
            B33 = Bzz-Bz*Bz;
        
            M = [B11 B12 B13; B21 B22 B23; B31 B32 B33];
            [V,D] = eig(M);
        
            Eigenvalues = diag(D);
            Eigenvectors = V;
        
            M_2 = [D(1,1), transpose(V(:,1)); D(2,2), transpose(V(:,2)); D(3,3), transpose(V(:,3))];
            %Sort the matrix according the eigenvalues, the top row - the
            %maximum eigenvalue.
            M_2 = sortrows(M_2,-1);
        
            %Ratio = Max direction eigenvalue / Int direction eigenvalue
            %Ratio2 = Int eigenvalue / Min eigenvalue
            Ratio = M_2(1,1)/M_2(2,1);
            Ratio2 = M_2(2,1)/M_2(3,1); 
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
            Fluctuations(lapslongenough,9) = Ratio;
            Fluctuations(lapslongenough,10) = Perp_Mean_ratioF;
            Fluctuations(lapslongenough,11) = Ratio2;
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            
            MaxIntRatios = [MaxIntRatios; Ratio];
            %Angle between the minimum variance direction and mean background field
            Angle = (180/pi)*acos((b_0mean(1)*M_2(3,2) + b_0mean(2)*M_2(3,3) + b_0mean(3)*M_2(3,4))/(sqrt(b_0mean(1)*b_0mean(1) + b_0mean(2)*b_0mean(2) + b_0mean(3)*b_0mean(3))*sqrt(M_2(3,2)*M_2(3,2) + M_2(3,3)*M_2(3,3) + M_2(3,4)*M_2(3,4))));
            if Angle > 90
               Angle = 180 - Angle;
            end
            Fluctuations(lapslongenough,12) = Angle;
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %Checking whether the interval passes the criteria:
            if Angle < Angle_criterion && Perp_Mean_ratio > Perp_Mean_criterion && Perp_Par_ratio > Perp_Par_critetion && Azimuth_variation < Azimuth_criterion  && Elevation_variation < Elevation_criterion && Magnitude_variation < Magnitude_criterion && Ratio < Max_Int_criterion
                
                NumberOfEventsInSheath = NumberOfEventsInSheath + 1;
                IntervalsPassed = IntervalsPassed + 1;
                
                %Writing properties down
                W1minPassed = [W1minPassed; w];
                
                Intervals(IntervalsPassed,1) = RelativeLocation; 
                Intervals(IntervalsPassed,2) = BF_average;
                Intervals(IntervalsPassed,3) = Perp_Mean_ratio;
                Intervals(IntervalsPassed,4) = Perp_Par_ratio;
                Intervals(IntervalsPassed,5) = Ratio;

                AICPlasmaValues(IntervalsPassed,1) = RelativeLocation;
                AICPlasmaValues(IntervalsPassed,2) = BetaPar;
                AICPlasmaValues(IntervalsPassed,3) = BetaPerp;
                AICPlasmaValues(IntervalsPassed,4) = Threshold;
                AICPlasmaValues(IntervalsPassed,5) = Anisotropy;
                
                AICPlasmaValues(IntervalsPassed,6) = Perp_Mean_ratio;
                AICPlasmaValues(IntervalsPassed,7) = Perp_Par_ratio;
                AICPlasmaValues(IntervalsPassed,8) = Angle;
                AICPlasmaValues(IntervalsPassed,9) = Ratio;
                AICPlasmaValues(IntervalsPassed,10) = Perp_Mean_ratioF;
                AICPlasmaValues(IntervalsPassed,11) = Ratio2;
                
                if RelativeLocation < 1/3
                    AIC_in_NS = AIC_in_NS + 1;
                end
                if RelativeLocation > 1/3 && RelativeLocation < 2/3
                    AIC_in_MS = AIC_in_MS + 1;
                end
                if RelativeLocation > 2/3
                    AIC_in_NLE = AIC_in_NLE + 1;
                end
                %%%
                if RelativeLocation < 0.1
                    F01 = F01 + 1;
                end
                if RelativeLocation >= 0.1 && RelativeLocation < 0.2 
                    F12 = F12 + 1;
                end
                if RelativeLocation >= 0.2 && RelativeLocation < 0.3 
                    F23 = F23 + 1;
                end
                if RelativeLocation >= 0.3 && RelativeLocation < 0.4 
                    F34 = F34 + 1;
                end
                if RelativeLocation >= 0.4 && RelativeLocation < 0.5 
                    F45 = F45 + 1;
                end
                if RelativeLocation >= 0.5 && RelativeLocation < 0.6 
                    F56 = F56 + 1;
                end
                if RelativeLocation >= 0.6 && RelativeLocation < 0.7 
                    F67 = F67 + 1;
                end
                if RelativeLocation >= 0.7 && RelativeLocation < 0.8 
                    F78 = F78 + 1;
                end
                if RelativeLocation >= 0.8 && RelativeLocation < 0.9 
                    F89 = F89 + 1;
                end
                if RelativeLocation >= 0.9 
                    F91 = F91 + 1;
                end
                
                
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%              
                x = dot(b_0mean(1:3),M_2(1,2:4));
                y = dot(b_0mean(1:3),M_2(2,2:4));
                z = dot(b_0mean(1:3),M_2(3,2:4));
                vektori = [x, y ,z];
    
                Cross = cross(M_2(1,2:4),M_2(2,2:4));
                Angle_V = dot(Cross,M_2(3,2:4))/(sqrt(Cross(1)*Cross(1) + Cross(2)*Cross(2) + Cross(3)*Cross(3))*sqrt( M_2(3,2)*M_2(3,2) + M_2(3,3)*M_2(3,3) + M_2(3,4)*M_2(3,4)));
                Angle_V = real(acosd(Angle_V));
   
                if Angle_V > 179
                    %disp('right handness')
        
                    B1(1,1:3) = -M_2(1,2:4);
                    B1(2,1:3) =  M_2(2,2:4);
                    B1(3,1:3) =  M_2(3,2:4);
        
                    B2(1,1:3) =  M_2(1,2:4);
                    B2(2,1:3) = -M_2(2,2:4);
                    B2(3,1:3) =  M_2(3,2:4);
        
                    B3(1,1:3) =  M_2(1,2:4);
                    B3(2,1:3) =  M_2(2,2:4);
                    B3(3,1:3) = -M_2(3,2:4);
        
                    Z1 = dot(b_0mean(1:3),B1(3,1:3));
                    Z2 = dot(b_0mean(1:3),B2(3,1:3));
                    Z3 = dot(b_0mean(1:3),B3(3,1:3));
        
                    if Z1 > 0 && Z3 < 0
                        M_2(1,2:4) = -M_2(1,2:4);
                    elseif Z3 > 0 && Z1 < 0
                        M_2(3,2:4) = -M_2(3,2:4);
                    else
                        disp('ERROR')
                    end
                    x = dot(b_0mean(1:3),M_2(1,2:4));
                    y = dot(b_0mean(1:3),M_2(2,2:4));
                    z = dot(b_0mean(1:3),M_2(3,2:4));
                    if z < 0
                        disp('z<0')
                    end
        
                end
                x = dot(b_0mean(1:3),M_2(1,2:4));
                y = dot(b_0mean(1:3),M_2(2,2:4));
                z = dot(b_0mean(1:3),M_2(3,2:4));
 
                if sign(z) < 0 
                    %disp('modify')
                    M_2(1,2:4) = -M_2(1,2:4);
                    M_2(3,2:4) = -M_2(3,2:4);
                end
    
                x = dot(b_0mean(1:3),M_2(1,2:4));
                y = dot(b_0mean(1:3),M_2(2,2:4));
                z = dot(b_0mean(1:3),M_2(3,2:4));
                Z = z;
    
                if sign(z) < 0
                    disp('Error sign(z)')
                end
              
                Cross = cross(M_2(1,2:4),M_2(2,2:4));
                Angle_V = dot(Cross,M_2(3,2:4))/(sqrt(Cross(1)*Cross(1) + Cross(2)*Cross(2) + Cross(3)*Cross(3))*sqrt( M_2(3,2)*M_2(3,2) + M_2(3,3)*M_2(3,3) + M_2(3,4)*M_2(3,4)));
                Angle_V = real(acosd(Angle_V));
                if Angle_V > 0.1
                   disp('ERROR'); 
                end
           
                Variance = [];
                i = index;
                i2 = 1;
                TimeAxis = [];
                Min_dir = M_2(3,2:4);
                while i <= k
                    Bmax = dot(B_f(1:3,i),M_2(1,2:4));
                    Binter = dot(B_f(1:3,i),M_2(2,2:4));
                    Bmin = dot(B_f(1:3,i),M_2(3,2:4));
                    Variance(:,i2) = [Bmax; Binter; Bmin];
                    
                    TimeAxis(i2) = Time(i)-Time(index);
                    
                    i2 = i2 + 1;
                    i = i + 1;
                end
                %Power Spectra
                Bspectra = transpose(sqrt(Variance(1,:).*Variance(1,:) + Variance(2,:).*Variance(2,:)));
                [dataout,F,Conf]=psdtsh(Bspectra,T,2,6/2);
                %Weighted frequency according to the power spectra,
                %spacecraft frequency, F_spacecraft 
                if min(F)>=0
                    [pks,locs] = findpeaks(dataout);
                    [peak,location] = max(pks);
               
                    %F_spacecraft2 = meanfreq(dataout,F);
                
                    Freq = F(locs(location));
                    F_spacecraft = Freq;
                
                    %F_spacecraft = F_spacecraft2;
                else
                    F_spacecraft = -1;
                end                    
                W_sc = 2*pi*F_spacecraft;
                %Ellipticity analysis
                p = [];
                p(1,:) = Variance(1,:);
                p(2,:) = Variance(2,:);
                p(3,:) = Variance(3,:);
                p(1,:) = p(1,:)-mean(p(1,:));
                p(2,:) = p(2,:)-mean(p(2,:));
                p(3,:) = p(3,:)-mean(p(3,:));
    
                p = transpose(p);
    
                windows = length(p);
                noverlap = [];
                nfft = length(p);

                SM(1,1) = mean(cpsd(p(:,1),(p(:,1)),windows,noverlap,nfft));
                SM(2,1) = mean(cpsd(p(:,2),(p(:,1)),windows,noverlap,nfft));
                SM(3,1) = mean(cpsd(p(:,3),(p(:,1)),windows,noverlap,nfft));

                SM(1,2) = mean(cpsd(p(:,1),(p(:,2)),windows,noverlap,nfft));
                SM(2,2) = mean(cpsd(p(:,2),(p(:,2)),windows,noverlap,nfft));
                SM(3,2) = mean(cpsd(p(:,3),(p(:,2)),windows,noverlap,nfft));

                SM(1,3) = mean(cpsd(p(:,1),(p(:,3)),windows,noverlap,nfft));
                SM(2,3) = mean(cpsd(p(:,2),(p(:,3)),windows,noverlap,nfft));
                SM(3,3) = mean(cpsd(p(:,3),(p(:,3)),windows,noverlap,nfft));

                Imaginary = imag(SM);
                Real = real(SM);

                [V1,V2] = eig(Real);
    
                Brot = p(:,1:3)*V1;
    
                SM = [];
    
                SM(1,1) = mean(cpsd(p(:,1),(p(:,1)),windows,noverlap,nfft));
                SM(1,2) = mean(cpsd(p(:,1),(p(:,2)),windows,noverlap,nfft));
                SM(2,1) = mean(cpsd(p(:,2),(p(:,1)),windows,noverlap,nfft));
                SM(2,2) = mean(cpsd(p(:,2),(p(:,2)),windows,noverlap,nfft));
    
                Rotated = SM;

                %disp('Degree of Polarization');
                R = sqrt(1-(4*real(det(Rotated)))/(Rotated(1,1)+Rotated(2,2))^2);

                D = 1/2*(Rotated(1,1) + Rotated(2,2)) - 1/2*sqrt( (Rotated(1,1)+Rotated(2,2))*(Rotated(1,1)+Rotated(2,2)) - 4*real(det(Rotated)) );

                P = []; 
                P(1,1) = Rotated(1,1)-D;
                P(1,2) = Rotated(1,2);
                P(2,1) = Rotated(2,1);
                P(2,2) = Rotated(2,2)-D;

                A = 2*real(P(1,2))/(real(P(1,1))-real(P(2,2)));
                %disp('Orientation')
                A = atand(A)/2;
    
                %disp('Ellipticity')
                p = 2*imag(P(1,2))/sqrt( (P(1,1)+P(2,2))*(P(1,1)+P(2,2)) -4*det(P) );
                p = asin(p)/2;
                p = tan(p);
    
                p = real(p);
                
                Intervals(IntervalsPassed,6) = sign(p); 
                Intervals(IntervalsPassed,7) = p; 
                Intervals(IntervalsPassed,8) = Z; 
                
                AICPlasmaValues(IntervalsPassed,12) = sign(p);
                
                %%%%DOPPLER SHIFT%%%%
                %K = wave_vector 
                if norm(Vbulk)>0 && F_spacecraft > -1  %size(PlasmaDataPoints,2) >= 1
                    value = value + 1;
                    %RH waves
                    if sign(p) > 0
                        A1 = -W_pe^2*W_sc/W_ge-W_pi^2*W_sc/(W_gi+W_sc);
                        A2 = c^2+(W_pi^2/2)*vperp^2/((W_gi+W_sc)^2);
                        K = sqrt(A1/A2);
                    end
                    %LF waves
                    if sign(p) < 0
                        %F_spacecraft = -F_spacecraft;
                        W_sc = -W_sc;
                        A1 = W_pe^2*W_sc/W_ge+W_pi^2*W_sc/(W_gi-W_sc);
                        A2 = c^2+(W_pi^2/2)*vperp^2/((W_gi-W_sc)^2);
                        K = sqrt(A1/A2);
                        W_sc = -W_sc;
                    end
                    
                    %%%
                    Termi = Vbulk/norm(Vbulk);
                    Termi1 = abs(dot(Min_dir,Termi)*norm(Vbulk));
                    Termi1 = Termi1/(abs(W_sc/K))+1;
                    F_plasma = F_spacecraft/Termi1;
                    W_plasma = 2*pi*F_plasma;
                    
                    %%%
                    
                    Frequencies(value,1:5) = [F_spacecraft sign(p)*W_sc/W_gi  F_plasma sign(p)*W_plasma/W_gi norm(Vbulk)/abs(W_sc/K)];
                    AICPlasmaValues(IntervalsPassed,12:16) = [F_spacecraft sign(p)*W_sc/W_gi  F_plasma sign(p)*W_plasma/W_gi norm(Vbulk)/abs(W_sc/K)];

                end
                
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   
                %Draw hodograms:
                if NumberOfEventsInSheath <= Drawing 
                    pubfig(figure)
                    %{
                    plot(F,dataout,'linewidth',2)
                    hold on
                    x = [F_spacecraft  F_spacecraft];
                    y = [0 max(dataout)+max(dataout)/4];
                    plot(x,y,'linewidth',2)
                    hold on 
                    x = [F_spacecraft2  F_spacecraft2];
                    y = [0 max(dataout)+max(dataout)/4];
                    plot(x,y,'b','linewidth',2)
                    hold on
                    x = [w w];
                    plot(x,y,'--','linewidth',2)
                    hold off
                    axis([0 max(F) 0 max(dataout)+max(dataout)/4]);
                    
                    %{
                    pubfig(figure)
                    plot(F,dataout,'linewidth',2)
                    hold on
                    [pks,locs] = findpeaks(dataout);
                    [peak,location] = max(pks);
                    scatter(F(locs(location)),peak,70,'linewidth',2)
                    hold on
                    x = [F(locs(location)) F(locs(location))];
                    y = [0 max(dataout)+max(dataout)/4];
                    h1 = plot(x,y,'--','linewidth',2);
                    hold on
                    x = [w w];
                    y = [0 max(dataout)+max(dataout)/4];
                    h2 = plot(x,y,'k','linewidth',2);
                    axis([0 F(end)/2 0 max(dataout)+max(dataout)/4]);
                    legend([h1 h2],{'AIC freq.','IC freq.'})
                    title(['AIC freq. / IC freq. = ' num2str(F(locs(location))/w)])
                    set(gca,'FontName','Arial','FontSize',12,'FontWeight','Bold','LineWidth',2);
                    hold off
                    %}
                    %}
                    TimeAxis = 1:10:10*size(Variance,2);
                    x = dot(BFmean(1:3),M_2(1,2:4));
                    y = dot(BFmean(1:3),M_2(2,2:4));
                    %z = dot(BFmean(1:3),M_2(3,2:4)); 
                    %vektori = [x, y ,z];
                    c = sort(linspace(10,40,length(Variance(1,:))),'descend');
                    sz = sort(linspace(20,150,length(Variance(1,:))),'descend');
                
                    Variance(1,:) = smooth(Variance(1,:));
                    Variance(2,:) = smooth(Variance(2,:));
                    
                    %Plot 3D
                    pubfig(figure)                
                    if z > 0
                        %plot3(TimeAxis,Variance(1,:),Variance(2,:),'k','LineWidth',1);
                        %hold on
                        scatter3(TimeAxis,Variance(1,:),Variance(2,:),sz,c,'filled')
                        hold on
                    else
                        disp('ERROR IN THE END')
                        %{
                        %plot3(TimeAxis,-Variance(1,:),Variance(2,:),'k','LineWidth',1);
                        %hold on
                        scatter3(TimeAxis,-Variance(1,:),Variance(2,:),sz,c,'filled')
                        hold on
                        %}
                    end
                    ylabel('B_1 [nT]') % y-axis label
                    zlabel('B_2 [nT]') % z-axis label
                    xlabel('Time [s]')
                    hold off
                    title(['Temp.An = ' num2str(Anisotropy) 'BetaPar = ' num2str(BetaPar)]);
                    %Plot 2D
                    %{
                    pubfig(figure)
                    scatter(Variance(1,:),Variance(2,:),sz,c,'filled')
                    hold on 
                    plot(Variance(1,:),Variance(2,:),'k','LineWidth',1);
                    hold on
                    scatter(vektori(1),vektori(2),100,'o','k','LineWidth',50);
                        
                    xlabel('B_1 [nT]') % x-axis label
                    ylabel('B_2 [nT]') % y-axis label
                    hold off
                    %title([' \theta_{kB0} =' num2str(Angle) ' \lambda_1/\lambda_2=' num2str(M_2(1,1)/M_2(2,1)) ' \delta B^2_{\perp}/B^2_{DC} = ' num2str(Perp_Mean_ratio) ' \delta B^2_{\perp}/ \delta B^2_{||} = ' num2str(Perp_Par_ratio) ]);
                    title(['Z = ' num2str(Z) ' p = ' num2str(p)]);
                    %}
                    %}
                end
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            else
                IntervalsNonPassed = IntervalsNonPassed + 1;
                NonAICSheathPlasmaValues(IntervalsNonPassed,1) = RelativeLocation;
                NonAICSheathPlasmaValues(IntervalsNonPassed,2) = BetaPar;
                NonAICSheathPlasmaValues(IntervalsNonPassed,3) = BetaPerp;
                NonAICSheathPlasmaValues(IntervalsNonPassed,4) = Threshold;
                NonAICSheathPlasmaValues(IntervalsNonPassed,5) = Anisotropy;  
                 
                NonAICSheathPlasmaValues(IntervalsNonPassed,6) = BF_average;
                NonAICSheathPlasmaValues(IntervalsNonPassed,7) = Perp_Mean_ratio;
                NonAICSheathPlasmaValues(IntervalsNonPassed,8) = Perp_Par_ratio;
                NonAICSheathPlasmaValues(IntervalsNonPassed,9) = Ratio;
            end
            index = k;
        else
            index = k;                
        end
    end
    StudiedSheath = StudiedSheath + 1;
    
    %Writing the occurrence to SheathData
    SheathData(sheath,4) = NumberOfEventsInSheath;
    SheathData(sheath,5) = NumberOfIntervalsInSheath;
    SheathData(sheath,6) = NumberOfEventsInSheath/NumberOfIntervalsInSheath;
    SheathData(sheath,7) = AIC_in_NS;
    SheathData(sheath,8) = AIC_in_MS;
    SheathData(sheath,9) = AIC_in_NLE;
    
    SheathData(sheath,10) = F01;
    SheathData(sheath,11) = F12;
    SheathData(sheath,12) = F23;
    SheathData(sheath,13) = F34;
    SheathData(sheath,14) = F45;
    SheathData(sheath,15) = F56;
    SheathData(sheath,16) = F67;
    SheathData(sheath,17) = F78;
    SheathData(sheath,18) = F89;
    SheathData(sheath,19) = F91;
    
    %Moving to a next sheath;
end

AIC_beta = sqrt(AICPlasmaValues(:,2).*AICPlasmaValues(:,2) + AICPlasmaValues(:,3).*AICPlasmaValues(:,3));
Non_AIC_beta = sqrt(NonAICSheathPlasmaValues(:,2).*NonAICSheathPlasmaValues(:,2) + NonAICSheathPlasmaValues(:,3).*NonAICSheathPlasmaValues(:,3));

AIC_beta = AIC_beta(AIC_beta(:,1)>0,:);
Non_AIC_beta = Non_AIC_beta(Non_AIC_beta(:,1)>0,:);

IntervalsPassed/lapslongenough
disp('Occurrence rate of AICs')