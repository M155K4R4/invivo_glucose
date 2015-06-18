%This is for 150k samples/sec

function [YdatA,YdatB,wave] = pfile1()
%function [Ydat,Ydat2,wave] = pfile1()


child_handles=get(gca,'children');
num_child=size(child_handles,1);
choice=num_child;
Ydat=[];
while choice>0
    x=get(child_handles(choice),'xdata');
    y=get(child_handles(choice),'ydata');
    Ydat=[Ydat; y.'];
    choice=choice-1;
end
%Ydat2=Ydat;
close;

xpoint=45000;
range=182400;
tempy1=Ydat(xpoint);
val=0;
xpoint=150000;
while val<1
    if tempy1 < Ydat(xpoint)
        val=1;
    end
    xpoint=xpoint+1;
end
YdatA=Ydat(xpoint:xpoint+range);
dist=25600;
xpointNew=xpoint+range+dist;
YdatB=Ydat(xpointNew:xpointNew+range);
YdatB=flipud(YdatB);

wave=linspace(1020,1220,range+1);



end
