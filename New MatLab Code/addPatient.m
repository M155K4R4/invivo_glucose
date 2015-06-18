function [Patient] = addPatient(Patient,id,Data,OtherData)
if isfield(Patient,'id')
    index=find([Patient.id]==id);
else
    index=0;
end

% add to existing id
if index
    Patient(index).Data=[Patient(index).Data, Data];
    Patient(index).OtherData=[Patient(index).OtherData, OtherData];
% create new id
else
    if isfield(Patient,'id')
        index=length(Patient)+1;
    else
        index=1;
    end
    Patient(index).id=id;
    Patient(index).Data=Data;
    Patient(index).OtherData=OtherData;
end

%assignin('base','Patient',Patient);