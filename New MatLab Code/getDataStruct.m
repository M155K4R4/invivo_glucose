function[DataStruct]=getDataStruct(conc,spectra,spectraNoOutlier,dev)
concField='conc';
spectraField='spectra';
noOutlierSpectraField='noOutlierSpectra';
devField='dev';
timeField='time';

DataStruct=struct(concField,conc,spectraField,spectra,noOutlierSpectraField,spectraNoOutlier,devField,dev,timeField,datestr(now));


