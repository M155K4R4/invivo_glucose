function varargout = clinicGUI(varargin)
%CLINICGUI M-file for clinicGUI.fig
%      CLINICGUI, by itself, creates a new CLINICGUI or raises the existing
%      singleton*.
%
%      H = CLINICGUI returns the handle to a new CLINICGUI or the handle to
%      the existing singleton*.
%
%      CLINICGUI('Property','Value',...) creates a new CLINICGUI using the
%      given property value pairs. Unrecognized properties are passed via
%      varargin to clinicGUI_OpeningFcn.  This calling syntax produces a
%      warning when there is an existing singleton*.
%
%      CLINICGUI('CALLBACK') and CLINICGUI('CALLBACK',hObject,...) call the
%      local function named CALLBACK in CLINICGUI.M with the given input
%      arguments.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help clinicGUI

% Last Modified by GUIDE v2.5 07-Nov-2014 11:10:07

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @clinicGUI_OpeningFcn, ...
                   'gui_OutputFcn',  @clinicGUI_OutputFcn, ...
                   'gui_LayoutFcn',  [], ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
   gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before clinicGUI is made visible.
function clinicGUI_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to clinicGUI (see VARARGIN)

% Choose default command line output for clinicGUI
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);
handles.struct1 = varargin;
guidata(hObject, handles);
%assignin('base','hand',handles)

% UIWAIT makes clinicGUI wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = clinicGUI_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in run.
function run_Callback(hObject, eventdata, handles)
% hObject    handle to run (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% assignin('base','hand',handles)
Patient=handles.struct1{1,1};
person=get(handles.name,'String');
conc=str2double(get(handles.concentration,'String'));
num=5;
num1=3;
%pressureS=str2double(get(handles.pressureS,'String'));
%pressureD=str2double(get(handles.pressureD,'String'));
%weight=str2double(get(handles.weightTag,'String'));
%height=str2double(get(handles.heightTag,'String'));
%foods=get(handles.foodsTag,'String');
mn=strcat(person,num2str(conc));
[spectra,spectraNoOutlier,dev,wave]=LaserPlusLIF(person,conc,num,num1,handles);
DataStruct=getDataStruct(conc,spectra,spectraNoOutlier,dev);
OtherDataStruct=getOtherDataStruct(pressureS,pressureD,weight,height,foods);
id=str2double(person); 
Patient=addPatient(Patient,id,DataStruct,OtherDataStruct);

%CHANGE THE STRING IN THE FOLLOWING LINE WHEN CHANGING STRUCTS
assignin('base','Patient',Patient);
assignin('base','wave',wave);

axes(handles.axes1);
plot(wave,mean(spectra,2));

%CHANGE THE STRING IN THE FOLLOWING LINE WHEN CHANGING STRUCTS
save('Patient.mat');



function heightTag_Callback(hObject, eventdata, handles)
% hObject    handle to heightTag (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of heightTag as text
%        str2double(get(hObject,'String')) returns contents of heightTag as a double


% --- Executes during object creation, after setting all properties.
function heightTag_CreateFcn(hObject, eventdata, handles)
% hObject    handle to heightTag (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function foodsTag_Callback(hObject, eventdata, handles)
% hObject    handle to foodsTag (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of foodsTag as text
%        str2double(get(hObject,'String')) returns contents of foodsTag as a double


% --- Executes during object creation, after setting all properties.
function foodsTag_CreateFcn(hObject, eventdata, handles)
% hObject    handle to foodsTag (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function weightTag_Callback(hObject, eventdata, handles)
% hObject    handle to weightTag (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of weightTag as text
%        str2double(get(hObject,'String')) returns contents of weightTag as a double


% --- Executes during object creation, after setting all properties.
function weightTag_CreateFcn(hObject, eventdata, handles)
% hObject    handle to weightTag (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function pressureS_Callback(hObject, eventdata, handles)
% hObject    handle to pressureS (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of pressureS as text
%        str2double(get(hObject,'String')) returns contents of pressureS as a double


% --- Executes during object creation, after setting all properties.
function pressureS_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pressureS (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function pressureD_Callback(hObject, eventdata, handles)
% hObject    handle to pressureD (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of pressureD as text
%        str2double(get(hObject,'String')) returns contents of pressureD as a double


% --- Executes during object creation, after setting all properties.
function pressureD_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pressureD (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function name_Callback(hObject, eventdata, handles)
% hObject    handle to name (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of name as text
%        str2double(get(hObject,'String')) returns contents of name as a double


% --- Executes during object creation, after setting all properties.
function name_CreateFcn(hObject, eventdata, handles)
% hObject    handle to name (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function concentration_Callback(hObject, eventdata, handles)
% hObject    handle to concentration (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of concentration as text
%        str2double(get(hObject,'String')) returns contents of concentration as a double


% --- Executes during object creation, after setting all properties.
function concentration_CreateFcn(hObject, eventdata, handles)
% hObject    handle to concentration (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
