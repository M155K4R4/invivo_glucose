person='Sabbir';
conc=3;
num=1;
num1=0;

[spectra,spectraNoOutlier,dev,wave]=LaserPlusLIF2(person,conc,num,num1);
DataStruct=getDataStruct(conc,spectra,spectraNoOutlier,dev);
OtherDataStruct=getOtherDataStruct({});
id=40; % id=getId();
Patient=addPatient(Patient,id,person,DataStruct,OtherDataStruct);
% action= strcat('[',mn,',',mn,'minStd,',mn,'DEV,wave]=LaserPlusLIF(person,conc,num,num1,handles);');
% eval(action);

assignin('base','wave',wave);