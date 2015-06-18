idNum=190;
i=1;
index=find([PatientTOT.id]==idNum);

PatientTOT(index).OtherData(i).bloodPressureS=0;
PatientTOT(index).OtherData(i).bloodPressureD=0;
PatientTOT(index).OtherData(i).weight=150;
PatientTOT(index).OtherData(i).height=6*12 + 0;
%PatientTOT(index).OtherData.foods='';