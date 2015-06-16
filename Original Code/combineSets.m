i=1;
while i<=size(Patient,2)
x=Patient(i).Data;
xx=Patient(i).OtherData;
Patient2=addPatient(Patient2,Patient(i).id,x,xx);
i=i+1;
end

