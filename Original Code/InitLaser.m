function [obj] = InitLaser()

% Find a GPIB object (Laser Tuner).
obj1 = instrfind('Type', 'gpib', 'BoardIndex', 0, 'PrimaryAddress', 17, 'Tag', '');


% Create the GPIB object if it does not exist
% otherwise use the object that was found.
if isempty(obj1)
    obj1 = gpib('NI', 0, 17);
else
    fclose(obj1);
    obj1 = obj1(1)
end

% Connect to instrument object, obj1.
fopen(obj1);

obj=obj1;

end
