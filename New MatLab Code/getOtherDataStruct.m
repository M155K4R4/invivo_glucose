function[OtherDataStruct]=getOtherDataStruct(bloodPressureS,bloodPressureD,weight,height,foods)
bloodPressureSField='bloodPressureS';
bloodPressureDField='bloodPressureD';
weightField='weight';
heightField='height';
foodsField='foods';
OtherDataStruct=struct(bloodPressureSField,bloodPressureS,bloodPressureDField,bloodPressureD,weightField,weight,heightField,height,foodsField,foods);