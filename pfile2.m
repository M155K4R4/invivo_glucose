function [YdatA,YdatRA,wave] = pfile2()

child_handles=get(gca,'children');
num_child=size(child_handles,1);
choice=num_child-1;
choice2=num_child-2;
Ydat=[];
YdatR=[];
while choice>0
    x=get(child_handles(choice),'xdata');
    y=get(child_handles(choice),'ydata');
    Ydat=[Ydat; y.'];
    choice=choice-2;
end

while choice2>0
    x=get(child_handles(choice2),'xdata');
    y=get(child_handles(choice2),'ydata');
    YdatR=[YdatR; y.'];
    choice2=choice2-2;
end

close;

xpoint=20000;
range=90700;
tempy1=Ydat(xpoint);
val=0;
xpoint=75000;
while val<1
    if tempy1 < Ydat(xpoint)
        val=1;
    end
    xpoint=xpoint+1;
end
YdatA=Ydat(xpoint:xpoint+range);

xpoint=20000;
range=90700;
tempy2=YdatR(xpoint);
val=0;
xpoint=75000;
while val<1
    if tempy2 < YdatR(xpoint)
        val=1;
    end
    xpoint=xpoint+1;
end
YdatRA=YdatR(xpoint:xpoint+range);

wave=linspace(1020,1220,range+1);
%figure;
%hold on
%plot(wave,YdatA)
%plot(wave,YdatRA,'r')


end
